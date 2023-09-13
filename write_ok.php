<?php

$conn = mysqli_connect("localhost", "root", "", "board");
// 제목과 내용을 가져옵니다.
$title = $_POST['title'];
$content = $_POST['content'];

// DB에 게시글을 저장합니다.
$sql = "INSERT INTO board (title, content, created_at)
VALUES ('$title', '$content', NOW())";
$result = mysqli_query($conn, $sql);

// 게시글 작성 성공 여부를 확인합니다.
if ($result) {
  // 게시글 작성 성공
  header("Location: index.php");
} else {
  // 게시글 작성 실패
  echo "게시글 작성에 실패했습니다.";
}

?>
