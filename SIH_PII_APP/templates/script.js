document.getElementById('fileInput').addEventListener('change', function(event) {
  const file = event.target.files[0];
  if (file) {
    document.getElementById('fileName').textContent = file.name;
  } else {
    document.getElementById('fileName').textContent = 'No file chosen';
  }
});

document.getElementById('browseFileBtn').addEventListener('click', function() {
  document.getElementById('fileInput').click();
});