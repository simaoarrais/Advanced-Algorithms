import matplotlib.pyplot as plt

def get_results(probs):
    results = {} # {probability : ( [Vertices], [Graph Creation Time], [Solution Time] ) }
    for p in probs:

        file_path = "results/solution_0" + str(p) + ".txt"
        vertices = []
        graph_creation_time = []
        solution_time = []
        basic_operations = []
        best_lens = []
        generated_solutions = []
        tested_candidates = []
        best_lens = []

        with open(file_path, "r") as file:
            # Read the contents of the file
            contents = file.read()

            # Split the contents into lines
            lines = contents.split("\n")

            # Loop over the lines in the file
            for line in lines:
                # Split the line into a list of values
                values = line.split()

                # Print the values
                if values:
                    if (values[0] == "vertices"):
                        vertices.append(values[2])
                    elif (values[0] == "graph"):
                        graph_creation_time.append(values[2])
                    elif (values[0] == "solution"):
                        solution_time.append(values[2])
                    elif (values[0] == "basic_operations:"):
                        basic_operations.append(values[1])
                    elif (values[0] == "best_len:"):
                        best_lens.append(values[1])
                    elif (values[0] == "generated_solutions:"):
                        generated_solutions.append(values[1])
                    elif (values[0] == "tested_candidates:"):
                        tested_candidates.append(values[1])
        results[p] = (vertices, graph_creation_time, solution_time, basic_operations, best_lens, generated_solutions, tested_candidates)
    return results

def plot_results_solution_time(results):
    max_solution_time = 0

    for elem in results:
        vertices = results[elem][0]
        graph_creation_time = results[elem][1]
        solution_time_list = results[elem][2]
        
        if elem == 125:
            plt.plot([int(v) for v in vertices], [float(v) for v in solution_time_list], "-o", color="green", label="12,5%")
        if elem == 25:
            plt.plot([int(v) for v in vertices], [float(v) for v in solution_time_list], "-o", color="blue", label="25%")
        if elem == 5:
            plt.plot([int(v) for v in vertices], [float(v) for v in solution_time_list], "-o", color="orange", label="5%")
        if elem == 75:
            plt.plot([int(v) for v in vertices], [float(v) for v in solution_time_list], "-o", color="red", label="75%")

        elem_max_time = max([float(v) for v in solution_time_list])
        if max_solution_time < elem_max_time:
            max_solution_time = elem_max_time

    plt.xlabel("Vertices")
    plt.ylabel("Time")
    plt.ylim([0, max_solution_time])
    plt.legend(loc="upper left")
    plt.show()

def plot_results_basic_operations(results):
    max_basic_operations = 0

    for elem in results:
        vertices = results[elem][0]
        basic_operations = results[elem][3]
        
        if elem == 125:
            plt.plot([int(v) for v in vertices], [int(v) for v in basic_operations], "-o", color="green", label="12,5%")
        if elem == 25:
            plt.plot([int(v) for v in vertices], [int(v) for v in basic_operations], "-o", color="blue", label="25%")
        if elem == 5:
            plt.plot([int(v) for v in vertices], [int(v) for v in basic_operations], "-o", color="orange", label="5%")
        if elem == 75:
            plt.plot([int(v) for v in vertices], [int(v) for v in basic_operations], "-o", color="red", label="75%")

        elem_max_operation = max([float(v) for v in basic_operations])
        if max_basic_operations < elem_max_operation:
            max_basic_operations = elem_max_operation
    # print([int(v) for v in basic_operations])
    plt.xlabel("Vertices")
    plt.ylabel("Basic Operations")
    plt.ylim([0, max_basic_operations])
    plt.legend(loc="upper left")
    plt.show()

def plot_results_best_solution(results):
    max_best_solution = 0

    for elem in results:
        vertices = results[elem][0]
        best_solutions = results[elem][4]
        
        if elem == 125:
            plt.plot([int(v) for v in vertices], [int(v) for v in best_solutions], "-o", color="green", label="12,5%")
        if elem == 25:
            plt.plot([int(v) for v in vertices], [int(v) for v in best_solutions], "-o", color="blue", label="25%")
        if elem == 5:
            plt.plot([int(v) for v in vertices], [int(v) for v in best_solutions], "-o", color="orange", label="5%")
        if elem == 75:
            plt.plot([int(v) for v in vertices], [int(v) for v in best_solutions], "-o", color="red", label="75%")

        new_max_best_solution = max([float(v) for v in best_solutions])
        if max_best_solution < new_max_best_solution:
            max_best_solution = new_max_best_solution
    # print([int(v) for v in basic_operations])
    plt.xlabel("Vertices")
    plt.ylabel("Number of Solutions")
    plt.ylim([0, max_best_solution])
    plt.legend(loc="upper left")
    plt.show()

def plot_results_generated_sets(results):
    max_generated_sets = 0

    for elem in results:
        vertices = results[elem][0]
        generated_sets = results[elem][5]
        
        if elem == 125:
            plt.plot([int(v) for v in vertices], [int(v) for v in generated_sets], "-o", color="green", label="12,5%")
        if elem == 25:
            plt.plot([int(v) for v in vertices], [int(v) for v in generated_sets], "-o", color="blue", label="25%")
        if elem == 5:
            plt.plot([int(v) for v in vertices], [int(v) for v in generated_sets], "-o", color="orange", label="5%")
        if elem == 75:
            plt.plot([int(v) for v in vertices], [int(v) for v in generated_sets], "-o", color="red", label="75%")

        elem_max_generated_sets = max([float(v) for v in generated_sets])
        if max_generated_sets < elem_max_generated_sets:
            max_generated_sets = elem_max_generated_sets
    # print([int(v) for v in basic_operations])
    plt.xlabel("Vertices")
    plt.ylabel("Generated Sets")
    plt.ylim([0, max_generated_sets])
    plt.legend(loc="upper left")
    plt.show()

def plot_results_tested_sets(results):
    max_tested_sets = 0

    for elem in results:
        vertices = results[elem][0]
        tested_sets = results[elem][6]
        
        if elem == 125:
            plt.plot([int(v) for v in vertices], [int(v) for v in tested_sets], "-o", color="green", label="12,5%")
        if elem == 25:
            plt.plot([int(v) for v in vertices], [int(v) for v in tested_sets], "-o", color="blue", label="25%")
        if elem == 5:
            plt.plot([int(v) for v in vertices], [int(v) for v in tested_sets], "-o", color="orange", label="5%")
        if elem == 75:
            plt.plot([int(v) for v in vertices], [int(v) for v in tested_sets], "-o", color="red", label="75%")

        elem_max_tested_sets = max([float(v) for v in tested_sets])
        if max_tested_sets < elem_max_tested_sets:
            max_tested_sets = elem_max_tested_sets
    # print([int(v) for v in basic_operations])
    plt.xlabel("Vertices")
    plt.ylabel("Tested Sets")
    plt.ylim([0, max_tested_sets])
    plt.legend(loc="upper left")
    plt.show()

def plot_results_combined_generated_tested(results):
    max_limit_tested = 0
    max_limit_generated = 0

    for elem in results:
        vertices = results[elem][0]
        num_solutions = results[elem][4]
        generated_sets = results[elem][5]
        tested_sets = results[elem][6]
        
        if elem == 125:
            plt.subplot(1, 2, 2)
            plt.plot([int(v) for v in vertices], [int(v) for v in tested_sets], "-o", color="green", label="12,5%")
            plt.subplot(1, 2, 1)
            plt.plot([int(v) for v in vertices], [int(v) for v in generated_sets], "-o", color="green", label="12,5%")
        if elem == 25:
            plt.subplot(1, 2, 2)
            plt.plot([int(v) for v in vertices], [int(v) for v in tested_sets], "-o", color="blue", label="25%")
            plt.subplot(1, 2, 1)
            plt.plot([int(v) for v in vertices], [int(v) for v in generated_sets], "-o", color="blue", label="25%")
        if elem == 5:
            plt.subplot(1, 2, 2)
            plt.plot([int(v) for v in vertices], [int(v) for v in tested_sets], "-o", color="orange", label="5%")
            plt.subplot(1, 2, 1)
            plt.plot([int(v) for v in vertices], [int(v) for v in generated_sets], "-o", color="orange", label="5%")
        if elem == 75:
            plt.subplot(1, 2, 2)
            plt.plot([int(v) for v in vertices], [int(v) for v in tested_sets], "-o", color="red", label="75%")
            plt.xlabel("Vertices")
            plt.ylabel("Tested Sets")
            plt.ylim([0, max_limit_tested])
            plt.legend(loc="upper left")
            plt.subplot(1, 2, 1)
            plt.plot([int(v) for v in vertices], [int(v) for v in generated_sets], "-o", color="red", label="75%")
            plt.xlabel("Vertices")
            plt.ylabel("Generated Sets")
            plt.ylim([0, max_limit_generated])
            plt.legend(loc="upper left")

        new_max_limit_tested = max([int(v) for v in tested_sets])
        if max_limit_tested < new_max_limit_tested:
            max_limit_tested = new_max_limit_tested
        
        new_max_limit_tested = max([int(v) for v in generated_sets])
        if max_limit_generated < new_max_limit_tested:
            max_limit_generated = new_max_limit_tested


    # print([int(v) for v in basic_operations])
    plt.show()

if __name__ == '__main__':
    probs = [125, 25, 5, 75]
    results = get_results(probs)
    # plot_results_solution_time(results)
    # plot_results_basic_operations(results)
    plot_results_best_solution(results)
    # plot_results_generated_sets(results)
    # plot_results_tested_sets(results)
    # plot_results_combined_generated_tested(results)


