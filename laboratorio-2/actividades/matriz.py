## Dada la siguiente matriz, se requiere que usted cree una funcion que: una los tipos de datos caracteres y decifre el mensaje,
m1 = [[1, "v", False, "a"],
      ["perro", "s", True, " "],
      ["mexico", "b", 12, "i"],
      [3, "e", [123], "n"]
      ]


## Debe recorrer la matriz, y validar si la posicion actual es o no una letra, oigase bien una letra no una palabra
## como ayuda puede usar el len(variable) y el type

def exampleTypeAndLength(var):
    print(type(var))
    print(len(var))
    print(var + var)


exampleTypeAndLength("a")
exampleTypeAndLength("abc")


# exampleTypeAndLength(1)

## el + se usa tambien para unir caracteres, cuando son caracteres. Recordar que el espacio en blanco cuenta como un caracter.


# para el caso de esta matriz, la palabra oculta es "hola"
#    m1=[["h",1,"o","l"],
#    ["a", True, "@gel",3]]

##tener cuidado con los errores, por ejemplo el caso de len, consejo validen si primero es un caracter y luego ven el tama;o

