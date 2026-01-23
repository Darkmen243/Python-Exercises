'''
1) Find first non-repeating character in a string

2) Find most frequent word in text

3) Merge overlapping ranges
[(1, 5), (3, 7), (8, 10)]

Some overlap, some don’t.

You must merge overlapping ones so the result becomes:
[(1, 7), (8, 10)]
'''

#1
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
#2
word_dict = {}
max_occ = 0
max_word = ""
try:
    with open("Decent Tasks/3.txt") as file:
        for line in file:
            for word in line.split():
                if word not in word_dict:
                    word_dict[word] = 1
                else:
                    word_dict[word]+=1
        
        for word in word_dict:
            if word_dict[word]>max_occ:
                max_occ = word_dict[word]
                max_word = word
        print(f"Most frequent word in text is {max_word}")
except Exception as ex:
    print(ex)

#3
test_ranges = [(1, 5), (3, 7), (8, 10)]
test_ranges.sort()
merged_ranges = []
current_range = list(test_ranges[0])
for range in test_ranges:
    if current_range[1]>=range[0]:
        current_range[1] = max(current_range[1], range[1]) 
    else:
        merged_ranges.append((current_range[0],current_range[1]))
        print(current_range)
        current_range = list(range)
merged_ranges.append((current_range[0],current_range[1]))    
print(merged_ranges)