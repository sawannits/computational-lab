text=input("Enter text to count no of char and words\n")
words = text.lower().split()
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
char_freq ={}
for char in text:
	if char in char_freq:
		char_freq[char]+=1;
	else:
		char_freq[char]=1
print (f"word freq:{word_freq}\n char freq:{char_freq}")
