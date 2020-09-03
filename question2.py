def factorial(n):
  if n == 0: 
    return 1 
  else:
    return n*factorial(n-1)

def main():

    print("Questão 2: Implemente uma função ou trecho de código que calcule o fatorial de um número inteiro de forma recursiva.\n")

    n = int(input("Digite um número inteiro: "))

    nFactorial = factorial(n)

    print("\nO fatorial de ", n, " é ", nFactorial, "\n")

if __name__ == "__main__":
    main()