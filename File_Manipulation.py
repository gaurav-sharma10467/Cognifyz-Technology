# Write a Python program that reads a text
# file and counts the occurrences of each
# word in the file. Display the results in
# alphabetical order along with their
# respective counts.

number_of_words = 0
with open('/home/frontman/Documents/Cognifyz Technology/Level-2/SampleFile.txt','r') as file:
    data = file.read()
    lines = data.split()
    number_of_words += len(lines)

print(number_of_words)
