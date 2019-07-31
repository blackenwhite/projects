<?php
$link=mysql_connect('localhost','root','');
if (!$link){
	die('Failed to connect to server'.mysql_error());

}

$db=mysql_select_db("bank");
if (!$db){
	die("Unable to select database");
}

$key=$_POST['id'];
$amount=$_POST['amount'];

$result=mysql_query("SELECT * FROM tab");
while($a=@mysql_fetch_array($result)){
	$count=0;
	$am=0;
	$id=$a['id'];

	//storing the amount already present in the bank
	if ($key==$id){
		$am=$a['amount'];
		$count+=1;
	}

	}
if ($count==0){
		echo "There is no Such account with this ID. Try Again!";
		
	}
else {
	if($am<$amount){
	echo "There is  not that much money in your account";
}   
    else{
    	$temp=$am-$amount;
    	while($a=@mysql_fetch_array(mysql_query("SELECT * FROM tab WHERE id ='$key'"))){
    		$a['amount']=$temp;


    	}
    	echo "Transaction successful";


    }
}



