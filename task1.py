
'''
    Combines a list of integers into a single integer
    e.g. [1,2,6,8] --> 1268 (type of int)
'''

'''
    Approach is to:
    -Loop through the list
    -convert each number into a string
    -concatenate each number to a string for storage (result)
    -repeat until the list has been fully looped through
    -return result as an integer


    This is because mathematical operations cannot really be used to achieve our desired result.
'''



def find_integer(lst):
    #define result as an empty string
    result= ""

    #Returns none if a list is empty, or if lst is not a list
    if lst==[] or not isinstance(lst,list):
        return None

    #Concatenates each index to the result
    for number in lst:
        result += str(number)
 
    #returns result as an integer, if there is an error, return None
    try:
        return int(result) 
    except ValueError:
        return None

#Test Cases
#In a Perfect Scenario
#input:[8,1,5,3]
#expected: 8153
res = find_integer([8,1,5,3])
print("test 1:",type(res), res)

#When List is Empty
#input:[]
#expected: None
res = find_integer([])
print("test 2:",type(res), res)

#When a string is in the list
#input:[8,"hi",2,4,5]
#expected: None
res = find_integer([8,"hi",2,4,5])
print("test 3:",type(res), res)

#When a string is in the list
#input:[8,"0",2,4,5]
#expected: 80245
res = find_integer([8,"0",2,4,5])
print("test 3:",type(res), res)

#When 0's are at the front of the list
#input:[0,0,0,5]
#expected: 5
res = find_integer([0,0,0,5])
print("test 4:",type(res), res)

#When the input is not a list
#input:True
#expected: None
res = find_integer(True)
print("test 5:",type(res), res)