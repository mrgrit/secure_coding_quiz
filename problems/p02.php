<?php
session_start();
$pdo = new PDO('sqlite:/var/www/data/board.db');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $stmt = $pdo->prepare('INSERT INTO posts (author, body) VALUES (?, ?)');
    $stmt->execute([$_POST['author'], $_POST['body']]);
    header('Location: /board.php');
    exit;
}

$posts = $pdo->query('SELECT author, body FROM posts ORDER BY id DESC')->fetchAll(PDO::FETCH_ASSOC);
$keyword = $_GET['q'] ?? '';
?>
<!DOCTYPE html>
<html>
<body>
<h1>게시판</h1>
<p>검색어: <?php echo $keyword; ?></p>
<?php foreach ($posts as $post) { ?>
  <div class="post">
    <strong><?php echo $post['author']; ?></strong>
    <p><?php echo $post['body']; ?></p>
  </div>
<?php } ?>
<form method="post">
  <input name="author">
  <textarea name="body"></textarea>
  <button type="submit">등록</button>
</form>
</body>
</html>
