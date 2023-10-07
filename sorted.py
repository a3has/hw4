def reverse_sort_dictionary(in_dict):
    
    if not isinstance(in_dict, dict):
        raise TypeError("Input must be a dictionary.")
    
    sorted_dict = sorted(in_dict.items(), key = lambda x: x[0], reverse = True)
    
    rev_dict = [(name, phone[0]) for name, phone in sorted_dict]
    
    return rev_dict

#print(reverse_sort_dictionary({'Tom' : (5464512, 24) , 'Sara' : (5446987, 32) , 'Mary' : (1557896, 20)}))