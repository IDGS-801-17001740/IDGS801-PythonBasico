import os

class OperasBas:
    # declaración de las propiedades

    # declaración de constructor
    def _init_(self):
        pass
    # declaración de métodos

    def suma(self, num1, num2):
        res = num1 + num2
        return res

    def resta(self, num1, num2):
        res = num1 - num2
        return res

    def multiplicacion(self, num1, num2):
        res = num1 * num2
        return res

    def division(self, num1, num2):
        res = num1 / num2
        return res
jnaranjo@quemari.com

def main():
    ob = OperasBas()
    opt = -1
    res = 0
    while (opt != 0):
        opt = int(
            input('1.- Suma\n2.- Resta\n3.- Multiplicación\n4.- División\n0.- Salir\n'))
        if (opt == 0):
            print("Saliendo....")
            break
        os.system('clear')
        num1 = int(input('Ingresa el primer número:'))
        num2 = int(input('Ingresa el segundo número:'))
        if (opt == 1):
            res = ob.suma(num1, num2)
            print('El resultado de la suma es: {}'.format(res))
        elif (opt == 2):
            res = ob.resta(num1, num2)
            print('El resultado de la resta es es: {}'.format(res))
        elif (opt == 3):
            res = ob.multiplicacion(num1, num2)
            print('El resultado de la multiplicación es: {}'.format(res))
        elif (opt == 4):
            res = ob.division(num1, num2)
            print('El resultado de la división es: {}'.format(res))
        

if __name__ == "__main__":
    main()
