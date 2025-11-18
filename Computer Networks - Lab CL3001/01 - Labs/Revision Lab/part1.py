def replace_words(input_file, output_file):
    # Read the input file content
    with open(input_file, 'r') as file:
        content = file.read()

    while True:
        word_to_replace = input("Word to replace: ")
        replacement_word = input("Replacement word: ")
        
        # Replace occurrences of the word
        content = content.replace(word_to_replace, replacement_word)

        # Ask user if they want to continue replacing words
        continue_replacing = input("Do you want to continue? (Yes/No): ").strip().lower()
        if continue_replacing != "yes":
            break

    # Write the updated content to output file
    with open(output_file, 'w') as file:
        file.write(content)

    print(f"Updated content written to {output_file}")

# Specify file names
input_filename = "input.txt"
output_filename = "output.txt"

# Call the function
replace_words(input_filename, output_filename)

