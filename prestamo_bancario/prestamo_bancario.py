#programa para adquirir un prestamo segun su salario y si tiene deudas anteriores

#input 
salario = int(input( " cuanto es su salario : "))
deuda = input( " ud tiene otra deuda que no ha pagado (si o no) : ")

#processing and output 
if salario >= 945200:
    if deuda == "no":
        print("su prestamo ha sido aprobado")
    else:
        print("su prestamo ha sido denegado")
elif salario <945200:
    print( " su prestamo ha sido denegado ")