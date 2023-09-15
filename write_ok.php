<?php

// MySQL 연결
$host = "localhost";
$user = "root";
$pw = "0228";
$dbName = "board";

$conn = new mysqli($host, $user, $pw, $dbName);

// 유저 입력 데이터 가져오기
$title = $_POST['title'];
$content = $_POST['content'];

// 데이터베이스에 데이터 저장
$sql = "INSERT INTO board (title, content) VALUES ('$title', '$content')";

$result = $conn->query($sql);

// 데이터베이스 연결 종료
$conn->close();

// 성공 메시지 출력
if ($result) {
  echo "<script>alert('게시글이 작성되었습니다.');</script>";
} else {
  echo "<script>alert('게시글 작성 실패했습니다.');</script>";
}

// 목록 페이지로 이동
header('Location: index.php');

?>
