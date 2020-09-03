class NodeList:
    
    # Em python, None representa o valor de NULL
    def __init__(self, data=0, nextNode=None):
        self.data = data
        self.next = nextNode

class LinkedList:
   
    def __init__(self):
        self.head = None

# Implementei a função de inserir somente para haver valores a serem removidos
def insertOnBeginning(linkedList, data):

    new_node = NodeList(data)

    new_node.next = linkedList.head

    linkedList.head = new_node

def remove(self, value):

    if self.head == None:
        print("Lista vazia!")
    else:

        if self.head.data == value:
            self.head = self.head.next
        else:
            previous = None
            actual = self.head
            while actual and actual.data != value:
                previous = actual
                actual = actual.next

            if actual:
                previous.next = actual.next
            else:
                previous.next = None

def printLinkedList(linkedList):

    node = linkedList.head

    print("[", end = '')
    while node:
        print(node.data, " -> ", end = '')
        node = node.next

    print("None]\n")

def main():

    print("Questão 3: Implemente uma classe ou trecho de código que represente uma lista encadeada e ordenada de inteiros de forma crescente.")
    print("Implemente apenas o método que faz a remoção de um elemento da lista.\n")

    linkedList = LinkedList()

    for i in range(10):
        insertOnBeginning(linkedList, i)

    printLinkedList(linkedList)

    valueToRemove = int(input("Digite o valor a ser removido: "))

    print("\nRemovendo elemento: ", valueToRemove)

    remove(linkedList, valueToRemove)

    printLinkedList(linkedList)

if __name__ == "__main__":
    main()