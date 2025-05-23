# Dictionaries Practice

# Problem 1: 
# Write a function that takes as input a dictionary and returns a new dictionary,
# where 5 is added to each value of the original dictionary, assuming all values are integers.
# e.g
# {"item1": 2, "item2": 7, "item3": 20} returns {"item1": 7, "item2": 12, "item3": 25}
def new_dict(input_dict):
    new_dic = {}
    for k,v in input_dict.items():
        new_dic[k] = v+5
        
    return new_dic

    
input_dict = {"item1": 2, "item2": 7, "item3": 20}
# print(new_dict({"item1": 2, "item2": 7, "item3": 20})) # expect {"item1": 7, "item2": 12, "item3": 25}






# Problem 2:
# Write a function to check all values are same in a dictionary. 
# Return True if they are all the same, False otherwise
# e.g 
# {'item1': 'apple', 'item2': 'apple', 'item3': 'apple'} returns True, 
# {'item1': 'apple', 'item2': 'apple', 'item3': 'orange'} return False

def check_same_values(input_dict):
    L = list(input_dict.values())
    for i in range(1, len(L)):
        if L[i-1] != L[i]:
            return False
    return True


##### Solution
# def check_same_values(input_dict):
#     values = list(input_dict.values())
#     correct_val = values[0]
#     for val in values:
#         if val != correct_val:
#             return False
#     return True


# testing
input_dict = {'item1': 'apple', 'item2': 'apple', 'item3': 'apple'}
print(check_same_values(input_dict))  # expect True
input_dict = {'item1': 'apple', 'item2': 'apple', 'item3': 'orange'}
print(check_same_values(input_dict))  # expect False






# Problem 3: 
# Convert a dictionary to a list of lists where each sublist is in the 
# form [key, value]. Return a sorted version of this list where we sort 
# by decreasing values. 
# Example input: {'a': 1, 'b': 5, 'c': 10, 'd': 3, 'e': 2} 
# Example output: [['c', 10], ['b', 5], ['d', 3], ['e', 2], ['a', 1]]

def dict_to_sorted_list(input_dict):
    my_list = list(input_dict.items())
    return sorted(my_list, key = lambda x : x[1],  reverse=True)

    
#####   sorted(iterable, key=key, reverse=reverse)
# iterable:(Required)The sequence to sort, list, dictionary, tuple etc.
# key:(Optional) A Function to execute to decide the order. Default is None
# reverse:(Optional) A Boolean. False will sort ascending, True will sort descending. Default is False

# testing
input_dict = {'a': 1, 'b': 5, 'c': 10, 'd': 3, 'e': 2}  
print(dict_to_sorted_list(input_dict))  # expect: [['c', 10], ['b', 5], ['d', 3], ['e', 2], ['a', 1]]





# Problem 4:
# Given a list of dictionaries with item names and amounts in the form {'item': 'my_item_name', 'amount': 'my_amount'}
# write function to combine these items into a single dictionary. See example below. 
# Example input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: {'item1': 1150, 'item2': 300}

def combine_dicts(input_dicts):
    new_dic = {}
    
    for dic in input_dicts:
    #{'item': 'item1', 'amount': 400}
        if dic['item'] not in new_dic :
            new_dic[dic['item']] = dic['amount']
        else:
            new_dic[dic['item']] += dic['amount']
    
    return new_dic
     
      
  

# testing
input_dicts = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
print(combine_dicts(input_dicts))  # expect {'item1': 1150, 'item2': 300}













    