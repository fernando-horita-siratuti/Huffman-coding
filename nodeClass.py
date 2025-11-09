class node: 
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq