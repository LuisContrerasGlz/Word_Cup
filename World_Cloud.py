import wordcloud
import string


def create_wordcloud(file_path, uninteresting_words):
    # Initialize the dictionary to store the word frequencies
    frequencies = {}
    # Open the file and read its contents
    with open(file_path, "r") as file:
        text = file.read()
    # Remove all punctuation marks from the text
    text = "".join(c for c in text if c not in string.punctuation)
    # Split the text into words
    words = text.split()
    # Iterate through the words
    for word in words:
        # Check if the word is not in the uninteresting set
        if word.lower() not in uninteresting_words:
            # Add the word to the dictionary or increment its value
            frequencies[word.lower()] = frequencies.get(word.lower(), 0) + 1
    return frequencies


uninteresting_words = {"a", "the", "to", "if"}
frequencies = create_wordcloud("myfile.txt", uninteresting_words)

cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies)
cloud.to_file("myfile.jpg")

"""

This function first reads the contents of the input file, then it removes all punctuation marks from the text, and splits it into words. 

It then iterates through the words, checking if each word is not in the uninteresting set, and if not, it adds it to the frequency dictionary or increments its value.

This function takes in two parameter, a file_path which is the path to the input text file, and uninteresting_words which is a set of uninteresting words that you want to ignore while creating the word cloud.

After that, it uses the frequency dictionary to create the word cloud image by passing it to generate_from_frequencies() method of the WordCloud class and then it saves the image to a file using the to_file() method.

"""
