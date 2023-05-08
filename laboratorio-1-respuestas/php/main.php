
<!-- php main.php -->
<?php
echo "laboratorio 1 \n";
function sum(int $x, int $y){
    return $x+$y;
}
function dependWithMe(int $x, int $y){
    if ($x > $y) return $x * $y;
    if ($x < $y) return ($x * $y)-($x + $y);
    return ($x * $y) *2;
}

 $result = sum(2,2);
echo "El resultado de la suma es: ($result) \n";
$resultWithMe = dependWithMe(2,2);
echo "El resultado es: ($resultWithMe) \n";
?>