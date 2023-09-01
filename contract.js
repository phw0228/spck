/* contract fetch */
fetch('contract.txt')
  .then(response => response.text())
  .then(text => {
    var textarea = document.getElementById('contract-text');
    textarea.value = text;
  })
  .catch(error => {
    console.error('Error:', error);
  });