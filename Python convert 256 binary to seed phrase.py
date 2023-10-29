import hashlib
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk

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

def update_character_count(event):
    global char_count_label, progress_label, progress_bar
    binary_input = binary_input_entry.get()
    char_count = len(binary_input)
    progress = (char_count / 256) * 100
    char_count_label.config(text=f"Character Count: {char_count}")
    progress_label.config(text=f"Progress: {progress:.2f}%")
    progress_bar["value"] = progress

def show_output():
    binary_input = binary_input_entry.get()
    expected_length = 256

    if len(binary_input) != expected_length:
        messagebox.showerror("Error", "Please enter exactly 256 characters.")
        return

    # Ensure the binary input is a multiple of 8 (1 byte)
    if len(binary_input) % 8 != 0:
        messagebox.showerror("Error", "Invalid binary input. It should be a multiple of 8 (1 byte).")
        return

    # Convert the binary input to bytes
    binary_bytes = bytes(
        int(binary_input[i : i + 8], 2) for i in range(0, len(binary_input), 8)
    )

    # Calculate the SHA-256 hash
    sha256_hash = hashlib.sha256(binary_bytes).hexdigest()
    first_two_characters = sha256_hash[:2]

    binary_result = ""
    for char in first_two_characters:
        hex_number = int(char, 16)
        binary_result += bin(hex_number)[2:].zfill(4)

    concatenated_binary = binary_input + binary_result

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

    # Create a new window to display the output
    output_window = tk.Tk()
    output_window.title("Output")
    output_window.geometry("800x400")  # Set the window size

    def copy_to_clipboard(value):
        output_window.clipboard_clear()
        output_window.clipboard_append(value)
        output_window.update()

    label_width = 30
    entry_width = 70

    tk.Label(output_window, text="SHA-256 hash:", width=label_width).pack()
    sha256_hash_entry = tk.Entry(output_window, width=entry_width)
    sha256_hash_entry.insert(0, sha256_hash)
    sha256_hash_entry.pack()
    sha256_hash_copy_button = tk.Button(output_window, text="Copy", command=lambda: copy_to_clipboard(sha256_hash))
    sha256_hash_copy_button.pack()

    tk.Label(output_window, text="First 2 characters of the hash:", width=label_width).pack()
    first_two_characters_entry = tk.Entry(output_window, width=entry_width)
    first_two_characters_entry.insert(0, first_two_characters)
    first_two_characters_entry.pack()
    first_two_characters_copy_button = tk.Button(output_window, text="Copy", command=lambda: copy_to_clipboard(first_two_characters))
    first_two_characters_copy_button.pack()

    tk.Label(output_window, text="Hexadecimal converted to binary:", width=label_width).pack()
    binary_result_entry = tk.Entry(output_window, width=entry_width)
    binary_result_entry.insert(0, binary_result)
    binary_result_entry.pack()
    binary_result_copy_button = tk.Button(output_window, text="Copy", command=lambda: copy_to_clipboard(binary_result))
    binary_result_copy_button.pack()

    tk.Label(output_window, text="Concatenated binary:", width=label_width).pack()
    concatenated_binary_entry = tk.Entry(output_window, width=entry_width)
    concatenated_binary_entry.insert(0, concatenated_binary)
    concatenated_binary_entry.pack()
    concatenated_binary_copy_button = tk.Button(output_window, text="Copy", command=lambda: copy_to_clipboard(concatenated_binary))
    concatenated_binary_copy_button.pack()

    tk.Label(output_window, text="All words:", width=label_width).pack()
    word_string_entry = tk.Entry(output_window, width=entry_width)
    word_string_entry.insert(0, word_string)
    word_string_entry.pack()
    word_string_copy_button = tk.Button(output_window, text="Copy", command=lambda: copy_to_clipboard(word_string))
    word_string_copy_button.pack()

    output_window.mainloop()

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Create the main input window
    input_window = tk.Tk()
    input_window.title("Binary Input")
    input_window.geometry("400x200")

    # Create a label to display character count
    global char_count_label, progress_label, progress_bar
    char_count_label = tk.Label(input_window, text="Character Count: 0")
    char_count_label.pack()
    progress_label = tk.Label(input_window, text="Progress: 0.00%")
    progress_label.pack()

    # Create a progress bar
    progress_bar = ttk.Progressbar(input_window, orient="horizontal", length=300, mode="determinate")
    progress_bar.pack()

    # Create an entry widget for binary input
    global binary_input_entry
    binary_input_entry = tk.Entry(input_window, width=40)
    binary_input_entry.pack()

    # Bind the entry widget to the update_character_count function
    binary_input_entry.bind("<KeyRelease>", update_character_count)

    # Create a button to submit the binary input
    submit_button = tk.Button(input_window, text="Submit", command=show_output)
    submit_button.pack()

    input_window.mainloop()
    root.mainloop()

if __name__ == "__main__":
    main()
