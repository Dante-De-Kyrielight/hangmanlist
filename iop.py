import itertools
import string

def generate_hangman_words(min_length=1, max_length=50):
    # Define the character set: letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    for length in range(min_length, max_length + 1):
        filename = f"hangmanlist-{length}-char.txt"  # Create filename for each length
        with open(filename, "w") as file:
            # Generate all combinations of the given length
            for word in itertools.product(characters, repeat=length):
                file.write("".join(word) + "\n")
            print(f"Completed generation for length {length}, saved in {filename}")
    print(f"All files created for word lengths from {min_length} to {max_length}.")

# Generate hangman words from 1 to 50 characters in separate files
generate_hangman_words(min_length=1, max_length=50)
