<?php
session_start();
require 'db.php';

if (!isset($_SESSION['user_id'])) {
    http_response_code(401);
    exit('login required');
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    exit;
}

$to = $_POST['to_account'];
$amount = (int)$_POST['amount'];

$stmt = $pdo->prepare('UPDATE accounts SET balance = balance - ? WHERE user_id = ?');
$stmt->execute([$amount, $_SESSION['user_id']]);
$stmt = $pdo->prepare('UPDATE accounts SET balance = balance + ? WHERE number = ?');
$stmt->execute([$amount, $to]);

echo 'transfer complete';
