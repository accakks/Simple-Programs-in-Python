# Function for linear search operation
def linear_search(array, element): 
    for i in range(len(array)): 
        
        # Check if element is in specific index of the array
        if array[i] == element: 
            print (f"{element} is in {i+1} position") 
    
    # If the element is not present in the array, it prints not found     
    if element not in array: 
        print ("Not found")

# Get the size of the array from the user
length = int(input('Enter the number of elements: '))
my_list = []

# Get the input for the list
for i in range(length):
    element = int(input(f"Enter {i+1} element: "))
    my_list.append(element)
    
# Get the element whose position is to be searched for
position = int(input('Enter the element whose position you want to find: '))

linear_search(my_list,position)
