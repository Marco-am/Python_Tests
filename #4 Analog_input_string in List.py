from operator import length_hint
import random

randomVal_list=[]
VectorLength = 3

for x in range(0, VectorLength):
    # analog simulated value 
    randomValues = (random.uniform(0.1, 100))
    # append the actual value to the list 
    randomVal_list.append(str(randomValues))
    print('Generated float:', randomValues)
    print('Updated String list:', randomVal_list)