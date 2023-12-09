""" 
Practice Question 2: Merge Dictionaries

Task:

Create a function merge_dictionaries that takes two dictionaries and 
merges them into one. If a key exists in both dictionaries, 
the value from the second dictionary should be used.
"""

def merge_dictionaries(dict_one, dict_two):
    ans = dict_one
    for key, value in dict_two.items(): #second dict overwrites the first
        ans[key] = value

    return ans