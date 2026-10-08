# Word Analysis

sentence = input("Enter a sentence: ")

words = sentence.split()

total_words = len(words)
total_characters = len(sentence)

longest_word = words[0]
shortest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

    if len(word) < len(shortest_word):
        shortest_word = word


vowels = 0

for letter in sentence:
    if letter.lower() in "aeiou":
        vowels = vowels + 1


unique_words = set(words)

alphabetical_words = sorted(unique_words)


print(" Word Analysis ")
print("Total Words:", total_words)
print("Total Characters:", total_characters)
print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)
print("Total Vowels:", vowels)

print("Unique Words:", unique_words)

print("Words in Alphabetical Order:")
for word in alphabetical_words:
    print(word)


file_text = "Word Analysis"
file_text = file_text + "Total Words: " + str(total_words) + "\n"
file_text = file_text + "Total Characters: " + str(total_characters) + "\n"
file_text = file_text + "Longest Word: " + longest_word + "\n"
file_text = file_text + "Shortest Word: " + shortest_word + "\n"
file_text = file_text + "Total Vowels: " + str(vowels) + "\n"
file_text = file_text + "Unique Words: " + str(unique_words) + "\n"
file_text = file_text + "Alphabetical Words: " + str(alphabetical_words) + "\n"


f = open("word_analysis.txt", "w")
f.write(file_text)
f.close()

print("\nAnalysis word_analysis.txt file  is saved !")