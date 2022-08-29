
#Path is a class so the first letter will be in uppercase
from pathlib import Path

path = Path("ecommerce") # creating a path, consider as current dir
print(path.exists()) # Check if path exists
"""
#Creating a dir
path = Path("email") #current dir
path.mkdir()
"""

#remove dir

"""
path = Path("email") #current dir
path.rmdir()

"""

#scan all files in a dir

path = Path() #Current dir. as if '.'
"""
print(path.glob('*')) #search for everything
print(path.glob('*.*')) #only search of all files with any extension. But not dir

"""
#only search of all files with extension py
#returns a generate object for us to iterate through
for file in path.glob('*'):
    print(file)


