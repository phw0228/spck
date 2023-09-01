document.addEventListener('DOMContentLoaded', () => {
  const myCanvas = document.getElementById('myCanvas');
  const context = myCanvas.getContext('2d');
  const agreeCheckbox = document.getElementById('agree');
  const submitButton = document.getElementById('submitButton');
  
  let drawing = false;
  
  
  myCanvas.addEventListener('touchstart', touchStartHandler, false);
  myCanvas.addEventListener('touchmove', touchMoveHandler, false);
  myCanvas.addEventListener('touchend', () => { drawing = false; }, false);
  agreeCheckbox.addEventListener('change', toggleSubmitButton, false);
  
  document.getElementById('eraseButton').addEventListener('click', function() {
    clearCanvas();
  // agreeCheckbox 체크 해제
    document.getElementById('agree').checked = false;
  // 제출 버튼 활성화 상태 업데이트
    toggleSubmitButton();
  });

  document.querySelectorAll('form input:not([type="checkbox"])').forEach(input => {
    input.addEventListener('input', toggleSubmitButton, false);
  });
  
  function touchStartHandler(event) {
    event.preventDefault();
    drawing = true;
    context.beginPath();
    context.moveTo(getTouchPos(event).x, getTouchPos(event).y);
  }

  function touchMoveHandler(event) {
    event.preventDefault();
    if (!drawing) return;
    context.lineTo(getTouchPos(event).x, getTouchPos(event).y);
    context.stroke();
  }

  function getTouchPos(event) {
    const rect = myCanvas.getBoundingClientRect();
    return {
      x: event.touches[0].clientX - rect.left,
      y: event.touches[0].clientY - rect.top,
    };
  }
  
  function isCanvasEmpty(canvas) {
    var blank = document.createElement('canvas');
    blank.width = canvas.width;
    blank.height = canvas.height;

    return canvas.toDataURL() === blank.toDataURL();
  }

  function clearCanvas() {
    context.clearRect(0, 0, myCanvas.width, myCanvas.height);
    toggleSubmitButton(); // 추가한 코드
  }

  function toggleSubmitButton() {
    const isFormValid = agreeCheckbox.checked 
      && Array.from(document.querySelectorAll('form input:not([type="checkbox"])')).every(input => input.value.trim() !== '') 
      && !isCanvasEmpty(document.getElementById('myCanvas'));
      submitButton.disabled = !isFormValid;
      submitButton.classList.toggle('active', isFormValid);
  }
  
});

/*
캡처해서 이미지 띄우기 및 url data 로 변환
document.getElementById('captureButton').onclick = function () {
    html2canvas(document.body).then(function (canvas) {
      var imgURL = canvas.toDataURL();
      console.log(imgURL);
      var img = document.createElement('img');
      img.src = imgURL;
      document.body.appendChild(img);
    });
  };

*/