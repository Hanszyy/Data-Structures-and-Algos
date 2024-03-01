# Initializing an array (using Python lists)
arr = [10, 20, 30, 40, 50]

# Accessing elements
print(arr[0])       # prints first element in the array, array starts from 0
print(arr[-2])      # kinda like counts in reverse

# Iterating through the array
for element in arr:
    print(element + 1) # prints all the elements, (with +1)

# Modifying elements
arr[2] = 50000 # changes 3rd element to 50k
arr.append(600000) # adds 600k as an element to the end of arry

# Array slicing
print(arr[0:2])     # slices elements out, excluding the last one (2nd element), 1st & 2nd element prints
print(arr[:3])      # slices elements out, 0,1,2 prints out except 3rd element
print(arr[2:])      # starts from [2], only [0] [1] excluded 
print(arr[::-1])    # reverse order
print(arr[:-1:])    # excluding last element
print(arr[-1::])    # counts reverse, going back from first element returns to last element
print(arr)