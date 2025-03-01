import os
import re
from collections import Counter
import socket

# Function to read and process text files
def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # Convert to lowercase for consistency
        # Split contractions and remove punctuation
        words = re.findall(r'\b\w+\b', text)
    return words

# Function to get the IP address of the machine
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Paths to the input files and output directory
if1_file = '/home/data/IF-1.txt'
always_file = '/home/data/AlwaysRememberUsThisWay-1.txt'
output_dir = '/home/data/output'
output_file = os.path.join(output_dir, 'result.txt')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Read and process both files
if1_words = read_file(if1_file)
always_words = read_file(always_file)

# a. Count total words in each file
if1_word_count = len(if1_words)
always_word_count = len(always_words)

# b. Calculate grand total of words
grand_total = if1_word_count + always_word_count

# c. Top 3 most frequent words in IF-1.txt
if1_word_freq = Counter(if1_words).most_common(3)

# d. Top 3 most frequent words in AlwaysRememberUsThisWay-1.txt (contractions split)
always_word_freq = Counter(always_words).most_common(3)

# e. Get IP address
ip_address = get_ip_address()

# f. Write detailed and concise results to output file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("=== Project 3: Docker Text Analysis Results ===\n\n")
    
    f.write("1. Word Counts:\n")
    f.write(f"   - IF-1.txt: {if1_word_count} words\n")
    f.write(f"   - AlwaysRememberUsThisWay-1.txt: {always_word_count} words\n")
    f.write(f"   - Grand Total: {grand_total} words\n\n")
    
    f.write("2. Top 3 Words in IF-1.txt:\n")
    for word, count in if1_word_freq:
        f.write(f"   - '{word}': {count} times\n")
    f.write("\n")
    
    f.write("3. Top 3 Words in AlwaysRememberUsThisWay-1.txt (contractions split):\n")
    for word, count in always_word_freq:
        f.write(f"   - '{word}': {count} times\n")
    f.write("\n")
    
    f.write("4. Machine Details:\n")
    f.write(f"   - IP Address: {ip_address}\n")

# Print the contents of result.txt to the console
with open(output_file, 'r', encoding='utf-8') as f:
    print(f.read())