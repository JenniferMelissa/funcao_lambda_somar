#funcao lambda
#simplifica a funcao
#é uma abreviacao de uma funcao, uma forma simplificada de fazer as funcoes
# é ideal para poucos itens de cofigos, programas bem pequenos mesmo, 3 a 4 linhas



#fazendo funcao sem lambda
# def somar(x,y):
#     soma = x + y
#     return soma
#retorn retorna so um valor


#funcao com lambda
somar = lambda x,y: x + y
#variavel = lambda'parametros': o que funcao vai retornar

#programa principal
x = int(input('Informe o valor de x: '))
y = int(input('Informe o valor de y: '))

print(f'A soma de {x} e {y} é: ')

