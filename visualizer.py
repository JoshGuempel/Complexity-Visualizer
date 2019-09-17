#Josh guempel
#pa01

import math
import time
from random import randint
import matplotlib.pyplot as plt
import pylab

class SortClass:
    def merge_sort(self, A, p, r):
        if p < r:
            q = (p + r) // 2
            self.merge_sort(A, p, q)
            self.merge_sort(A, q + 1, r)
            self.merge(A, p, q, r)

    def merge(self, A, p, q, r):
        n1 = q - p + 1
        n2 = r - q
        
        L = []
        R = []

        for i in range(n1):
            L.append(A[p + i])
        for j in range(n2):
            R.append(A[q + j + 1])

        L.append(math.inf)
        R.append(math.inf)
        
        i = 0
        j = 0
        
        #assert statements commented out so as to not mess with runtime
        for k in range(p,  r+1):
            #assert self.is_sorted(A[p:k]) == True
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
    
    def insertion_sort(self, A):

        for i in [type(j) is int for j in A]:
            assert i == True

        #original = [i for i in A]
        #assert statements commented out so as to not mess with runtime
        for j in range(1, len(A)):
            #assert self.is_sorted(A[1:j]) == True
            key = A[j]
            i = j - 1
            while i > -1 and A[i] > key:
                A[i + 1] = A[i]
                i -= 1
            A[i + 1] = key

        #assert sorted(original) == A
        

    
    def selection_sort(self, A):

        for i in [type(j) is int for j in A]:
            assert i == True

        #original = [i for i in A]

        for i in range(len(A)-1):
            #assert self.is_sorted(A[:i]) == True
            min = i
            for j in range((i+1), len(A)):
                if A[min] > A[j]:
                    min = j
            A[i], A[min] = A[min], A[i]
        
        #assert sorted(original) == A
    
    def is_sorted(self, A):
        return all(A[i] <= A[i+1] for i in range(len(A) - 1))

    def timed_merge_sort(self, A):
        for i in [type(j) is int for j in A]:
            assert i == True
        begin = time.time()
        #original = [i for i in A]
        self.merge_sort(A, 0, len(A) - 1)
        #assert sorted(original) == A
        end = time.time()
        return end - begin

    def timed_insertion_sort(self, A):
        begin = time.time()
        self.insertion_sort(A)
        end = time.time()
        return end - begin

    def timed_selection_sort(self, A):
        begin = time.time()
        self.selection_sort(A)
        end = time.time()
        return end - begin

def random_array(n):
    a = []
    for i in range(n):
        a.append(randint(0,1000))
    return a


def compare_algorithms(case):
    '''Compare merge sort, insertion, sort, and selection sort for 2000 big array with best/wors/avg case'''
    S = SortClass()
    input_sizes = []

    #generate data for merge
    merge_sort_runtimes = []

    #generate data for insert
    insert_sort_runtimes = []

    #generate data for select
    select_sort_runtimes = []

    i = 50
    while i < 2000:
        input_sizes.append(i)

        a1 = random_array(i)

        if case == 'best':
            a1.sort()
        elif case == 'worst':
            a1.sort()
            a1.reverse()
        merge_sort_runtimes.append(S.timed_merge_sort(a1))
        
        a2 = random_array(i)

        if case == 'best':
            a2.sort()
        elif case == 'worst':
            a2.sort()
            a2.reverse()
        insert_sort_runtimes.append(S.timed_insertion_sort(a2))

        a3 = random_array(i)

        if case == 'best':
            a3.sort()
        elif case == 'worst':
            a3.sort()
            a3.reverse()        	
        select_sort_runtimes.append(S.timed_selection_sort(a3))

        i += 50


    #graph each set of points as a line
    pylab.plot(input_sizes, merge_sort_runtimes, '-g', label='merge sort')
    pylab.plot(input_sizes, insert_sort_runtimes, '-r', label='insertion sort')
    pylab.plot(input_sizes, select_sort_runtimes, '-b', label='selection sort')

    pylab.legend(loc='upper left')
    pylab.title(case + str(' case runtime'))
    pylab.xlabel('number of elements')
    pylab.ylabel('time in seconds')
    pylab.show()

def input_file():
    S = SortClass()

    A = []
    B = []
    C = []
    filename = str(input('enter a file name:  '))
    with open(filename) as f:
        for line in f:
            A.append(int(line))
            B.append(int(line))
            C.append(int(line))
    merge_time = S.timed_merge_sort(A)
    insert_time = S.timed_insertion_sort(B)
    select_time = S.timed_selection_sort(C)
    
    print("Array after merge sort: ")
    print(A)
    print("Array after insertion sort: ")
    print(B)
    print("array after selection sort: ")
    print(C)

    print("Merge sort runtime: " + str(merge_time))
    print("Insertion sort runtime: " + str(insert_time))
    print("selection sort runtime: " + str(select_time))

def main():
    print("~~~~~~~~~~~~~~~~~~~~~WELCOME TO THE SORTING ALGORITHM COMPARISON THINGY 6000~~~~~~~~~~~~~~~~~~~~")
    
    quit = False

    #basic menu that runs the analysis with commands
    while(not quit):
        command = str(input("enter 'compare' to graph the runtimes, or enter 'input' to input a file. or 'quit' to quit:  "))
        if command == 'compare':
            case = str(input("Enter 'best', 'worst', or 'average':  "))
            compare_algorithms(case)
        elif command == 'input':
           input_file()
        elif command == 'quit':
            quit = True
        else:
            print("not valid command")
    
if __name__ == '__main__':
    main()
