from collections import Counter as collections_counter
from collections import defaultdict

import random
import re

class Counter:

    def __init__(self, file_path, stopw_path, prob, data_file):
        self.file_path = file_path
        self.stopw_path = stopw_path
        self.prob = prob
        self.data_file = data_file
        self.regex_words = re.compile(r"[a-zA-ZÀ-ÿ’]+")
        self.regex_letters = re.compile(r"[a-zA-ZÀ-ÿ]")
        self.regex_numbers = re.compile(r"[0-9]+")
    
    def read(self, file):
        with open(file, 'r') as f:
            return f.read()
    
    def process_data(self, contents, stop_words):
        # Get all words and filter through stop-words
        pre_words = self.regex_words.findall(contents)
        words = [w for w in pre_words if not w in stop_words]

        # Get all letters
        letters_list = []
        for w in words:
            letters = self.regex_letters.findall(w)
            letters_list.extend(letters)

        # Apply upper case
        upper_letters = [lettter.upper() for lettter in letters_list]
        return upper_letters

    def apply_regex(self, contents, regex):
        return regex.findall(contents)

    def exact_counter(self, contents):
        freq = collections_counter(contents)
        return freq
    
    def approximate_counter(self, contents, prob = 1/16):
        freq_counter = dict()

        for letter in contents:
            if random.random() <= prob:
                if letter in freq_counter:
                    freq_counter[letter] += 1
                else: 
                    freq_counter[letter] = 1
        
        return freq_counter

    def misra_gries_counter(self, stream, k):
        # Initialization
        A = dict()

        # Processing
        for j in stream:
            if j in A:
                A[j] += 1
            elif len(A) < k - 1:
                A[j] = 1
            else:
                for i in list(A.keys()):
                    A[i] -= 1
                    if A[i] == 0:
                        del A[i]

        # Output
        top_k = sorted(A.items(), key=lambda x: x[1], reverse=True)
        return top_k

    def start(self):
        # Read contents from file and stop-words
        contents = self.read(self.file_path)
        stop_words = self.read(self.stopw_path)

        # Process the contents
        letter_list = self.process_data(contents, stop_words)
        # letter_list = ['T', 'H', 'E', 'P', 'R', 'E', 'F', 'A', 'C', 'E', 'T', 'H', 'E', 'A', 'R', 'T', 'I', 'S', 'T', 'C', 'R', 'E', 'A', 'T', 'O', 'R', 'B', 'E', 'A', 'U', 'T', 'I', 'F']

        # Exact counter
        freq_count = self.exact_counter(letter_list)
        sorted_count_dict = freq_count.most_common()

        # Approximate counter
        approx_dict = self.approximate_counter(letter_list, self.prob)

        # Misra & Gries
        data_stream = self.read(self.data_file)
        data_stream = self.apply_regex(data_stream, self.regex_numbers)
        k = 3
        print(self.exact_counter(letter_list).most_common()[:k])
        print("\n\n\n\n\n\n\n\n")
        data_count = self.misra_gries_counter(letter_list, k)
        print(data_count)
