from tkinter import *
from PIL import Image, ImageTk
import action
import spech_to_text

# Function to handle user input from Entry box
def process_user_input():
    user_text = user_entry.get()
    bot_response = action.handle_command(user_text)
    chat_window.insert(END, "You --> " + user_text + "\n")
    if bot_response:
        chat_window.insert(END, "Bot --> " + str(bot_response) + "\n")
    if bot_response == "Okay, shutting down the system now.":
        root.destroy()

# Function to handle voice input
def process_voice_input():
    voice_input = spech_to_text.spech_to_text()
    bot_reply = action.handle_command(voice_input)
    chat_window.insert(END, "You --> " + voice_input + "\n")
    if bot_reply:
        chat_window.insert(END, "Bot --> " + str(bot_reply) + "\n")
    if bot_reply == "Okay, shutting down the system now.":
        root.destroy()

# Function to clear chat text area
def clear_chat():
    chat_window.delete("1.0", END)

# GUI window setup
root = Tk()
root.title("Smart AI Assistant")
root.geometry("550x675")
root.config(bg="#6F8FAF")
root.resizable(False, False)

# Frame for heading and image
header_frame = LabelFrame(root, padx=100, pady=7, relief=RAISED, bd=3, bg="#6F8FAF")
header_frame.grid(row=0, column=1, padx=55, pady=10)

# Title label
title = Label(header_frame, text="Smart Assistant", font=("Comic Sans MS", 14, "bold"), bg="#356696", fg="white")
title.grid(row=0, column=0, padx=20, pady=10)

# Assistant image
assistant_img = ImageTk.PhotoImage(Image.open("image/assitant.png"))
image_label = Label(header_frame, image=assistant_img)
image_label.grid(row=1, column=0, pady=20)

# Chat display area
chat_window = Text(root, font=("Courier", 10, "bold"), bg="#356696", fg="white")
chat_window.place(x=100, y=375, width=375, height=100)

# User input box
user_entry = Entry(root, justify=CENTER)
user_entry.place(x=100, y=500, width=350, height=30)

# Voice input button
ask_button = Button(root, text="Ask", bg="#356696", pady=16, padx=40, relief=SOLID, bd=3, command=process_voice_input)
ask_button.place(x=70, y=575)

# Send text input button
send_button = Button(root, text="Send", bg="#356696", pady=16, padx=40, relief=SOLID, bd=3, command=process_user_input)
send_button.place(x=400, y=575)

# Clear text button
clear_button = Button(root, text="Clear", bg="#356696", pady=16, padx=40, relief=SOLID, bd=3, command=clear_chat)
clear_button.place(x=225, y=575)

# Start GUI loop
root.mainloop()