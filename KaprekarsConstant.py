#Using the Python language, have the function KaprekarsConstant(num) take the num parameter being passed which will 
#be a 4-digit number with at least two distinct digits. 

#Your program should perform the following routine on the number: 
#Arrange the digits in descending order and in ascending order (adding zeroes to fit it to a 4-digit number), 
#and subtract the smaller number from the bigger number. Then repeat the previous step.

#Performing this routine will always cause you to reach a fixed number: 6174. Then performing the routine on 6174 will 
#always give you 6174 (7641 - 1467 = 6174). Your program should return the number of times this routine must be performed 
#until 6174 is reached. For example: if num is 3524 your program should return 3 because of the following 
#steps: (1) 5432 - 2345 = 3087, (2) 8730 - 0378 = 8352, (3) 8532 - 2358 = 6174. 

def KaprekarsConstant(num): 
    
    routine_count = 0
    
    ascending_list = sorted(str(num))
    
    number_str = "".join(ascending_list)
    
    while num != 6174:
        ascending_list = sorted(str(num))       #must do again for next number if num != 6174 at first, sorts list but #s are strings
        number_str = "".join(ascending_list)    #make the list a string
        ascending_num = int(number_str)         #set ascending number
        descending_num = number_str[::-1]       #set descending number
        descending_num = int(descending_num)    #make descending_num an int
    
        routine_count += 1    #increase the routine count per every iteration
        
        num = descending_num - ascending_num
        
# these if-cases are neccessary for being able to keep performing the operation
# for example, if given number is 1121, ascending order would be 1112 and descending order
# would be 2111. Once we subtract 1112 from 2111 num is equal to 999 which is not a 4-digit
#number so we multiply it by 10 (in this case) to add another digit(zero).
        if(num<10):
            num = num * 1000
        elif(num < 100):
            num = num * 100
        elif(num<1000):
            num = num * 10
            
    return routine_count    
    
print(KaprekarsConstant(input("Enter 4-digit number: ")))  
