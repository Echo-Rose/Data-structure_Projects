class HuffmanNode :
    def __init__(self, char = None, freq = 0, left = None, right = None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def heappush(heap, node) :
    heap.append(node)
    i = len(heap)-1
    while i > 1 and heap[i].freq < heap[i//2].freq :
        heap[i], heap[i//2] = heap[i//2], heap[i]
        i //= 2

def heappop(heap) :
    if len(heap) <= 1 :
        return None
    if len(heap) == 2:
        return heap.pop()
    root = heap[1]
    heap[1] = heap.pop()
    i = 1

    while True :
        smallest = i
        left = 2 * i
        right = left + 1
        if left < len(heap) and heap[left].freq < heap[smallest].freq:
            smallest = left
        if right < len(heap) and heap[right].freq < heap[smallest].freq:
            smallest = right
        if smallest == i :
            break
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
    return root

def build_huffman_tree(chars, freqs) :
    heap = [None]
    for char, freq in zip(chars, freqs) :
        heappush(heap, HuffmanNode(char, freq))
    while len(heap) > 2 :
        left = heappop(heap)
        right = heappop(heap)
        merged  = HuffmanNode(None, left.freq + right.freq, left, right)
        heappush(heap, merged)
    return heappop(heap)

def generate_codes(node, current_code="", codes={}):
    if node == None :
        return
    if node.char != None :
        codes[node.char] = current_code
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)
    return codes

def huffman_encode(text, codes) :
    encoded_text = ""
    for char in text :
        if char in codes :
            encoded_text += codes[char]
    return encoded_text

def calculate_compression_rate(original_text, encoded_text):
    original_bits = len(original_text) * 8 #아스키코드는 문자당 8비트
    encoded_bits = len(encoded_text)
    compression_rate = (1-encoded_bits/original_bits)*100
    return compression_rate

if __name__ == "__main__":
    chars = ['k','o','r','e','a','t','c','h']
    freqs = [10, 5, 2, 15, 18, 4, 7, 11]
    huffman_tree = build_huffman_tree(chars, freqs)
    huffman_codes = generate_codes(huffman_tree)
    print("허프만코드 문자 : ")
    for char, code in huffman_codes.items() :
        print(f"[{char} : {code}]")
    while True :
        text = input("Please a word : ")
        if all(char in huffman_codes for char in text):
            break
        print("illegal character")

    encoded_text = huffman_encode(text, huffman_codes)
    print("결과 비트 열 : ", encoded_text)

    compression_rate = calculate_compression_rate(text, encoded_text)
    print(f"압축률 : {compression_rate:.2f}%")
