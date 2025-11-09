# Huffman Coding — Python Implementation

![Python](https://img.shields.io/badge/python-3.8%2B-blue)

**Description**  

Individual project of AEDS 2 about the **Huffman Coding** algorithm in Python.  
Compresses data by building a Huffman tree and generating prefix-free binary codes based on word frequencies.  
Designed for learning, experiments, and small demonstrations.

---

## Table of Contents
- [Highlights](#highlights)  
- [Requirements](#requirements)  
- [Quickstart](#quickstart)  
- [Repository Structure](#repository-structure)  
- [How It Works (Technical Summary)](#how-it-works-technical-summary) 
- [Contact](#contact)

---

## Highlights
- Implemented in **Python**, organized into clean classes (`nodeClass.py`, `huffmanClass.py`) and an execution script (`main.py`).
- Focused on **clarity and readability** — perfect for students learning data compression.
- Optional example inputs/outputs in the `data/` directory (if present).

---

## Requirements
- Python 3.8+  
- No external dependencies required (uses only the standard library).  

> If you add dependencies in the future, include them in a `requirements.txt` file and install with:  
> `pip install -r requirements.txt`

---

## Quickstart

```bash
# clone the repository
git clone https://github.com/fernando-horita-siratuti/Huffman-coding.git
python3 main.py
```
---

## Repository Structure

```bash
Huffman-coding/
├─ data/                 
│  ├─ input.dat          # input file with the sentences to be compressed
│  ├─ output.dat         # example output (compressed result)
│
├─ huffmanClass.py       # main Huffman algorithm implementation
├─ nodeClass.py          # Huffman tree node structure
├─ main.py               
└─ README.md             
```

---

## How It Works (Technical Summary)

- Counts word frequencies in the input.
- Creates leaf nodes for each word, weighted by frequency.
- Builds the Huffman tree by repeatedly combining the two least frequent nodes into a new parent node.
- Generates binary codes (0/1) along root→leaf paths — guaranteeing prefix-free codes.

---

## Example test

### Input:

```bash
O computador executa instruções em alta velocidade. O computador processa dados com precisão.

A memória armazena informações. Essas informações são acessadas pela CPU.

Os sistemas operacionais controlam recursos. Esses sistemas executam tarefas.
```

### Output:

```bash
----- 1ª frase -----

O: 100
computador: 110
executa: 0110
instruções: 1010
em: 1011
alta: 0111
velocidade: 000
processa: 010
dados: 1111
com: 1110
precisão: 001

Frase comprimida: 100110011010101011011100001011111110001

----- 2ª frase -----

A: 1100
memória: 1111
armazena: 1101
informações: 01
Essas: 000
são: 1110
acessadas: 100
pela: 001
CPU: 101

Frase comprimida: 110011111101010001110100001101

----- 3ª frase -----

Os: 010
sistemas: 111
operacionais: 011
controlam: 000
recursos: 001
Esses: 101
executam: 100
tarefas: 110

Frase comprimida: 010111011000001101100110
```

---

