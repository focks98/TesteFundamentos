def mode(numbers):
    
    maxRepetition = 0

    for i in numbers:                                                                       
        nRepetition = numbers.count(i)                                                             
        if nRepetition > maxRepetition:    
            mode = []                                                   
            maxRepetition = nRepetition
        elif nRepetition == maxRepetition and i not in mode:
            mode.append(i)

    return mode

def main():

    integerNumbers =[5, 20, 2, 5, 4, 3, 25, 32,
                     3, 9, 14, 2, 4, 3, 23, 0,
                     2, 1, 6, 8, 11, 15, 95, 3]

    print("Questão 4: Implemente uma função ou trecho de código que calcule a moda das idades dos alunos de uma turma de colégio.\n")

    modeVector = mode(integerNumbers)
    
    print("\n A moda do vetor: ", integerNumbers," é ", modeVector, "\n")

if __name__ == "__main__":
    main()