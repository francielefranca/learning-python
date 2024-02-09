#CALCULADORA - PYCALC

print('\n\n\nPYCALC - CALCULADORA PYTHON' + 
      '\n\nEscolha qual funcionalidade da calculadora, voce deseja utilizar:' +
      '\n 1 - Soma de dois numeros' + 
      '\n 2 - Subtracao de dois numeros' +
      '\n 3 - Multiplicacao de dois numeros' +
      '\n 4 - Divisao de dois numeros' + 
      '\n\nATENÇÃO: Digite apenas dois numeros!!')

opcaoCalculadora = int(input('\nDigite a opção escolhida para a calculadora: '))
numero1 = int(input('\nDigite o primeiro número: '))
numero2 = int(input('\nDigite o segundo número: '))

def calculo(op: int):
    match op:
        case 1:
            resultado = numero1 + numero2
            return resultado
        case 2:
            if(numero1 > numero2):
                resultado = numero1 - numero2
                return resultado
            else:
                resultado = numero2 - numero1
                return resultado
        case 3:
            resultado = numero1 * numero2
            return resultado
        case 4:
            if(numero1 > numero2):
                resultado =  numero1/numero2
                return resultado
            elif(numero2 > numero1):
                resultado =  numero2/numero1
                return resultado
        case _ :
            resultado = 0
            return resultado

def funcao(op: int):
    match op:
        case 1:
            return 'soma'
        case 2:
            return 'subtracao'
        case 3:
            return 'multiplicacao'
        case 4:
            return 'divisao'
        case _ :
            return 'nenhuma operacao valida'
    
print('\n##############################################################')
print('A funcionalidade escolhida foi: ' + funcao(opcaoCalculadora))
print('E o resultado obtido foi = ' + str(calculo(opcaoCalculadora)))