import hashlib

# Function to create a dictionary from the "bip39.txt" file
def create_bip39_dictionary(filename):
    bip39_dict = {}
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(".")
            if len(parts) == 2:
                numeric_number = int(parts[0])
                word = parts[1].strip()
                bip39_dict[numeric_number] = word
    return bip39_dict


def main():
    expected_length = 256
    binary_input = input("Please enter a binary number (256 characters): ")

    if len(binary_input) != expected_length:
        print("Please enter exactly 256 characters.")
    else:
        # Ensure the binary input is a multiple of 8 (1 byte)
        if len(binary_input) % 8 != 0:
            print("Invalid binary input. It should be a multiple of 8 (1 byte).")
        else:
            # Convert the binary input to bytes
            binary_bytes = bytes(
                int(binary_input[i : i + 8], 2) for i in range(0, len(binary_input), 8)
            )

            # Calculate the SHA-256 hash
            sha256_hash = hashlib.sha256(binary_bytes).hexdigest()

            print("SHA-256 hash:", sha256_hash)

        first_two_characters = sha256_hash[:2]
        print(f"First 2 characters of the hash: {first_two_characters}")

        binary_result = ""
        for char in first_two_characters:
            hex_number = int(char, 16)
            binary_result += bin(hex_number)[2:].zfill(4)

        print(f"Hexadecimal converted to binary: {binary_result}")

        concatenated_binary = binary_input + binary_result
        print(f"Concatenated binary: {concatenated_binary}")

        bip39_dict = create_bip39_dictionary("bip39.txt")

        binary_sets = [
            concatenated_binary[i : i + 11]
            for i in range(0, len(concatenated_binary), 11)
        ]

        words = []
        for binary_set in binary_sets:
            numeric_number = int(binary_set, 2) + 1
            if numeric_number in bip39_dict:
                word = bip39_dict[numeric_number]
                words.append(word)

        word_string = " ".join(words)
        print(f"All words: {word_string}")


if __name__ == "__main__":
    main()
