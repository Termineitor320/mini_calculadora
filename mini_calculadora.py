import math

print("-------------------------")
print("1-- sumar (x+y) ") 
print("2-- restar (x-y) ")
print("3-- multiplicar (x*y) ")
print("4-- division (x/y) ")
print("5-- potencia (x**y) ")
print("6-- logaritmo (log*y) ")
print("_________________________")

print("----------------------------------------------------------------------------------------------")
# input
x = int(input("digite el primer numero: "))
y = int(input("digite el segundo numero: "))
print("----------------------------------------------------------------------------------------------")
opcion= int(input("seleccione la operacion que desea realizar: "))
print("----------------------------------------------------------------------------------------------")

# processing
if opcion== 1:
    r =(x+y) 
elif opcion== 2:
    r = (x-y)
elif opcion== 3:
    r = (x*y)
elif opcion== 4:
    r = (x/y)
elif opcion== 5:
    r = (x**y)
elif opcion== 6: #output
    r = (Log*y)
else:
    r = "opcion no valida" #output

#output
print("resultado: " + str(r))

     
        


