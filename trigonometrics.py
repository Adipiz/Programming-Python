# Create two functions that convert from radians to degrees (r2d(x)) and from degrees to radians (d2r(x)) respectively. 
# These functions should be saved in one Python file .py.


# Radians to Degrees
def r2d(x):
    degrees = x*(180/3.14159)
    return degrees 

# Degrees to radians

def d2r(x):
    radians = x*(3.14159/180)
    return(radians)