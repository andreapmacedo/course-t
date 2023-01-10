class Calculadora:
    def soma(self, x, y):
        return x + y

class CalculadoraDecorada:
    def __init__(self, calculadora):
        self.calculadora = calculadora      


    def soma(self, x, y):
        
        numberList = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
        return self.calculadora.soma(numberList.index(x)+1, numberList.index(y)+1)


if __name__ == "__main__":
    calculadora = Calculadora()
    print("10 + 20 =")
    calculadora.soma(10, 20) 
    # print(calculadora.soma(10, 20))
    
    calculadoraDecorada = CalculadoraDecorada(calculadora)
    print("'eight' + 'two' =", calculadoraDecorada.soma("eight", "two"))    