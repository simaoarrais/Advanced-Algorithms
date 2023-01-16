import json
import matplotlib.pyplot as plt
import os

def read_file(file):
    with open(file, 'r') as f:
        return f.read()

def start_plot(folder_path):
    # Read files
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            if not len(file.split("-")) > 1:
                pass
                language = file.split(".")[0]

                # Get content
                contents = read_file(file_path)
                json_contents = json.loads(contents)

                # Get counters
                exact_counter = json_contents['Exact']
                approximate_counter = json_contents['Approximate']
                error_counter = json_contents['Error']

                # Exact Counter
                for counter in exact_counter:
                    plt.bar(counter[0], counter[1], color="blue")
                plt.title(f'Exact counter for {language.upper()} book')
                plt.xlabel("Letter")
                plt.ylabel("Count")
                plt.savefig(f'plots/{language}-Exact.png')
                plt.clf()

                # Approximate Counter
                for counter in approximate_counter:
                    plt.bar(counter[0], counter[1], color="green")
                plt.title(f'Approximate counter for {language.upper()} book')
                plt.xlabel("Letter")
                plt.ylabel("Count")
                plt.savefig(f'plots/{language}-Approximate.png')
                plt.clf()

                # Absolute Error Counter
                for counter in error_counter:
                    plt.bar(counter[0], counter[1][5], color="red")
                plt.title(f'Average Absolute Error for {language.upper()} book')
                plt.xlabel("Letter")
                plt.ylabel("Error")
                plt.savefig(f'plots/{language}-AbsoluteError.png')
                plt.clf()

                # Relative Error Counter
                new_sort = sorted(error_counter, key=lambda x: x[1][2], reverse=True)
                for counter in new_sort:
                    plt.bar(counter[0], counter[1][2], color="red")
                plt.title(f'Average Relative Error for {language.upper()} book')
                plt.xlabel("Letter")
                plt.ylabel("Error")
                # plt.savefig(f'plots/ExactCounter-{k}-{language}.png')
                plt.savefig(f'plots/{language}-RelativeError.png')
                plt.clf()

                # Print min and max of relative and absolute errors
                print(f'{language}:')
                # Min Relative Error
                new_sort = sorted(error_counter, key=lambda x: x[1][0])[0]
                print(f'Min Relative Error: {new_sort[1][0]} -> {new_sort[0]}')
                # Max Relative Error
                new_sort = sorted(error_counter, key=lambda x: x[1][1])[0]
                print(f'Max Relative Error: {new_sort[1][1]} -> {new_sort[0]}')
                # Min Relative Error
                new_sort = sorted(error_counter, key=lambda x: x[1][3])[0]
                print(f'Min Absolute Error: {new_sort[1][3]} -> {new_sort[0]}')
                # Max Relative Error
                new_sort = sorted(error_counter, key=lambda x: x[1][4])[0]
                print(f'Max Absolute Error: {new_sort[1][4]} -> {new_sort[0]}')

                # Print average of relative and absolute errors
                avg_relative_sum = 0
                avg_absolute_sum = 0
                for letter_info in error_counter:
                    avg_relative_sum += letter_info[1][2]
                    avg_absolute_sum += letter_info[1][5]
                print(f'Average Relative Error: {avg_relative_sum/len(error_counter)}')
                print(f'Max Absolute Error: {avg_absolute_sum/len(error_counter)}')

                print("\n")
                

            else:
                k, txt = file.split("-")
                language = txt.split(".")[0]

                # Get content
                contents = read_file(file_path)
                json_contents = json.loads(contents)

                # Get counters
                for k in json_contents:
                    frequent_count = json_contents[k]

                    # Frequent Counter
                    for counter in frequent_count:
                        plt.bar(counter[0], counter[1], color="orange")
                    plt.title(f'Exact counter for {language.upper()} book')
                    plt.xlabel("Letter")
                    plt.ylabel("Count")
                    plt.savefig(f'plots/{language}-Frequent-{k}.png')
                    plt.clf()


if __name__ == "__main__":
    start_plot("results")
