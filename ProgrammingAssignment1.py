import random
import time

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


'#Computing the Operation - we have to write time and space complexity measures here'


def compute():

    for x in range(len(dataset1)):
        dataset3[x] = dataset1[x] + dataset2[x]


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


'# Function calls'

dataset_size = (input("Enter the size for the array :"))
while validateinputs(dataset_size):
    dataset_size = input("Enter valid numerical size for the array: ")

sequence_size = (input("Enter the size for the sequence :"))
while validateinputs(sequence_size):
    sequence_size = input("Enter valid numerical size for the sequence: ")

dataset_size = int(dataset_size)
sequence_size = int(sequence_size)

initialize_data_sets(dataset_size)
random_number_generator(sequence_size, dataset_size)
t1 = time.time()
compute()
t2 = time.time()
print("Compute time : " + str((t2 - t1)))
display()






