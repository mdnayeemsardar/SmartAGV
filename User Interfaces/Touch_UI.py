from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image  
from tkinter import messagebox

# Create the Tkinter window
root = tk.Tk()
root.geometry('1200x800')

# Define functions to handle button clicks
def start_button_click():
    print("robot has started")

def stop_button_click():
    print("robot is stopped") 

def pause_button_click():
    print("robot process suspended") 

# Load the initial map image
image = Image.open('updated_image.png')
photo = ImageTk.PhotoImage(image)

# Create a label to hold the map image
label = tk.Label(root, image=photo)
label.pack()
label.place(x=50, y=200)

# Define a function to update the image
def update_image():
    while True:
        try:
            # Load the updated map image
            updated_image = Image.open('updated_image.png')
            updated_photo = ImageTk.PhotoImage(updated_image)

            # Update the label with the new image
            label.configure(image=updated_photo)
            label.image = updated_photo
            label.place(x=610, y=300)
            root.after(100, update_image)
            break
        except Exception as e:
            print(f"Error loading image: {e}")
            root.after(1000)

# Start updating the image
root.after(100, update_image)

# Load a picture1 and make it as a click button
im = PhotoImage(file="start.png")
start_btn1 = Button(root, image=im, command=start_button_click)
start_btn1.pack()
start_btn1.place(x=200, y=5)

# Load a picture2 and make it as a click button
im_1 = PhotoImage(file="stop256.png")
start_btn2 = Button(root, image=im_1, command=stop_button_click)
start_btn2.pack()
start_btn2.place(x=650, y=5)

# Load a picture3 and make it as a click button
im_2 = PhotoImage(file="pause.png")
start_btn3 = Button(root, image=im_2, command=pause_button_click)
start_btn3.pack()
start_btn3.place(x=1080, y=5)

# Start the Tkinter main loop
root.mainloop()