/* idxjs.js */

// 관리자 로그인 버튼 애니메이션
const managerButton = document.querySelector("#manager-button");
const managerButtonAnimation = anime({
  targets: managerButton,
  opacity: [0, 1],
  translateY: [-150, 0],
  duration: 1500,
  easing: "easeInOutQuad",
});

// 근로자 로그인 버튼 애니메이션
const workerButton = document.querySelector("#worker-button");
const workerButtonAnimation = anime({
  targets: workerButton,
  opacity: [0, 1],
  translateY: [150, 0],
  duration: 1500,
  easing: "easeInOutQuad",
});

// 페이지가 로드되면 애니메이션을 시작합니다.
document.addEventListener("DOMContentLoaded", () => {
  managerButtonAnimation.play();
  workerButtonAnimation.play();

  // 버튼 클릭 이벤트 설정
  workerButton.addEventListener("click", () => {
    window.location.href = "{{url_for('feed')}}";
  });

  // 관리자 로그인 버튼 클릭 이벤트
  managerButton.addEventListener("click", () => {
    // 구글 로그인 API를 초기화합니다.
    gapi.load("auth2", () => {
      gapi.auth2.init();
      gapi.auth2.getAuthInstance().signIn();
    });
  });
});
