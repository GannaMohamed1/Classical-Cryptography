import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            if char.islower():
                shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            else:
                shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():  # Check if character is a letter
            if char.islower():
                shifted = (ord(char) - ord('a') - shift) % 26 + ord('a')
            else:
                shifted = (ord(char) - ord('A') - shift) % 26 + ord('A')
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def encrypt_text():
    text = entry_text.get()
    encrypted_text = encrypt(text, 3)  # shift value 
    entry_result.delete(0, tk.END)
    entry_result.insert(0, encrypted_text)

def decrypt_text():
    encrypted_text = entry_text.get()
    decrypted_text = decrypt(encrypted_text, 3)  
    entry_result.delete(0, tk.END)
    entry_result.insert(0, decrypted_text)

# Create main window
root = tk.Tk()
root.title("Encryp/Decryption")

# Create widgets
label_text = tk.Label(root, text="Enter Text, Dear:")
entry_text = tk.Entry(root, width=30)
label_result = tk.Label(root, text="Result:")
entry_result = tk.Entry(root, width=30)
button_encrypt = tk.Button(root, text="Encrypt", command=encrypt_text)
button_decrypt = tk.Button(root, text="Decrypt", command=decrypt_text)

# Grid positioning
label_text.grid(row=0, column=0, padx=5, pady=5)
entry_text.grid(row=0, column=1, padx=5, pady=5)
label_result.grid(row=1, column=0, padx=5, pady=5)
entry_result.grid(row=1, column=1, padx=5, pady=5)
button_encrypt.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="we")
button_decrypt.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# GUI
root.mainloop()
