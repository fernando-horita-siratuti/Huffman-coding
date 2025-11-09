import os
from huffmanClass import huffman

# Obtém o caminho absoluto do arquivo de entrada combinando o diretório atual com 'data/input.dat'
fileName = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "input.dat")

# Cria uma nova instância da classe huffman 
h = huffman()          

# Constrói o mapa de frequência das palavras a partir do arquivo de entrada
h.buildWordMap(fileName)