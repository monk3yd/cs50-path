from cs50 import get_string

X = 1.0
x = 0.0588
y = 0.296

text = get_string("Text: ")

letters = 0.0
words = 0.0 + X
sentences = 0.0

for i in text:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        letters += 1.0
    elif i == ' ':
        words += 1.0
    elif i == '.' or i == '?' or i == '!':
        sentences += 1.0
    #print(text[i], end="")
    
index = x * 100 * letters / words - y * 100 * sentences / words - 15.8
index = round(index)
    
if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")