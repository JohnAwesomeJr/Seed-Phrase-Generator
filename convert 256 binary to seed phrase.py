# Import the hashlib module to use for SHA-256 hashing
import hashlib

# Function to create a dictionary from the "bip39.txt" file
def create_bip39_dictionary(filename):
    # Initialize an empty dictionary to store the mappings
    bip39_dict = {}
    
    # Open and read the contents of the specified file
    with open(filename, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Split the line into two parts using the period as the delimiter
            parts = line.strip().split(".")
            
            # Check if there are exactly two parts in the line
            if len(parts) == 2:
                # Extract the numeric number and the associated word
                numeric_number = int(parts[0])
                word = parts[1].strip()
                
                # Add the mapping to the dictionary
                bip39_dict[numeric_number] = word
    
    # Return the populated dictionary
    return bip39_dict

# Main program entry point
def main():
    # Define the expected length of the binary input
    expected_length = 256
    
    # Prompt the user for a 256-character binary input
    binary_input = input("Please enter a binary number (256 characters): ")

    # Check if the input length is not 256 characters
    if len(binary_input) != expected_length:
        print("Please enter exactly 256 characters.")
    else:
        # Ensure the binary input is a multiple of 8 (1 byte)
        if len(binary_input) % 8 != 0:
            print("Invalid binary input. It should be a multiple of 8 (1 byte).")
        else:
            # Convert the binary input to bytes
            binary_bytes = bytes(int(binary_input[i:i+8], 2) for i in range(0, len(binary_input), 8)

            # Calculate the SHA-256 hash of the binary input
            sha256_hash = hashlib.sha256(binary_bytes).hexdigest()

            # Print the calculated SHA-256 hash
            print("SHA-256 hash:", sha256_hash)

            # Extract the first two characters of the hash
            first_two_characters = sha256_hash[:2]
            print(f"First 2 characters of the hash: {first_two_characters}")

            # Convert the hexadecimal characters to binary
            binary_result = ""
            for char in first_two_characters:
                hex_number = int(char, 16)
                binary_result += bin(hex_number)[2:].zfill(4)

            # Print the binary representation of the hexadecimal characters
            print(f"Hexadecimal converted to binary: {binary_result}")

            # Concatenate the binary input and the binary result
            concatenated_binary = binary_input + binary_result
            print(f"Concatenated binary: {concatenated_binary}")

            # Create a dictionary from "bip39.txt"
            bip39_dict = create_bip39_dictionary("bip39.txt")

            # Split the concatenated binary into sets of 11 characters each
            binary_sets = [concatenated_binary[i:i+11] for i in range(0, len(concatenated_binary), 11)]

            # Initialize a list to store the associated words
            words = []

            # Iterate through the binary sets
            for binary_set in binary_sets:
                # Convert the binary set to a numeric number and add 1
                numeric_number = int(binary_set, 2) + 1
                # Check if the numeric number is in the BIP-39 dictionary
                if numeric_number in bip39_dict:
                    # Get the corresponding word and add it to the list
                    word = bip39_dict[numeric_number]
                    words.append(word)

            # Join the list of words into a single string
            word_string = " ".join(words)
            print(f"All words: {word_string}")

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()
