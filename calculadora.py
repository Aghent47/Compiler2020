# -*- enconding: utf-8 -*-
from calculatorOrientedObjects import Calculator

objC = Calculator()

def Menu():
    """Funcion que Muestra el Menu"""
    print ("""************
                     Calculadora

**********************     Menu       **********************
************************************************************
****************    1) Suma                 ****************    
****************    2) Resta                ****************    
****************    3) Multiplicacion       ****************    
****************    4) Division             ****************    
****************    5) Salir                ****************
************************************************************
""") 

def Calculadora():
    """  Funcion Para Calcular Operaciones Aritmeticas  """
    Menu()
    op = int(input("\nSelecione Opción: "))

    while (op >0 and op <5):
        numberOne = float(input("Ingrese Numero: "))
        numberTwo = float(input("Ingrese un segundo Numero: "))
        if (op==1):
            objC.sumar(numberOne,numberTwo)
            op = int(input("Selecione Opción: "))
        elif(op==2):
            objC.restar(numberOne,numberTwo)
            op = int(input("Selecione Opción: "))
        elif(op==3):
            objC.mult(numberTwo,numberTwo)
            op = int(input("Selecione Opción: "))
        elif(op==4):
            try:
                objC.div(numberOne,numberTwo)
                op = int(input("Selecione Opción: "))
            except ZeroDivisionError:
              print ("Operación Invalida!!!")
              op = int(input("Selecione Opción: "))
Calculadora()