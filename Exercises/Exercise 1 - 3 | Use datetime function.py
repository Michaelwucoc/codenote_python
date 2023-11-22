"""
The datetime module supplies classes for manipulating dates and times in both simple and complex ways. 
datetime.now(tz=None) returns the current local date and time. 
If optional argument tz is None or not specified, this is like today().
"""
import datetime # import the datetime function get the date info

now = datetime.datetime.now() # get the time now

print ("Current Data and Time:")
print (now.strftime("%Y-%m-%d %H:%M:%S")) # use the strftime to modify the output theme
