import random
import timeit
import matplotlib.pyplot as plt


class Programming_Assignment1:

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

            borrow = (~inv_sequence1) & sequence2  # gather all the bits that are 1's since 1 + 1 will give a carry

            sequence1 = sequence1 ^ sequence2  # Sum of all bits except 1 + 1 since carry has that.

            sequence2 = borrow << 1 # shifting carry

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

# variables

sequences = [4, 8, 16, 32, 64, 128, 256, 512]

time = 0


# operations = []
#
# summation_time = 0
#
# averagetimer = []


# Function to plot the performance

def graphplot(xaxis, yaxis, xlabel, ylabel, title):
    x = xaxis
    y = yaxis
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()


for sequence in sequences:
    time = timeit.timeit(setup=SETUP_CODE.replace("***", str(sequence)), stmt=TEST_CODE, number=1000)
    print("Compute time for sequence of size " + str(sequence) + " : " + str(time))

# # time = timeit.timeit(setup=SETUP_CODE.replace("***", str(4)), stmt=TEST_CODE, number=1000)
# # print("Compute time for sequence of size " + str(sequence) + " : " + str(time))
#
#
# # Computing performance over 1000 iterations for 1000 random inputs of varied size of n
# for sequence in sequences:
#     for x in range(1000):
#         time = timeit.timeit(setup=SETUP_CODE.replace("***", str(sequence)), stmt=TEST_CODE, number=1000)
#         summation_time += time
#         operations.append(time)
#     # graphplot(range(1000), operations, 'Iterations', 'Time taken', 'Performance for sequence size ' + str(sequence) + ' over 1000 iterations')
#     averagetimer.append(summation_time / 1000)
#     summation_time = 0
#     operations.clear()
#     print("Compute time for sequence of size " + str(sequence) + " : " + str(time))
# #
# #
# graphplot(sequences, averagetimer, 'Sequence', 'Average Compute Time', 'Order of growth of runtimes as the input scales')

