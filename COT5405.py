import random
import timeit


class Programming_Assignment1:

    def __init__(self, sequence_size):
        self.sequence_size = sequence_size

    def generate_random(self):
        minbound = 10 ** (self.sequence_size - 1)
        maxbound = (10 ** self.sequence_size) - 1
        return random.randint(minbound, maxbound)

    def compute(self, sequence1, sequence2):
        return sequence1 - sequence2


TEST_CODE = '''

result = object_Programming_Assignment1.compute(sequence_1 , sequence_2)

'''

SETUP_CODE = '''

from __main__ import Programming_Assignment1

object_Programming_Assignment1 = Programming_Assignment1(sequence_size = ***) 
sequence_1 = object_Programming_Assignment1.generate_random()
sequence_2 = object_Programming_Assignment1.generate_random()

#object_Programming_Assignment1 is an object for the class Programming_Assignment1. 

'''

sequences = [4, 8, 16, 32, 64, 128, 256, 512]

for sequence in sequences:
    time = timeit.timeit(setup=SETUP_CODE.replace("***", str(sequence)), stmt=TEST_CODE, number=1000)
    print("Compute time for sequence of size " + str(sequence) + " : " + str(time))


