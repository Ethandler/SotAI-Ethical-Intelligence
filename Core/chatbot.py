import tkinter as tk
from tkinter import ttk, simpledialog
import json
import os
import random
from collections import defaultdict

# Persistent Memory JSON File
MEMORY_FILE = "memory.json"

class MrKlawmideya:
    def __init__(self):
        self.responses = {
            "hi": ["Ah, hello there! *hic!* What brings you here today?"],
            "how are you": ["I am as fine as a sip of sake under the moonlight. *hic!*"],
            "what is your name": ["My name is Mr. Klawmideya, your loyal, slightly tipsy assistant. *hic!*"],
            "tell me a joke": ["Why did the ninja refuse dessert? *hic!* He was afraid he'd *split* his pants!"]
        }
        self.meanings = {}
        self.synonyms = {}
        self.antonyms = {}
        self.reinforcement_memory = defaultdict(int)  # Tracks liked responses
        self.disliked_memory = defaultdict(int)  # Tracks disliked responses
        self.load_memory()

    def load_memory(self):
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r") as f:
                data = json.load(f)
                self.responses.update(data.get("responses", {}))
                self.meanings.update(data.get("meanings", {}))
                self.synonyms.update(data.get("synonyms", {}))
                self.antonyms.update(data.get("antonyms", {}))

    def save_memory(self):
        data = {
            "responses": self.responses,
            "meanings": self.meanings,
            "synonyms": self.synonyms,
            "antonyms": self.antonyms
        }
        with open(MEMORY_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def get_face(self):
        return " (¬‿¬) *hic!*"

    def introduce(self):
        return f"{self.get_face()} Greetings, traveler. I am Mr. Klawmideya, the wandering drunken master of wisdom and nonsense."

    def teach_response(self, trigger, response):
        if trigger not in self.responses:
            self.responses[trigger] = []
        self.responses[trigger].append(response)
        self.save_memory()
        return f"*hic!* Learned new response for '{trigger}': {response}"

    def teach_meaning(self, word, meaning):
        self.meanings[word] = meaning
        self.save_memory()
        return f"*hic!* Learned the meaning of '{word}': {meaning}"

    def teach_synonym(self, word, synonym):
        if word not in self.synonyms:
            self.synonyms[word] = []
        self.synonyms[word].append(synonym)
        self.save_memory()
        return f"*hic!* Learned synonym for '{word}': {synonym}"

    def teach_antonym(self, word, antonym):
        if word not in self.antonyms:
            self.antonyms[word] = []
        self.antonyms[word].append(antonym)
        self.save_memory()
        return f"*hic!* Learned antonym for '{word}': {antonym}"

    def get_response(self, user_input):
        user_input = user_input.lower().strip()

        # Check if the user is asking for a meaning
        if user_input.startswith("what does") and user_input.endswith("mean"):
            word = user_input.replace("what does", "").replace("mean", "").strip()
            return self.meanings.get(word, f"*hic!* I don’t know what '{word}' means yet. Teach me, perhaps?")

        for key, response_list in self.responses.items():
            if key in user_input:
                response = random.choice(response_list)
                return response

        return "Ah, that is a riddle even I cannot solve. *hic!* Ask again, but maybe slower?"

class ChatApp:
    def __init__(self, root, bot):
        self.bot = bot
        self.root = root
        self.root.title("Mr. Klawmideya Chat")
        self.root.geometry("600x700")

        # Chat Display
        self.chat_frame = tk.Frame(root)
        self.chat_frame.pack(fill=tk.BOTH, expand=True)

        self.text_widget = tk.Text(self.chat_frame, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 12))
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.chat_frame, command=self.text_widget.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_widget.config(yscrollcommand=self.scrollbar.set)

        # Input Field
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(fill=tk.X, pady=10)

        self.input_box = tk.Entry(self.input_frame, font=("Arial", 14))
        self.input_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.handle_user_input)
        self.send_button.pack(side=tk.RIGHT, padx=10)

        # Teaching Buttons
        self.teach_button_frame = tk.Frame(root)
        self.teach_button_frame.pack(fill=tk.X, pady=5)

        tk.Button(self.teach_button_frame, text="Teach Response", command=self.teach_response_ui).pack(side=tk.LEFT, padx=5)
        tk.Button(self.teach_button_frame, text="Teach Meaning", command=self.teach_meaning_ui).pack(side=tk.LEFT, padx=5)
        tk.Button(self.teach_button_frame, text="Teach Synonym", command=self.teach_synonym_ui).pack(side=tk.LEFT, padx=5)
        tk.Button(self.teach_button_frame, text="Teach Antonym", command=self.teach_antonym_ui).pack(side=tk.LEFT, padx=5)

        # Initialize Chat
        self.display_bot_message(self.bot.introduce())

    def display_bot_message(self, message):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, f"Mr. Klawmideya: {message}\n\n")
        self.text_widget.see(tk.END)
        self.text_widget.config(state=tk.DISABLED)

    def display_user_message(self, message):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.insert(tk.END, f"You: {message}\n\n")
        self.text_widget.see(tk.END)
        self.text_widget.config(state=tk.DISABLED)

    def handle_user_input(self):
        user_input = self.input_box.get().strip()
        if user_input:
            self.display_user_message(user_input)
            bot_response = self.bot.get_response(user_input)
            self.display_bot_message(bot_response)
            self.input_box.delete(0, tk.END)

    def teach_response_ui(self):
        trigger = simpledialog.askstring("Teach Response", "Enter the trigger phrase:")
        if trigger:
            response = simpledialog.askstring("Teach Response", f"Enter the response for '{trigger}':")
            if response:
                bot_response = self.bot.teach_response(trigger, response)
                self.display_bot_message(bot_response)

    def teach_meaning_ui(self):
        word = simpledialog.askstring("Teach Meaning", "Enter the word:")
        if word:
            meaning = simpledialog.askstring("Teach Meaning", f"Enter the meaning of '{word}':")
            if meaning:
                bot_response = self.bot.teach_meaning(word, meaning)
                self.display_bot_message(bot_response)

    def teach_synonym_ui(self):
        word = simpledialog.askstring("Teach Synonym", "Enter the word:")
        if word:
            synonym = simpledialog.askstring("Teach Synonym", f"Enter a synonym for '{word}':")
            if synonym:
                bot_response = self.bot.teach_synonym(word, synonym)
                self.display_bot_message(bot_response)

    def teach_antonym_ui(self):
        word = simpledialog.askstring("Teach Antonym", "Enter the word:")
        if word:
            antonym = simpledialog.askstring("Teach Antonym", f"Enter an antonym for '{word}':")
            if antonym:
                bot_response = self.bot.teach_antonym(word, antonym)
                self.display_bot_message(bot_response)

if __name__ == "__main__":
    root = tk.Tk()
    bot = MrKlawmideya()
    app = ChatApp(root, bot)
    root.mainloop()
