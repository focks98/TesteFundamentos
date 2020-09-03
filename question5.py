def multMatrix(matrixA, matrixB):
    
    matrixResult = []

    for i in range(len(matrixA)): 
        vectorAux = []                                                                     
        for j in range(len(matrixB[0])):
            sumAux = 0 
            for k in range(len(matrixB)):
                sumAux += matrixA[i][k] * matrixB[k][j]

            vectorAux.append(sumAux)
        
        matrixResult.append(vectorAux)

    return matrixResult

def main():

    matrixA =[[3, 5, 1],
              [1, 7, 2]]

    matrixB =[[1, 3],
              [2, 4],
              [1, 1]]
    

    print("Questão 4: Implemente uma função que receba duas matrizes de inteiros e efetue sua multiplicação.\n")

    matrixResult = multMatrix(matrixA, matrixB)

    print("MatrixA: ")
    for row in matrixA:
        print(row)

    print("\nMatrixB: ")
    for row in matrixB:
        print(row)
    
    print("\nResult: ")
    for row in matrixResult:
        print(row)

if __name__ == "__main__":
    main()