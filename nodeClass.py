class node: 
    """
    Classe que representa um nó na árvore de Huffman
    
    Atributos:
        word (str): palavra que o nó representa
        freq (int): frequência da palavra na frase
        left (node): filho esquerdo do nó
        right (node): filho direito do nó
    """

    def __init__(self, word, freq):
        # Construtor da classe

        self.word = word
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        """
        Método que compara a frequeência entre 2 nós

        Retorno:
            bool: "True" se a frequência do atual for menor que a do outro, "False" caso contrário
        """
        return self.freq < other.freq
