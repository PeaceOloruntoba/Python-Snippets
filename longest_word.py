def find_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

example_sentence = input("Enter any given sentence to find the longest word in it: ")
print(f"Longest Word: {find_longest_word(example_sentence)}")
