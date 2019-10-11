<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

$options = array(
  array('id' => 1, 'text' => 'Hello'),
  array('id' => 2, 'text' => 'PHP'),
  array('id' => 3, 'text' => 'World')
);

echo json_encode($options);

?>