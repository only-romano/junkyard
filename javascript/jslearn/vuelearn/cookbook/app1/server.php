<?php
header('Content-Type: application/json');
$products = array("vista", "windows", "apple", "linux");

if(isset($_GET['product']))
{
  header("Status: 200 OK");
  $product = htmlentities($_GET['product']);

  if (!in_array($product, $products))
  {
    echo json_encode(array(
      'product' => $product,
      'count' => random_int(1, 25)
    ));
    array_push($products, $product);
  }
  else
  {
    echo json_encode(array(
      'error' => 'Product already Exist'
    ));
  }
}
else
{
    header("Status: 500 Server Error");
}

?>