  //document.getElementById('browseFileBtn').addEventListener('click', () => {
   // document.getElementById('fileInput').click();
  //});
  
  document.getElementById('fileInput').addEventListener('change', (event) => {
    const fileName = event.target.files[0].name;
    document.getElementById('fileName').textContent = fileName;
  });
  
  document.getElementById('about-btn').addEventListener('click', () => {
    const aboutPanel = document.getElementById('about-panel');
    aboutPanel.classList.toggle('active');
  });
  
  document.getElementById('contact-btn').addEventListener('click', () => {
    const contactPanel = document.getElementById('contact-panel');
    contactPanel.classList.toggle('active');
  });

  document.getElementById('inst-btn').addEventListener('click', () => {
    const contactPanel = document.getElementById('instruction-panel');
    contactPanel.classList.toggle('active');
  });
  
  