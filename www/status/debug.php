<?php
if (! isset ($_COOKIE['userId'])){
        header('Location:/status/login.php');
        die;
}

$ip = empty($_GET['ip']) ? 0 : $_GET['ip'];
$port = empty($_GET['port']) ? 4028 : intval($_GET['port']);

if (!$ip)
	exit;
if (preg_match('/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/', $ip)) {
    $output = array();
    exec("python debug.py " . $ip . " " . $port, $output);
    foreach ($output as $o)
		echo $o . "<br />";
}
