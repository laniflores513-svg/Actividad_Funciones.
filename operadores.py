a = 5
b = 3

#operadores relacionales
identico = (a == b) #false
mayorque = (a > b) #true
menorque = (a < b) #false
mayorigualque = (a >= b) #true
menorigualque = (a <= b) #false
diferente = (a != b) #true

print(identico)
print(mayorque)
print(menorque)
print(mayorigualque)
print(menorigualque)
print(diferente)

#operadores logicos AND(&&) OR(//) NOT(!)
y = (a > b and b < a) #true:Ambas expresiones sean verdaderas
o = (a > b or b < a) #true:solo si una es verdadera
no = (not(a > b )) #Da lo contrario al resultado

print("--------------------------------------------------------")
print(y)
print(o)
print(no)

#operadores de asignacion
print("---------------------------------------")
a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a%=b
print(a)