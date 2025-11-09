from nodeClass import node
import heapq
import os

class huffman:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.cont = 0
        self.wordMap = {}
        
    def buildWordMap(self, fileName):
        try:
            with open(fileName, 'r') as file:
                for line in file:
                    if not line.strip():
                        continue
                    self.wordMap.clear()
                    self.codes.clear()
                    self.heap.clear()
                    words = line.split()
                    for word in words:
                        if not word.isalpha():
                            word = word[:-1]
                        if word in self.wordMap:
                            self.wordMap[word] += 1
                        else:
                            self.wordMap[word] = 1
                    self.buildHeap(self.wordMap)
                    fileName = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "output.dat")
                    self.writeOnOutput(fileName)
        except IOError:
            print("An error occurred reading the file.")
        
    def buildHeap(self, wordMap):
        for word in wordMap.items():
            newNode = node(word[0], word[1])
            heapq.heappush(self.heap, newNode)

        self.mergeNodes()

    def mergeNodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

        self.getRoot()

    def getRoot(self):
        rootItem = self.heap[0]

        self.generateCode(rootItem, prefix="", codes=self.codes)
    
    def generateCode(self, node, prefix="", codes=None):
        # nó folha: tem símbolo
        if node is None:
            return self.codes
        if node.word is not None:
            # caso especial: árvore com apenas 1 nó -> atribuir "0" ou "1"
            self.codes[node.word] = prefix or "0"
        else:
            # percorre esquerda adicionando '0'
            self.generateCode(node.left, prefix + "0", self.codes)
            # percorre direita adicionando '1'
            self.generateCode(node.right, prefix + "1", self.codes)

    def writeOnOutput(self, fileName):
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