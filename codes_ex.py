#codes_ex.py
# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 



def conv_celsus():
  #F = (C * 9/5)+32
  celsus = input(f"Digite a temperatura em celsusl: ")
  celsus = celsus.replace (",",".")

  celsus = float(celsus)
  fare = (celsus * 9/5) + 32

  print("A temperatura em fahrenheit é: ", fare)

def media_notas():
  nota1 = input(f"Digite a primeira nota: ")
  nota2 = input(f"Digite a segunda nota: ")
  nota3 = input(f"Digite a terceira nota: ")

  nota1 = nota1.replace (",",".")
  nota1 = float(nota1)

  nota2 = nota2.replace (",",".")
  nota2 = float(nota2)

  nota3 = nota3.replace (",",".")
  nota3 = float(nota3)

  media = (nota1 + nota2 + nota3) / 3

  print("A média final é:", media)


def volume_caixa():
  altura = input(f"Digite a altura da caixa d'água: ")
  raio = input(f"Digite o raio da caixa d'água: ")

  altura = altura.replace(",",".")
  raio = raio. replace(",",".")

  altura = float(altura)
  raio = float(raio)

  volume = 3.14 * (raio **2) * altura

  print("O volume da caixa d'água: ", volume)

def area_esfera():
  raio = input(f"Digite o raio da esfera: ")
  raio = raio.replace(",",".")
  raio = float(raio)

  area = (4 * 3.14) * (raio ** 2)

  print("A área da esfera é: ", area)

def area_circulo():
  raio = input(f"Digite o raio do circulo: ")
  raio = raio.replace(",",".")
  raio = float(raio)

  area = 3.14 * (raio ** 2)

  print ("A área do circulo é: ", area)

def area_retangulo():
  altura = input(f"Digite a altura do retângulo: ")
  base = input(f"Digite a base do retângulo: ")

  altura = altura.reajuste(",",".")
  altura = float(altura)

  base = base.replace(",",".")
  base = float(base)

  area = altura * base

  print ("A área do retângulo é: ", area)

def area_quadrado():
  lado = input("Digite o lado do quadrado: ")
  lado = lado.replace(",",".")
  lado = float(lado)

  area = lado ** 2

  print ("A área do quadrado é: ", area)

def aumento_sal():
  salario = input(f"Digite o salário:")
  reajuste = input(f"Digite o valor do reajuste:")

  salario = salario.replace(",",".")
  salario = float(salario)

  reajuste = reajuste.replace(",",".")
  reajuste = float(reajuste)

  novosal = (salario * (reajuste / 100)) + salario

  print("O novo salário é:", novosal)

def gorjeta():
  conta = input("Digite o valor da conta: ")
  conta = conta.replace(",",".")

  gor = float(conta) * 0.1

  print("O valor da gorjeta é:", gor)

def calc_imc():
  peso = input("insira o seu peso:")
  altura = input ("insira a sua altura:")

  peso = peso.replace(",",".")
  peso = float(peso)

  altura = altura.replace(",",".")
  altura = float(altura)

  imc = round(peso / altura ** 2, 2)
  print(f"O IMC é:{imc}")


def medponderada():
  p1 = input("Insira a primeira nota:")
  teste()
  p2 = input("Insira a segunda nota:")
  teste()
  p3 = input("Insira a terceira nota:")
  teste()

  p1 = p1.reajuste(",",".")
  p1 = float(p1)

  p2 = p2.reajuste(",",".")
  p2 = float(p2)

  p3 = p3.reajuste(",",".")
  p3 = float(p3)

  media = round((p1 * 1 + p2 * 2 + p3 * 3) / 6,3)
  teste()
  print(f"A média ponderada é {media}")

def notapnd2():
  nota1 = input(f"Digite a primeira nota:")
  nota2 = input(f"Digite a segunda nota:")

  nota1 = nota1.replace(",",".")
  nota1 = float(nota1)

  nota2 = nota2.replace(",",".")
  nota2 = float(nota2)

  media = (int(nota1) + (int(nota2) * 2)) / 3

  print("A média ponderada é:", media)

def posto ():
  valor = input(f"Digite o valor que deseja abastecer:")
  preco = input(f"Digite o preço do combustível:" )

  valor = valor.replace(",",".")
  valor = float(valor)

  preco = preco.replace(",",".")
  preco = float(preco)

  litros = round (valor / preco, 2)
  print("A quantidade de litros é: ", litros)

def teste():
  i = 0
  x = 10000
  while (x>i):
    print("/", end="\r", flush=True)
    print("", end="\r", flush=True)
    print("-", end="\r", flush=True)
    print("", end="\r", flush=True)
    print("|", end="\r", flush=True)
    print("", end="\r", flush=True)
    print("-", end="\r", flush=True)
    print("", end="\r", flush=True)
    print("\\", end="\r", flush=True)
    print("", end="\r", flush=True)
    i = i +1