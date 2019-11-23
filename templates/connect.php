<?php
$con = mysql_connect('127.0.0.1:5000/','root',);
$db = mysql_select_db('Survey_attempt');

if($con)
{echo 'Successfully stored survey data'}
else {'error.'}
}




?>
