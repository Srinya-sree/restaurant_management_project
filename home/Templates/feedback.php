<?php
// Database connection
$servername = "localhost";
$username = "root";   // your DB username
$password = "";       // your DB password
$dbname = "restaurant_db";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$message = "";

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $comment = $conn->real_escape_string($_POST['comment']);

    $sql = "INSERT INTO feedback (comment) VALUES ('$comment')";

    if ($conn->query($sql) === TRUE) {
        $message = "Thank you for your feedback!";
    } else {
        $message = "Error: " . $conn->error;
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Customer Feedback</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 50px;
    }
    h2 {
      color: #343a40;
    }
    form {
      margin-top: 20px;
    }
    textarea {
      width: 100%;
      padding: 10px;
      border-radius: 5px;
      border: 1px solid #ccc;
      margin-bottom: 10px;
    }
    button {
      background-color: #343a40;
      color: white;
      padding: 10px 15px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    button:hover {
      background-color: #495057;
    }
    .message {
      margin-top: 15px;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h2>Leave Your Feedback</h2>

  <form method="POST">
    <textarea name="comment" rows="5" placeholder="Write your feedback here..." required></textarea><br>
    <button type="submit">Submit Feedback</button>
  </form>

  <?php if ($message != ""): ?>
    <div class="message"><?php echo $message; ?></div>
  <?php endif; ?>

</body>
</html>

<?php $conn->close(); ?>
