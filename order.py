def unique_words(file_name):
    try:
        # Open the file for reading
        with open(file_name, 'r') as file:
            # Read the contents of the file
            file_contents = file.read()

            # Split the contents into words and convert them to lowercase
            words = file_contents.lower().split()

            # Extract unique words and sort them alphabetically
            unique_words = sorted(set(words))

            # Print the unique words
            print("Unique words in alphabetical order:")
            for word in unique_words:
                print(word)

    except FileNotFoundError:
        print("File not found. Please enter a valid file name.")
    except IOError:
        print("Error occurred while reading the file.")

if __name__ == "__main__":
    file_name = input("Enter the name of the text file: ")
    unique_words(file_name)
