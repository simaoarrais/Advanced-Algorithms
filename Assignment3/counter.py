from collections import Counter as collections_counter

import re

class Counter:

    def __init__(self, file_path, stopw_path):
        self.file_path = file_path
        self.stopw_path = stopw_path
        self.regex_words = re.compile(r"[a-zA-Z0-9À-ÿ’]+")
        self.regex_letters = re.compile(r"[a-zA-Z0-9À-ÿ]")
    
    def read(self, file):
        with open(file, 'r') as f:
            return f.read()
    
    def process(self, contents, stop_words):
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
    
    def start(self):
        # Read contents from file and stop-words
        contents = self.read(self.file_path)
        stop_words = self.read(self.stopw_path)

        # Process the contents
        letter_list = self.process(contents, stop_words)

        # Exact counter
        count_dict = self.exact_counter(letter_list)
        sorted_count_dict = count_dict.most_common()