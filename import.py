import os
import glob

os.chdir("/Users/eugen/Documents/Github")
print(glob.glob("Python Practise/*.py"))


a_list = [1,2,3,4,5,6,7]

b_list = [elem * 2 for elem in a_list]

print(b_list)       