import tkinter as tk

def on_key_press(event):
    """Function to handle key presses."""
    if event.keysym == "Return":
        text = entry.get()
        print("Typed:", text)
        # You can perform any action with the typed text here
        entry.delete(0, tk.END)  # Clear the entry widget after processing the input

def on_button_click(word):
    """Function to handle button clicks."""
    print("Selected:", word)
    # Append the word to the text area
    text_area.insert(tk.END, word + " ")

# Create the main window
root = tk.Tk()
root.title("Pop-up Screen")

# Create a text entry box at the top center
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=20)
entry.bind("<KeyPress>", on_key_press)

# Create a text area
text_area = tk.Text(root, font=("Arial", 14), height=5)
text_area.pack()

# Create a frame for the keyboard layout
keyboard_frame = tk.Frame(root)
keyboard_frame.pack()

# Define the keyboard layout
keyboard_layout = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '-'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', ' ']
]

# Create keyboard buttons
for row, keys in enumerate(keyboard_layout):
    for col, key in enumerate(keys):
        button = tk.Button(keyboard_frame, text=key, width=3, height=1, font=("Arial", 12),
                           command=lambda key=key: entry.insert(tk.END, key))
        button.grid(row=row, column=col)

# Create buttons for predefined words on the left side
predefined_words = ["Pain", "Leg", "Arm", "Stomach", "Back", "Head"]
for word in predefined_words:
    button = tk.Button(root, text=word, width=10, font=("Arial", 12),
                       command=lambda word=word: on_button_click(word))
    button.pack(side=tk.LEFT, padx=10, pady=5)

# Create buttons for specific actions on the right side
specific_actions = ["Hungry", "Thirsty", "Help"]
for action in specific_actions:
    button = tk.Button(root, text=action, width=10, font=("Arial", 12),
                       command=lambda action=action: on_button_click(action))
    button.pack(side=tk.RIGHT, padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()

