import random
import time
import timeit
import matplotlib.pyplot as plt



t3 = time.time()
'#datasets for computation'
dataset1 = []
dataset2 = []
dataset3 = []

'#Initializing the datasets to given array size'


def initialize_data_sets(size):
    global dataset1
    dataset1 = [0 for x in range(size)]
    global dataset2
    dataset2 = [0 for x in range(size)]
    global dataset3
    dataset3 = [0 for x in range(size)]


'#Function for generation random numbers in the datasets 1 and 2'


def random_number_generator(n_digits, size):
    minbound = 10**(n_digits - 1)
    maxbound = (10**n_digits) - 1

    global dataset1
    dataset1 = [random.randint(minbound, maxbound) for x in range(size)]
    global dataset2
    dataset2 = [random.randint(minbound, maxbound) for x in range(size)]


'#Computing the Operation - we have to write time and space complexity measures here - Our operation is subtraction'


def compute():

    for x in range(len(dataset1)):
        dataset3[x] = compute1(dataset1[x], dataset1[2])


def compute1(a, b) -> int:
    return a - b


'#displays the output'


def display():
    print(dataset1)
    print(dataset2)
    print(dataset3)


def validateinputs(input: str) -> bool:
   if input.isdigit():
       return False
   else:
       return True


def graphplot(xaxis, yaxis):
    x = xaxis
    y = yaxis
    plt.plot(x, y)
    plt.xlabel('Sequence Size')
    plt.ylabel('Time Taken')
    plt.show()


'# Function calls'

dataset_size = 1000.

sequences = [4, 8, 16, 32, 64, 128, 256, 512]
dataset_size = int(dataset_size)
List = []

for sequence in sequences:
    sequence_size = int(sequence)
    initialize_data_sets(dataset_size)
    random_number_generator(sequence_size, dataset_size)
    t = timeit.Timer(compute).timeit(number=dataset_size)
    List.append(t)
    print("Compute time for sequence of " + str(sequence) + " : " + str(t))

graphplot(sequences, List)





