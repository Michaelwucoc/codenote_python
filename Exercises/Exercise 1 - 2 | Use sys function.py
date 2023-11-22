"""
Write a Python program to find out what version of Python you are using.

A string containing the version number of the Python interpreter plus additional information on the build number and compiler used. This string is displayed when the interactive interpreter is started.

"""
import sys # Import the sys function to use the system function

print ("Python Version") 
print(sys.version) # get the python version
print("Version Info")
print(sys.version_info) # get the python version info

