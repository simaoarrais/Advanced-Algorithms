from collections import Counter as collections_counter

import array
import random
import re

class Counter:

    def __init__(self, file_path, stopw_path, prob):
        self.file_path = file_path
        self.stopw_path = stopw_path
        self.prob = prob
        self.regex_words = re.compile(r"[a-zA-ZÀ-ÿ’]+")
        self.regex_letters = re.compile(r"[a-zA-ZÀ-ÿ]")
    
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

    def start(self):
        # Read contents from file and stop-words
        contents = self.read(self.file_path)
        stop_words = self.read(self.stopw_path)

        # Process the contents
        letter_list = self.process_data(contents, stop_words)
        # letter_list = ['T', 'H', 'E', 'P', 'R', 'E', 'F', 'A', 'C', 'E', 'T', 'H', 'E', 'A', 'R', 'T', 'I', 'S', 'T', 'C', 'R', 'E', 'A', 'T', 'O', 'R', 'B', 'E', 'A', 'U', 'T', 'I', 'F']

        # Exact counter
        count_dict = self.exact_counter(letter_list)
        sorted_count_dict = count_dict.most_common()

        # Approximate counter
        approx_dict = self.approximate_counter(letter_list, self.prob)
        # print(sorted_count_dict)
        # print(approx_dict)
