<?php
//Database connection
$servername = "localhost";
$username = "root";
$password="";
$dbname = "restaurant_db";
$conn = new mysqli($servername,$username,$password,$dbname);
//check connection
if($conn->connect_error){
    die("Connection failed:".$conn->connect_error)
}

$message="";
//Handle form submission

if ($_SERVER["REQUEST_METHOD"]=="POST"){
    $comment = $conn->real_escape_string($_POST['comment']);

    $sql = "INSERT INTO feedback(comment) VALUES('$comment')";
    if($conn->query($sql)===TRUE){
        $message="Thank you for your feedback!";
    }else{
        $message = "Error:".$conn->error;
    }
}
?>
