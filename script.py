import os
import re
from collections import Counter
import socket


def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            words = re.findall(r'\b\w+\b', text)  # Extract words
        return words
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return []


def get_ip_address():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


if1_file = '/home/data/IF-1.txt'
always_file = '/home/data/AlwaysRememberUsThisWay-1.txt'
output_dir = '/home/data/output'
output_file = os.path.join(output_dir, 'result.txt')


os.makedirs(output_dir, exist_ok=True)


if1_words = read_file(if1_file)
always_words = read_file(always_file)


if1_word_count = len(if1_words)
always_word_count = len(always_words)


grand_total = if1_word_count + always_word_count


if1_word_freq = Counter(if1_words).most_common(3)


always_word_freq = Counter(always_words).most_common(3)

ip_address = get_ip_address()


with open(output_file, 'w', encoding='utf-8') as f:
    f.write("=== Project 3: Docker Text Analysis Results ===\n\n")
    f.write(f"1. Word Counts:\n   - IF-1.txt: {if1_word_count} words\n   - AlwaysRememberUsThisWay-1.txt: {always_word_count} words\n   - Grand Total: {grand_total} words\n\n")
    f.write("2. Top 3 Words in IF-1.txt:\n")
    for word, count in if1_word_freq:
        f.write(f"   - '{word}': {count} times\n")
    f.write("\n3. Top 3 Words in AlwaysRememberUsThisWay-1.txt:\n")
    for word, count in always_word_freq:
        f.write(f"   - '{word}': {count} times\n")
    f.write(f"\n4. Machine Details:\n   - IP Address: {ip_address}\n")


with open(output_file, 'r', encoding='utf-8') as f:
    print(f.read())
