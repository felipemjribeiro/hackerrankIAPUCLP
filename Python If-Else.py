#!/bin/python

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(raw_input().strip()) 
if(n % 2) != 0:                         #If  is odd, print Weird
    print ("Weird")
elif n >= 2 and n <= 5:                 #If  is even and in the inclusive range of  to , print Not Weird
    print ("Not Weird")  
elif n >= 6 and n <= 20:                #If  is even and in the inclusive range of  to , print Weird
    print ("Weird")  
elif n > 20:                            #If  is even and greater than , print Not Weird
    print ("Not Weird")