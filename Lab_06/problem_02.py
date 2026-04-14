import heapq
import random
import string
from collections import Counter


def generate_random_text(length=200):
    chars = string.ascii_lowercase + " "
    return ''.join(random.choice(chars) for _ in range(length))



class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)

    heap = []
    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0], frequency


def generate_codes(node, current_code="", codes={}):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code
        return

    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)

    return codes



def calculate_bits(text, codes):
    total_bits = 0
    
    
    for char in text:
        total_bits += len(codes[char])
    
    code_size_bits = 0
    for char, code in codes.items():
        code_size_bits += (len(code) + 8)
    
    return total_bits + code_size_bits



random_text = generate_random_text(200)

print("Random Text:\n", random_text)
print("\nText Length:", len(random_text))


root, frequency = build_huffman_tree(random_text)


codes = generate_codes(root)

print("\nCharacter Frequencies:")
for char, freq in frequency.items():
    print(f"'{char}': {freq}")

print("\nHuffman Codes:")
for char, code in codes.items():
    print(f"'{char}': {code}")


huffman_bits = calculate_bits(random_text, codes)


fixed_bits = len(random_text) * 8

print("\nTotal Bits Required (Huffman Encoding):", huffman_bits)
print("Total Bits Required (Fixed 8-bit Encoding):", fixed_bits)
print("Bits Saved:", fixed_bits - huffman_bits)
