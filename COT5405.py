import random
import timeit
import matplotlib.pyplot as plt  # remove this header if matplot is not installed in the system
from memory_profiler import profile  # remove this header if memory_profiler is not installed in the system


class Programming_Assignment1:

    precision = 10

    def __init__(self, sequence_size):
        self.sequence_size = sequence_size

    def generate_random(self):
        minbound = 10 ** (self.sequence_size - 1)
        maxbound = (10 ** self.sequence_size) - 1
        return random.randint(minbound, maxbound)

    # Compute time complexity for this function only - Bitwise subtraction
    # fp = open('memory_profiler_subtract.log', 'w+')  # comment this code when measuring time, else time will recorded for logging as well

    # @profile(precision=precision, stream=fp) # comment this code when measuring time, else time will recorded for logging as well
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

diff_time = []

time_array = []

individual_array = []

initialtime = 0

summationtime = 0


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
    for x in range(1000):
        time = timeit.timeit(setup=SETUP_CODE.replace("***", str(sequence)), stmt=TEST_CODE, number=1000) # change this value to 1 when measuring memory usage
        summationtime += time
        individual_array.append(time)

    avg = summationtime / 1000
    print("Compute time for sequence of size " + str(sequence) + " : " + str(avg))
    diff_time.append(abs(initialtime - avg))
    time_array.append(avg)
    initialtime = avg
    graphplot(range(1000), individual_array, 'iterations', 'Time taken', 'Performance for sequence size ' + str(sequence) +' over million iterations')
    individual_array.clear()



for time in diff_time:
    print("Increase in growth rate between previous and current iteration : " + str(time))

graphplot(sequences, time_array, 'Sequence size', 'Time taken', 'Performance for sequence size  over million iterations')

graphplot(sequences, diff_time, 'Sequence size', 'Time taken', 'Differntiable Growth rate over million iterations')


