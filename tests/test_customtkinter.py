import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x200")
label = ctk.CTkLabel(app, text="CustomTkinter is Working!")
label.pack(pady=20)
app.mainloop()
