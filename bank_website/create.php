<?php
$link=mysql_connect('localhost','root','');
if (!$link){
	die('Failed to connect to server'.mysql_error());

}
$db=mysql_select_db("bank");
if (!$db){
	die("Unable to select database");
}
$id=rand(1000,100000);
$name=$_POST['name'];
$email=$_POST['email'];
$ms=$_POST['ms'];
$age=$_POST['age'];
$Amount=$_POST['deposit'];
if ($Amount<1000) {
	//deposit failed
	header("location:create.html");
	exit();
}
else{
	$q="insert into tab values('$id','$name','$email','$ms','$age','$Amount')";
	mysql_query($q,$link) or die("Unable to insert");
	mysql_close($link);
echo "<br> Congrats!Your account has been created </br>";
echo "<h3>Note!Your account number is :".$id;
}
?>