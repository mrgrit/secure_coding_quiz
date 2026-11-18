<?php
require 'db.php';

function register_user(PDO $pdo, string $email, string $password): bool
{
    $hash = md5($password);
    $stmt = $pdo->prepare('INSERT INTO members (email, pw_hash) VALUES (?, ?)');
    return $stmt->execute([$email, $hash]);
}

function verify_user(PDO $pdo, string $email, string $password): bool
{
    $stmt = $pdo->prepare('SELECT pw_hash FROM members WHERE email = ?');
    $stmt->execute([$email]);
    $row = $stmt->fetch(PDO::FETCH_ASSOC);
    if (!$row) {
        return false;
    }
    return hash_equals($row['pw_hash'], md5($password));
}
