strings = ["  b n", "f ete", "liths", "astat", "t ene", "  r d"]
first_letters = []
sorted_strings = sorted(strings, key=len, reverse=True)
new = ''
count = 0

if len(sorted_strings[0]) < len(strings):
    for sublist in sorted_strings[0]:
        for word in strings:
            if count < len(word):
                new += word[count]
            if count >= len(word):
                new += ' '
        first_letters.append(new)
        new = ''
        count += 1
        
else:
    for word in sorted_strings[0]:
        for word in strings:
            if count < len(word):
                new += word[count]
            if count >= len(word):
                new += ' '
        first_letters.append(new)
        new = ''
        count += 1
    

for wordss in first_letters:
    print(wordss)
    
