#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#Renta	   
#Tipo impositivo
#Menos de 10000€
#5%
#Entre 10000€ y 20000€	
#15%
#Entre 20000€ y 35000€
#20%
#Entre 35000€ y 60000€
#30%
#Más de 60000€
#45%

#Escribir un programa que pregunte al usuario su renta anual 
# y muestre por pantalla el tipo impositivo que le corresponde. (10p)

renta=float(input("Introduce tu renta anual: "))

if renta<10000:
    print("Su tipo impositivo es de 5% ")
elif 10000<= renta <20000:
    print("Su tipo impositivo es de 15%")
elif 20000<= renta <35000:
    print("Su tipo impositivo es de 20%")
elif 35000<= renta <60000:
    print("Su tipo impositivo es de 30%")
else:
    print ("Su tipo impositivo es de 45%")