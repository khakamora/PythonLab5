'''
Created on 28 жовт. 2018 р.

@author: F
'''
import os

# Open a file
path = "F:\lab5"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
    print (file)
    
#count
print (len([name for name in os.listdir(path) if os.path.isfile(name)]))