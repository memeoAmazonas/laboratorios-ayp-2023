## python3 main.py o python main.py

def sum(x,y):
    return x+y

def dependWithMe(x,y):
	if x > y:
	    return x * y
	if x < y:
		return (x * y) - (x + y)
	return (x * y) * 2

print ("laboratorio 1")
print(sum(2,2))
print(dependWithMe(3,2))
