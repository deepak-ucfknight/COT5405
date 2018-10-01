import random
import timeit
import matplotlib.pyplot as plt      # remove this header if memory_profiler is not installed in the syste
import sys


# variables

sequences = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

time = 0

diff_time = []

time_array = []

individual_array = []

initial_time = 0

summation_time = 0

average_memory = []

memory = []


class Programming_Assignment1:

    precision = 10

    def __init__(self, sequence_size):
        self.sequence_size = sequence_size

    def generate_random(self):
        minbound = 10 ** (self.sequence_size - 1)
        maxbound = (10 ** self.sequence_size) - 1
        return random.randint(minbound, maxbound)

    # Compute time complexity for this function only - Bitwise subtraction

    def subtract(self, sequence1, sequence2):

        if sequence1 < sequence2:
            swapper = sequence1
            sequence1 = sequence2
            sequence2 = swapper

        while sequence2 != 0:

            inv_sequence1 = ~sequence1

            borrow = inv_sequence1 & sequence2  # gather all the bits that are 1's since 1 + 1 will give a carry

            sequence1 = sequence1 ^ sequence2  # Sum of all bits except 1 + 1 since carry has that.

            sequence2 = borrow << 1  # shifting carry

        memory.append(sys.getsizeof(sequence1))

        return sequence1


TEST_CODE = '''

result = object_Programming_Assignment1.subtract(sequence_1 , sequence_2)

'''

SETUP_CODE = '''

from __main__ import Programming_Assignment1

object_Programming_Assignment1 = Programming_Assignment1(sequence_size = ***) 
sequence_1 = object_Programming_Assignment1.generate_random()
sequence_2 = object_Programming_Assignment1.generate_random()

#object_Programming_Assignment1 is an object for the class Programming_Assignment1. 

'''

# Function to plot the performance


def graphplot(xaxis, yaxis, xlabel, ylabel, title):
    x = xaxis
    y = yaxis
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


print("--------------------------------------------------")
print("Time Complexity")
print("---------------------------------------------------")
for sequence in sequences:
    for x in range(1000):
        time = timeit.timeit(setup=SETUP_CODE.replace("***", str(sequence)), stmt=TEST_CODE, number=1000) # change this value to 1 when measuring memory usage
        summation_time += time
        individual_array.append(time)
    average_memory.append(sum(memory) / len(memory))
    memory.clear()

    avg = summation_time / 1000
    print("Compute time for sequence of size " + str(sequence) + " : " + str(avg))
    diff_time.append(abs(initial_time - avg))
    time_array.append(avg)
    initial_time = avg
    # graphplot(range(1000), individual_array, 'iterations', 'Time taken', 'Performance for sequence size ' + str(sequence) +' over 1000 iterations')
    individual_array.clear()

print("--------------------------------------------------")
print(" Growth rate ")
print("---------------------------------------------------")

for growth in range(1, len(diff_time)):
    print("Growth Factor for sequence of size " + str(sequences[growth]) + " : " + str(diff_time[growth] / diff_time[growth - 1]))


graphplot(sequences, time_array, 'Sequence size', 'Time taken', 'Performance for sequence size  over 1000 iterations')

graphplot(sequences, diff_time, 'Sequence size', 'Time taken', 'Differentiable growth rate')

print("--------------------------------------------------")
print(" Space Complexity ")
print("---------------------------------------------------")

for mem_consumption in range(len(average_memory)):
    print("Space allocated for sequence of size " + str(sequences[mem_consumption]) + " : " + str(average_memory[mem_consumption]))

graphplot(sequences, average_memory, 'sequence structure', 'Space consumed', 'space complexity')






