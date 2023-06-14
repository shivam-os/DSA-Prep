str = input("Enter the string: ")
letters_count = {}

#Build the dictionary with letters and their counts
for i in str:
    if i in letters_count:
        letters_count[i] += 1
    else:
        letters_count[i] = 1

#Now get the key with max value
#Java way
# max = 0
# letter = ""
# for i in letters_count:
#     if letters_count[i] > max:
#         max = letters_count[i]
#         letter = i

#Python way
letter = max(letters_count, key=letters_count.get)

print("Letter with max frequency:", letter)
