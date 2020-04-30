# type 'pip3.8 install requests' in terminal to add the 'requests' package
#necessary for the API request part of the weather program
#type 'pip3.8 install Pillow' in terminal to add the 'Pillow' package
#Pillow stands for Python Imaging Library and helps when working with images

import tkinter as tk

HEIGHT = 600
WIDTH = 700

root = tk.Tk()

#make a container to add the GUI widgets to
#use 'canvas' to create the container
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

#to organize the widgets in the GUI, use a frame
#can assign background attribute with color string like 'blue' or enter the #hexadecimal
frame = tk.Frame(root, bg='#80c1ff')
#can use packing, placing or grid. I use .place below and relative width and height)
#relwidth and relheight just fills the parent frame with the above blue background
#frame.place(relwidth=1, relheight=1)
#below using relative x and y to center the frame and relative width and height to color just part of the canvas
#0.1 means 10% in from each side in x and y and 0.8 means fill the middle 80% of the canvas, I think
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

#add a button widget to the GUI
#the background attribute 'bg' won't work no matter what I do
#the button doesn't resize along with the canvas and frame and it's coloring seems to be overwritten by the frame color
#button = tk.Button(root, text='Test button', fg='blue', activeforeground='green')
#above, I added the button to 'root', but you can also add it to the frame
#the active background defaults to blue no matter what I do!
button = tk.Button(frame, text="Test button", bg='green')
button.pack()

#add a label to the GUI
label=tk.Label(frame, text="this is a label", bg='yellow')
label.pack()

#add an entry bar to the GUI
entry=tk.Entry(frame, bg='green')
entry.pack()

root.mainloop()
