import collections

def check_anagram(data1,data2):
    
    results = dict(collections.Counter(data1))
    sort_orders = sorted(results.items(), key=lambda x: x[1], reverse=True)
    if(sort_orders[0][1] > 1):
        return False
    
    elif len(data1) == len(data2):
        if(sorted(data1.lower()) == sorted(data2.lower())):
           return True
            
        return False
    return False
    
print(check_anagram("eat", "tea"))
print(check_anagram("backward","drawback"))
print(check_anagram("Reductions","discounter"))
print(check_anagram("About", "table"))
