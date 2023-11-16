class StringReverser:
    def reverse_words(self, sentence):
        # Split the sentence into words
        words = sentence.split()

        # Reverse the order of words
        reversed_words = words[::-1]

        # Join the reversed words to form the reversed sentence
        reversed_sentence = ' '.join(reversed_words)
        return reversed_sentence

# Example usage:
reverser = StringReverser()
input_sentence = "Hello World! This is a test."
reversed_result = reverser.reverse_words(input_sentence)
print(f"The reversed sentence is: {reversed_result}")
