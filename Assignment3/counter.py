from collections import Counter as collections_counter
from collections import defaultdict

import json
import random
import re
import os

class Counter:

    def __init__(self, file_path, stopw_path, prob, k_list, results_file):
        self.file_path = file_path
        self.stopw_path = stopw_path
        self.prob = prob
        self.k_list = k_list
        self.results_file = results_file
        self.regex_words = re.compile(r"[a-zA-ZÀ-ÿ’]+")
        self.regex_letters = re.compile(r"[a-zA-ZÀ-ÿ]")
        self.regex_numbers = re.compile(r"[0-9]+")
    
    def read(self, file):
        with open(file, 'r') as f:
            return f.read()
    
    def write(self, file, string):
        folder_name = "results"

        # Check if folder results exists
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)  

        with open(f'{folder_name}/{file}.txt', 'a') as f:
            f.write(string)
    
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
        freq_counter = collections_counter()

        for letter in contents:
            if random.random() <= prob:
                if letter in freq_counter:
                    freq_counter[letter] += 1
                else: 
                    freq_counter[letter] = 1

        for letter in freq_counter:
            freq_counter[letter] /= prob

        return freq_counter

    def misra_gries_counter(self, stream, k):
        # Initialization
        A = collections_counter()

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

        return A
    
    def average_approximation(self, exact_count, contents, iterations):
        avg_approx_counter = collections_counter()
        avg_error_counter = dict() # {Letter: [min_relative_error, max_relative_error, avg_relative_error, min_absolute_error, max_absolute_error, avg_absolute_error]}

        for i in range(iterations):
            approx_dict = self.approximate_counter(contents, self.prob)

            # Check for errors
            for k,v in approx_dict.items():

                # Build final average counter
                if k not in avg_approx_counter:
                    avg_approx_counter[k] = v
                else:
                    avg_approx_counter[k] += v

                # Calculate errors
                approx_value = approx_dict[k]
                exact_value = exact_count[k]
                relative_error = (approx_value - exact_value)/exact_value
                absolute_error = approx_value - exact_value

                if not relative_error >= 1:
                    if k not in avg_error_counter:
                        avg_error_counter[k] = [relative_error, relative_error, abs(relative_error), absolute_error, absolute_error, abs(absolute_error)]
                    else:
                        # avg_error_counter = {Letter: [min_relative_error, max_relative_error, avg_relative_error, min_absolute_error, max_absolute_error, avg_absolute_error]}
                        letter_info = avg_error_counter[k]

                        # Relative errors
                        if relative_error < letter_info[0]:
                            letter_info[0] = relative_error
                        elif relative_error > letter_info[1]:
                            letter_info[1] = relative_error
                        letter_info[2] += abs(relative_error)
                    
                        # Absolute errors
                        if absolute_error < letter_info[3]:
                            letter_info[3] = absolute_error
                        elif absolute_error > letter_info[4]:
                            letter_info[4] = absolute_error
                        letter_info[5] += abs(absolute_error)
            
        # Get an average for the final dictionary
        for k,v in approx_dict.items():
            avg_approx_counter[k] = round(avg_approx_counter[k] / iterations)
        
        for k,v in avg_error_counter.items():
            avg_error_counter[k][2] /= iterations
            avg_error_counter[k][5] /= iterations
        
        return avg_approx_counter, avg_error_counter

    def start(self):
        # Read contents from file and stop-words
        contents = self.read(self.file_path)
        stop_words = self.read(self.stopw_path)

        # Process the contents
        letter_list = self.process_data(contents, stop_words)

        # Exact counter
        freq_count = self.exact_counter(letter_list)
        sorted_count_dict = freq_count.most_common()

        # Approximate counter
        avg_approx_dict, error_dict = self.average_approximation(freq_count, letter_list, 10)
        sorted_approx_dict = avg_approx_dict.most_common()
        sorted_error_dict = sorted(error_dict.items(), key=lambda x: x[1][5], reverse=True)

        # Save results
        result = {"Exact": sorted_count_dict, "Approximate": sorted_approx_dict, "Error": sorted_error_dict}
        self.write(self.results_file, json.dumps(result))

        # Misra & Gries
        result = {}
        for k in self.k_list:
            data_count = self.misra_gries_counter(letter_list, k)
            sorted_misra_gries = data_count.most_common()
            result[k] = sorted_misra_gries
        self.write(f'{self.results_file}-fequent', json.dumps(result))
            