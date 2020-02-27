import os
import sys
from buildSolution import BuildSolution

def booking():
    return BuildSolution().mainFunc(sys.argv[1], os.getcwd()+ "\output.txt")

print(booking())

