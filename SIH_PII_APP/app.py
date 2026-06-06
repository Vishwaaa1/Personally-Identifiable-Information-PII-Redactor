from flask import Flask, render_template, request, send_file, redirect, url_for
import os
from werkzeug.utils import secure_filename
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
import fitz  # PyMuPDF
import io

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads/'
PROCESSED_FOLDER = 'processed/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max file size: 16MB

# Allowed extensions
ALLOWED_EXTENSIONS = {'pdf'}

# Load the YOLO model
model = YOLO("Detection/runs/detect/train/weights/best.pt")

def allowed_file(filename):
    """Check if the uploaded file is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def overwrite_with_noise(image, x1, y1, x2, y2):
    h, w = y2 - y1, x2 - x1
    noise = np.random.randint(0, 256, (h, w, 3), dtype=np.uint8)
    image[y1:y2, x1:x2] = noise


# Your existing PII redaction functions here:
def detect_and_mask_pii_in_image(image):
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = model.predict(rgb_image, imgsz=640, conf=0.8)

    for result in results:
        for box in result.boxes.xyxy:
            x1, y1, x2, y2 = map(int, box)
            overwrite_with_noise(image, x1, y1, x2, y2)
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 0), -1)  # Mask with a black box
    return image

def extract_images_from_pdf(pdf_path):
    pdf_doc = fitz.open(pdf_path)
    images = []
    image_locations = []
    
    for page_num in range(pdf_doc.page_count):
        page = pdf_doc.load_page(page_num)
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_doc.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            image = np.array(image)

            images.append(image)
            image_locations.append((page_num, img, xref))

    return images, image_locations, pdf_doc

def save_images_to_pdf(pdf_doc, redacted_images, image_locations, output_pdf_path):
    for i, (page_num, img_info, xref) in enumerate(image_locations):
        page = pdf_doc.load_page(page_num)
        redacted_image = Image.fromarray(redacted_images[i])
        
        img_byte_arr = io.BytesIO()
        redacted_image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        pix = fitz.Pixmap(io.BytesIO(img_byte_arr))
        page.replace_image(xref, pixmap=pix)

    pdf_doc.save(output_pdf_path)
    pdf_doc.close()

def detect_and_mask_pii_in_pdf(pdf_path, output_pdf_path):
    images, image_locations, pdf_doc = extract_images_from_pdf(pdf_path)
    redacted_images = []

    for image in images:
        redacted_image = detect_and_mask_pii_in_image(image)
        redacted_images.append(redacted_image)

    save_images_to_pdf(pdf_doc, redacted_images, image_locations, output_pdf_path)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(pdf_path)

        output_pdf_path = os.path.join(app.config['PROCESSED_FOLDER'], filename.replace('.pdf', '_redacted.pdf'))

        # Redact PII
        detect_and_mask_pii_in_pdf(pdf_path, output_pdf_path)

        file_url = url_for('download_file', filename=filename.replace('.pdf', '_redacted.pdf'), _external=True)

        return {'success': True, 'file_url': file_url}
    else:
        return {'success': False}, 400


@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['PROCESSED_FOLDER'], filename), as_attachment=True)

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(PROCESSED_FOLDER, exist_ok=True)
    app.run(debug=True)
