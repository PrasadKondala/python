def copy_file():
    # Prompting the user for the names of two text files
    file1_name = input("Enter the name of the first text file: ")
    file2_name = input("Enter the name of the second text file: ")

    try:
        # Open the first file for reading
        with open(file1_name, 'r') as file1:
            # Read the contents of the first file
            file1_contents = file1.read()

            # Open the second file for writing
            with open(file2_name, 'w') as file2:
                # Write the contents of the first file into the second file
                file2.write(file1_contents)

        print(f"Contents from {file1_name} copied to {file2_name} successfully!")

    except FileNotFoundError:
        print("File not found. Please enter valid file names.")
    except IOError:
        print("Error occurred while reading/writing the file.")


if __name__ == "__main__":
    copy_file()
