def count_characters(file_content):
    return len(file_content)

def count_vowels(file_content):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in file_content if char in vowels)

def count_words(file_content):
    return len(file_content.split())

def count_sentences(file_content):
    return len(file_content.splitlines())

def main():
    try:
        with open('input.txt', 'r') as file:
            file_content = file.read()
            
            total_chars = count_characters(file_content)
            total_vowels = count_vowels(file_content)
            total_words = count_words(file_content)
            total_sentences = count_sentences(file_content)
            
            print(f"Total Characters: {total_chars}")
            print(f"Total Vowels: {total_vowels}")
            print(f"Total Words: {total_words}")
            print(f"Total Sentences: {total_sentences}")
            
    except FileNotFoundError:
        print("The file 'input.txt' was not found.")
        
if __name__ == "__main__":
    main()
