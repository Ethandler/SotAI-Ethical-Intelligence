import customtkinter as ctk
from tkinter import Toplevel

# Set appearance and color theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# Initialize main window
root = ctk.CTk()
root.geometry("900x700")  # Default size
root.title("Mr. Klawmideya Chat")

# Variables to manage bot mood and drunkenness
bot_mood = ctk.DoubleVar(value=50)  # Starting at neutral
bot_drunkenness = ctk.DoubleVar(value=30)  # Starting at moderate

# Adjust layout based on window size
def adjust_layout(event=None):
    if root.winfo_width() < 900 or root.winfo_height() < 700:
        chat_frame.pack_forget()
        stats_frame.pack_forget()
        chat_frame.pack(fill="both", expand=True)
        stats_frame.pack(side="bottom", fill="x")
    else:
        chat_frame.pack(side="left", fill="both", expand=True)
        stats_frame.pack(side="right", fill="y")

# Handle sending messages
def handle_send():
    user_input = input_box.get()
    if user_input.strip():
        chat_history.configure(state="normal")
        chat_history.insert("end", f"You: {user_input}\n")
        chat_history.insert("end", "Mr. Klawmideya: Hmm... Let me think about that! *hic*\n")
        chat_history.configure(state="disabled")
        chat_history.see("end")
        input_box.delete(0, "end")
        animate_face()

# Animate bot face during responses
def animate_face():
    bot_face.configure(text="☺")  # Smiling face
    root.after(1000, lambda: bot_face.configure(text="☹"))  # Back to neutral

# Create draggable window for notes or chatbox
def make_draggable(content):
    new_window = Toplevel(root)
    new_window.geometry("400x300")
    new_window.title("Detached View")
    content_widget = ctk.CTkTextbox(new_window, wrap="word")
    content_widget.insert("end", content)
    content_widget.pack(fill="both", expand=True, padx=10, pady=10)

# Frames
chat_frame = ctk.CTkFrame(root)
stats_frame = ctk.CTkFrame(root, width=200)

# Chat widgets
chat_history = ctk.CTkTextbox(chat_frame, state="disabled", wrap="word")
chat_history.pack(fill="both", expand=True, padx=10, pady=10)
chat_history.insert("end", "Welcome to Mr. Klawmideya Chat!\n")

input_box = ctk.CTkEntry(chat_frame, placeholder_text="Type your message here...")
input_box.pack(fill="x", padx=10, pady=5)

send_button = ctk.CTkButton(chat_frame, text="Send", command=handle_send)
send_button.pack(padx=10, pady=5)

# Stats widgets
bot_face = ctk.CTkLabel(stats_frame, text="☹", font=("Helvetica", 32))  # Neutral face
bot_face.pack(pady=20)

mood_label = ctk.CTkLabel(stats_frame, text="Bot Mood")
mood_label.pack()

mood_bar = ctk.CTkProgressBar(stats_frame, variable=bot_mood, progress_color="#FF69B4")  # Neon pink
mood_bar.pack(fill="x", padx=10, pady=5)

mood_bar.set(bot_mood.get() / 100)

drunkenness_label = ctk.CTkLabel(stats_frame, text="Bot Drunkenness")
drunkenness_label.pack()

drunkenness_bar = ctk.CTkProgressBar(stats_frame, variable=bot_drunkenness, progress_color="#FF69B4")  # Neon pink
drunkenness_bar.pack(fill="x", padx=10, pady=5)

drunkenness_bar.set(bot_drunkenness.get() / 100)

# Tabs
tabview = ctk.CTkTabview(root)
tabview.pack(fill="both", expand=True, padx=10, pady=10)

help_tab = tabview.add("Help")
prompt_tab = tabview.add("Suggested Prompts")
char_tab = tabview.add("Character Switching")
notes_tab = tabview.add("Notes")

help_label = ctk.CTkLabel(help_tab, text="Help Instructions Coming Soon!")
help_label.pack(pady=20, padx=20)

notes_drag_button = ctk.CTkButton(notes_tab, text="Detach Notes", command=lambda: make_draggable("Notes content here"))
notes_drag_button.pack(pady=10)

chat_drag_button = ctk.CTkButton(chat_frame, text="Detach Chat", command=lambda: make_draggable("Chat history here"))
chat_drag_button.pack(pady=10)

# Add a background image or wavy effect
def set_background():
    root.configure(bg="#101820")  # Dark background

set_background()

# Bind resize event
root.bind("<Configure>", adjust_layout)

# Start main loop
root.mainloop()
