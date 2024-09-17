'''
Function to find the longest common prefix among an array of strings.
'''
def longestCommonPrefix(strs):
    if not strs:  
        return ""
    
    if len(strs) == 1:  
        return strs[0]
    
    
    prefix = strs[0]
    
   
    for i in strs[1:]:
        while not i.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"])) 
print(longestCommonPrefix(["dog", "racecar", "car"]))    
print(longestCommonPrefix(["apple", "ape", "april"]))     
print(longestCommonPrefix([""]))                          
print(longestCommonPrefix(["alone"]))                    
