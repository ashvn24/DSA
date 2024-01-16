def count_letters(sentence):
    letter_counts = {}

    for char in sentence:
        if char.isalpha():  # Check if the character is a letter
            char = char.lower()  # Convert to lowercase to treat 'A' and 'a' as the same letter
            letter_counts[char] = letter_counts.get(char, 0) + 1

    return letter_counts

# Example usage:
sentence = "Hello, World!"
result = count_letters(sentence)

# Display the result
for letter, count in result.items():
    print(f"{letter}: {count}")
