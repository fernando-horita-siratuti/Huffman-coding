import os
from huffmanClass import huffman

fileName = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "input.dat")
h = huffman()          

h.buildWordMap(fileName)