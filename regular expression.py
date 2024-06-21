import re

text = input("Enter the text: ")
pattern = input("Enter the regex pattern: ")

matches = re.findall(pattern, text)

if matches:
    print("Matches found:", matches)
else:
    print("No matches found.")




