def calculador (num1, num2 , operacao):
  if (operacao == 1):
    return num1 + num2
  
  if (operacao == 2):
    return num1 - num2

  if (operacao == 3):
    return num1 * num2

  if (operacao == 4):
   return num1 / num2

  else:
    return 0
         
while True:
  print("Escolha a operação:")
  print("1: Soma")
  print("2: Subtração")
  print("3: Multiplicação")
  print("4: Divisão")
  print("0: Sair") 
   
  opcao = input("Digite o número para a operação correspondente: ")  
  if opcao == "0":
    print("Saindo da calculadora.")
    break         
  elif opcao not in ["1", "2", "3", "4"]:
    print("Essa opção não existe.")
    continue               
 
  num1 = float(input("Digite o primeiro valor: "))
  num2 = float(input("Digite o segundo valor: "))

  if opcao == "1":
    resultado =  (num1+num2)
    print(f"Resultado da soma: {resultado}")
  elif opcao == "2":
    resultado = (num1 - num2)
    print(f"Resultado da subtração: {resultado}")
  elif opcao == "3":
    resultado = (num1 * num2)
    print(f"Resultado da multiplicação: {resultado}")
  elif opcao == "4":
    resultado = (num1 / num2)
    print(f"Resultado da divisão: {resultado}")   
  elif opcao == "0":
    resultado == "sair " 
    print (f"Sair da calculadora")
   
               



