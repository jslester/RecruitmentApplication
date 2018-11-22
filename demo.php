<?php 

define('DB_NAME', 'demo');
define('DB_USER', 'root');
define('DB_PASSWORD', ' ');
define('DB_HOST', 'localhost');

$link = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);


if (!$link){
	die('Could not connect: ' . mysql_error());
}

$value = $_POST['FirstName'];
$value2 = $_POST['LastName'];
$value3 = $_POST['Rating'];

$sql = "INSERT INTO demo (FirstName,LastName,Rating) VALUES ('$value', '$value2', '$value3')";

if (!$result = $link->query($sql)) {
    // Oh no! The query failed. 
    echo "Sorry, the website is experiencing problems.";

    // Again, do not do this on a public site, but we'll show you how
    // to get the error information
    echo "Error: Our query failed to execute and here is why: \n";
    echo "Query: " . $sql . "\n";
    echo "Errno: " . $link->errno . "\n";
    echo "Error: " . $link->error . "\n";
    exit;
}

$link->close();
echo('Submitted!');
?>
<br><br>
<a href="demo-form.php">Return to Page!</a>
