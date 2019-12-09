from codes_ex import *
import sys

i = 0
while 1>i :
  
  print ("Escolha uma opção: ")
  print("\t")
  print("Opçao 1 - média de 3 notas")
  print("Opçao 2 - média ponderada")
  print("Opçao 3 - IMC - Índice de Massa Corporal")
  print("Opçao 4 - converter graus celsus em fahrenheit")
  print("Opçao 5 - abastecer o carro")
  print("Opçao 6 - média com peso 2")
  print("Opçao 7 - valor da gorjeta")
  print("Opçao 8 - reajuste salarial")
  print("Opçao 9 - área do quadrado")
  print("Opçao 10 - área do retângulo")
  print("Opçao 11 - área do círculo")
  print("Opçao 12 - área da esfera")
  print("Opçao 13 - volume da cixa d'água")
  print("Opçao 14 - SAIR")
  
  opcao = input(f"Digite aqui: ")
  #teste()

  if opcao.isdigit() == False:
    opcao = 15

  opcao = int(opcao)
  if opcao <= 14: 
    if opcao == 14:
      i=2
      print("Inté!")
    if opcao == 1:
      media_notas()
      print("\t")
      sleep(5)
      clear()
    if opcao == 2:
      medponderada()
      print("\t")
      sleep(5)
      clear()
    if opcao == 3:
      calc_imc()
      print("\t")
      sleep(5)
      clear()
    if opcao == 4:
      conv_celsus()
      print("\t")
      sleep(5)
      clear()
    if opcao == 5:
      posto ()
      print("\t")
      sleep(5)
      clear()
    if opcao == 6:
      notapnd2()
      print("\t")
      sleep(5)
      clear()
    if opcao == 7:
      gorjeta()
      print("\t")
      sleep(5)
      clear()
    if opcao == 8:
      aumento_sal()
      print("\t")
      sleep(5)
      clear()
    if opcao == 9:
      area_quadrado()
      print("\t")
      sleep(5)
      clear()
    if opcao == 10:
      area_retangulo()
      print("\t")
      sleep(5)
      clear()
    if opcao == 11:
      area_circulo()
      print("\t")
      sleep(5)
      clear()
    if opcao == 12:
      area_esfera()
      print("\t")
      sleep(5)
      clear()
    if opcao == 13:
      volume_caixa()
      print("\t")
      sleep(5)
      clear()
  else:
    print("  ")
    print("***Comando inválido. Digite valores de 1 a 13 ou 14 para sair***")
    teste()
    sleep(5)
    clear()