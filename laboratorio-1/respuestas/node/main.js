
function main() {
    console.log("Laboratorio 1");
    const result = sum(2,2);
     console.log("El resultado de la suma es "+ result);
     const resultWithMe = dependWithMe(3,2);
     console.log("El resultado de la operacion es "+ resultWithMe);
}
function sum(x,y){
    return x+y;
}

function dependWithMe(x, y){
    if (x > y) return x * y;
    if (x < y) return (x * y)-(x + y);
    return (x * y)*2;
}
main();