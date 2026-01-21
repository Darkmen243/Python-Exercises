'''
Find first non-repeating character in a string

Find most frequent word in text

Merge overlapping ranges
'''
test_string = "aabbcdde"
char_dict = {}
for c in test_string:
    if c not in char_dict:
        char_dict[c] = 1
    else:
        char_dict[c]+=1
for item in char_dict:
    if char_dict[item]==1:
        print(f"First non-repeating character is {item}")
        break

