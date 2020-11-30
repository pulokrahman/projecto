import pandas as pd
import numpy as np
from tabulate import tabulate
import time
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def generator_1(num):
    return int(np.mod(np.floor(num*np.power(np.pi,11)),30))
def puzzle_1():
    start = time.time()
    checker_list = []
    puzzle_1_list=[]
    i = 1
   
    #chunked = []
    for i in range(1,301):
        x = generator_1(i)
        if x in checker_list[::2]:
            for y in range(0,len(checker_list),2):
                
                if checker_list[y] == x:
                   count = checker_list[y+1]
                   if(count < 3):
                       puzzle_1_list.append(x)
                       checker_list[y+1] = count + 1
                   break
        else:
            checker_list.append(x)
            checker_list.append(1)
            puzzle_1_list.append(x)
        if(len(puzzle_1_list) == 90):
            break
    chunked = chunks(puzzle_1_list,3)
    end = time.time()
    print(tabulate(chunked, headers=["Face 1", "Face 2","Face 3"],tablefmt="github",showindex = False))
    #print(checker_list)
    #print(chunked)
    print("Program ran for " , end - start, " seconds")


puzzle_1()
