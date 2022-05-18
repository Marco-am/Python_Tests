from operator import length_hint
import random

randomVal_list=[]
VectorLength = 3

for x in range(0, VectorLength):
    # digital simulated value 
    randomValues = bool(random.choice([True, False]))
    # append the actual boolean value to the list 
    randomVal_list.append(randomValues)
    print('Generated Boolean:', randomValues)
    print('Updated boolean list:', randomVal_list)