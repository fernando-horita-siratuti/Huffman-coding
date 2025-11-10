from nodeClass import node
import heapq
import os

class huffman:
    def __init__(self):
        # Heap que armazena os nós da árvore
        self.heap = []
        # Dicionário que armazena os códigos Huffman
        self.codes = {}
        # Contador para a quantidade de frases
        self.cont = 0
        # Dicionário que armazena a quantidade de ocorrências de cada palavra
        self.wordMap = {}
        
    def buildWordMap(self, fileName):
        # Tenta abrir o arquivo e criar o mapa de palavras
        try:
            with open(fileName, 'r') as file:
                for line in file:
                    # Ignora as linhas em branco
                    if not line.strip():
                        continue
                    # Limpa o mapa de palavras, os códigos para cada frase e o heap dos nós
                    self.wordMap.clear()
                    self.codes.clear()
                    self.heap.clear()
                    words = line.split()
                    for word in words:
                        # Ignora as palavras que não são alfabéticas
                        if not word.isalpha():
                            word = word[:-1]
                        # Checa se a palavra já existe no map e incrementa a quantidade de ocorrências da palavra
                        if word in self.wordMap:
                            self.wordMap[word] += 1
                        else:
                            self.wordMap[word] = 1
                    # Chama a função que cria o heap com as palavras e suas ocorrências
                    self.buildHeap(self.wordMap)
                    # Escreve o resultado no arquivo de saída
                    fileName = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "output.dat")
                    self.writeOnOutput(fileName)
        except IOError:
            print("An error occurred reading the file.")
        
    def buildHeap(self, wordMap):
        # Cria o heap com as palavras e suas ocorrências
        for word in wordMap.items():
            newNode = node(word[0], word[1])
            heapq.heappush(self.heap, newNode)

        # Chama a função que faz o merge dos nós da árvore
        self.mergeNodes()

    def mergeNodes(self):
        # Enquanto houver mais de um nó, a função faz o merge dos dois menores
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

        # Chama a função que obtem o nó raiz da árvore
        self.getRoot()

    def getRoot(self):
        # Obtem o nó raiz da árvore
        rootItem = self.heap[0]

        # Chama a função que gera os códigos Huffman da árvore
        self.generateCode(rootItem, prefix="", codes=self.codes)
    
    def generateCode(self, node, prefix="", codes=None):
        if node.word is not None:
            self.codes[node.word] = prefix or "0"
        else:
            # Chamada recursiva que percorre esquerda adicionando '0'
            self.generateCode(node.left, prefix + "0", self.codes)
            # Chamada recursiva que percorre direita adicionando '1'
            self.generateCode(node.right, prefix + "1", self.codes)

    def writeOnOutput(self, fileName):
        # Tenta abrir o arquivo e escrever o resultado final das frases
        try:
            with open(fileName, 'a') as file:
                self.cont += 1
                compressedSentence = []
                file.write(f'----- {self.cont}ª frase -----\n\n')
                for wordMap in self.wordMap:
                    for wordCodes, code in self.codes.items():
                        if wordMap == wordCodes: 
                            file.write(f'{wordCodes}: {code}\n')
                            compressedSentence.append(code)
                file.write('\nFrase comprimida: ')
                for code in compressedSentence: 
                    file.write(f'{code}')
                file.write('\n\n')
        except IOError:
            print("An error occurred writing on the file.")
