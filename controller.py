import cv2
import mediapipe as mp
import pyautogui
import tkinter as tk

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)

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
