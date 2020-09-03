def avg(numbers):
    return float(sum(numbers))/len(numbers)

def main():
    
    floatNumbers = [1.5, 2.7, 5.8, 8.1, 12.54, 20.05]

    print("Questão 1: Implemente uma função ou trecho de código que calcule a média de um vetor de números reais.\n")

    vectorAvg = avg(floatNumbers)

    print("Vetor a ser calculada a média: ", floatNumbers, "\n")
    print("Média calculada: %.2f" % vectorAvg)

if __name__ == "__main__":
    main()
