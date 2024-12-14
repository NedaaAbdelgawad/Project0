import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def play_text():
    text = text_entry.get("1.0", tk.END).strip()  
    if text:
        try:
            tts = gTTS(text,lang='en')
            tts.save("output.mp3")
            os.system("start output.mp3")
        except Exception as e:
            messagebox.showerror("Error",f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter some text to play.")

def exit_app():
    root.destroy()

def clear_text():
    text_entry.delete("1.0",tk.END)

root = tk.Tk()
root.title("Text-to-Speech")
root.geometry("400x300")  

title_label = tk.Label(root, text="Text to Speech", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

text_entry = tk.Text(root, width=40, height=5, font=("Arial", 12))
text_entry.pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

play_button = tk.Button(buttons_frame, text="Play", width=10, bg="lightgreen", font=("Arial", 12), command=play_text)
play_button.grid(row=0, column=0, padx=5)

exit_button = tk.Button(buttons_frame, text="Exist", width=10, bg="tomato", font=("Arial", 12), command=exit_app)
exit_button.grid(row=0, column=1, padx=5)

set_button = tk.Button(buttons_frame, text="Set", width=10, bg="lightblue", font=("Arial", 12), command=clear_text)
set_button.grid(row=0, column=2, padx=5)

root.mainloop()