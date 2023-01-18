# Createing a dictionary with words and word frequencies that can be passed to the generate_from_frequencies function of the WordCloud class.

## Once the dictionary is ready, we use this code to generate the word cloud image:

    - cloud = wordcloud.WordCloud()
    - cloud.generate_from_frequencies(frequencies)
    - cloud.to_file("myfile.jpg")

## Things to remember

    Before processing any text, need to remove all the punctuation marks. To do this, go through each line of text, character-by-character, using the isalpha() method. This will check whether or not the character is a letter.

    To split a line of text into words, use the split() method.

    Before storing words in the frequency dictionary, checking if they’re part of the "uninteresting" set of words (for example: "a", "the", "to", "if"). Making this set a parameter to the function so that it can change if necessary.

## Input file

    For the input file, we need to provide a file that contains text only.
