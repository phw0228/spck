/* rate fetch */
var rate_url = 'https://api.odcloud.kr/api/15068774/v1/uddi:21d816e5-6c44-4e30-903d-e98e30a4f227?page=1&perPage=1&serviceKey=Ygfcgp9s3CaMllh9Pi4w6yUn044brEUPDQMdUSlZF1Ato6NXse12GzKi1zXIgXuSK0uSux1sLLOiFsNNnQ1aiQ%3D%3D';

// Fetch API를 사용하여 데이터 가져오기
fetch(rate_url)
  .then(response => response.json())
  .then(data => {
    // 데이터 처리
    var rate = data.data[0]['시간급'];
    
    // 시간급 데이터를 textarea에 삽입
    var textarea = document.querySelector('textarea');
    var originalText = textarea.value;
    var modifiedText = originalText.replace('시급', '시급(' + rate +')')
    textarea.value = modifiedText;
  })
  .catch(error => {
    // 에러 처리
    console.error('Error:', error);
  });