'''
Function to reverse a string word by word.
'''
def reverse_words(s: str) -> str:
    n = len(s)
    i = 0
    
    while i < n and s[i] == ' ':
        i += 1
    
    j = n - 1
    while j >= 0 and s[j] == ' ':
        j -= 1
    
    if i > j:
        return ""
    
    words = []
    word = []
    
    while i <= j:
        if s[i] != ' ':
            word.append(s[i])
        elif word:
            words.append(''.join(word))
            word = []
        i += 1
    
    if word:
        words.append(''.join(word))
    
    words.reverse()
    
    return ' '.join(words)

print(reverse_words("the sky is blue"))          
print(reverse_words("  hello world  "))        
print(reverse_words("a good   example"))        
print(reverse_words("    "))                     
print(reverse_words("word"))                    
