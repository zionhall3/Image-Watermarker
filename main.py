from PIL import Image, ImageTk, ImageDraw
from tkinter import *
import os
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename

# image_to_edit = ""
# watermark_to_add = ""
# output_folder = ""

image_selected = False
watermark_selected = False
output_folder_selected = False

root = Tk()
root.resizable(width=False, height=False)
#Keeps window at a small compact size
root.minsize(100,100)
root.title(" Image Watermarker")

Image_Select_Text1 = "Please select an image"
Image_Select_Text2 = "Image has been selected"

Watermark_Select_Text1 = "Please select a watermark"
Watermark_Select_Text2 = "Watermark has been selected"

Folder_Select_Text1 = "Please select an output folder"
Folder_Select_Text2 = "Output folder has been selected"

def select_image():
        global image_to_edit
        image_to_edit = filedialog.askopenfilename()
        global image_selected
        image_selected = True
        select_button.config(text=Image_Select_Text2)


def select_watermark():
        global watermark_to_add
        watermark_to_add = filedialog.askopenfilename()
        global watermark_selected
        watermark_selected = True
        watermark_button.config(text=Watermark_Select_Text2)

def select_folder():
        global output_folder
        output_folder = filedialog.askdirectory()
        global output_folder_selected
        output_folder_selected = True
        folder_button.config(text=Folder_Select_Text2)

def convert_image():
        pass

select_button = Button(root, height = 2,
                 width = 25,
                 text= Image_Select_Text1, 
                 command = lambda:select_image())

watermark_button = Button(root, height = 2,
                 width = 25,
                 text= Watermark_Select_Text1, 
                 command = lambda:select_watermark())

folder_button = Button(root, height = 2,
                 width = 25,
                 text= Folder_Select_Text1, 
                 command = lambda:select_folder())


convert_button = Button(root, height = 2,
                 width = 25,
                 text="Convert", 
                 command = lambda:convert_image())


select_button.pack()
watermark_button.pack()
folder_button.pack()
convert_button.pack()

mainloop()





# from PIL import Image, ImageTk, ImageDraw
# import tkinter as tk
# from tkinter.filedialog import askopenfilename, asksaveasfilename
 
# SOURCE_DIRECTORY = "../Users/Paul/Pictures"
# TARGET_DIRECTORY = "../Users/Paul/Pictures/Watermarked Photos"
 
 
# def open_file():
#     #Open dialog and allow file to be selected.
#     #Merge watermark and main photo
#     #Resave photo to TARGET_DIRECTORY
#     browse_text.set("Loading...")
#     photo_name = askopenfilename(initialdir=SOURCE_DIRECTORY, title="Select A File", filetype=
#         (("jpeg files", "*.jpg"), ("all files", "*.*")))
#     if photo_name:
#         image = Image.open(photo_name).convert("RGBA")
#         wm_image = Image.open("images/Paul Watermark 2.png").convert("RGBA")
 
#         # Size watermark relative to size of base image
#         wm_resized = wm_image.resize((round(image.size[0]*.35), round(image.size[1]*.35)))
#         wm_mask = wm_resized.convert("RGBA")
 
#         # Set position to lower right corner
#         position = (image.size[0] - wm_resized.size[0], image.size[1] - wm_resized.size[1])
 
#         transparent = Image.new('RGBA', image.size, (0,0,0,0))
#         transparent.paste(image, (0, 0))
#         transparent.paste(wm_mask, position, mask=wm_mask)
#         transparent.show()
 
#         # Save watermarked photo
#         finished_img = transparent.convert("RGB")
#         finished_img_name = photo_name[:-4] + " WM.jpg"
#         finished_img.save(finished_img_name)
 
#         success_text.set(f"Success!  File saved to {finished_img_name}.")
 
#         browse_text.set("Browse")
 
# def quit():
#     root.destroy()
 
# #GUI should allow you to select photo / path to add images,
# #  Outgoing photo name / path
# root = tk.Tk()
# root.title("Photo Watermark App")
 
# canvas = tk.Canvas(root, width=600, height=500)
# canvas.grid(columnspan=5, rowspan=4)
 
# logo = Image.open("images/logo.png")
# logo = logo.resize((200, 200))
# logo = ImageTk.PhotoImage(logo)
# logo_label = tk.Label(image=logo)
# logo_label.image = logo
# logo_label.grid(column=3, row=0)
 
# instruction_label = tk.Label(root, text="Select photo to watermark.", font="Ariel")
# instruction_label.grid(columnspan=5, column=0, row=1)
 
# # Browse dialog button
# browse_text = tk.StringVar()
# browse_btn = tk.Button(root, command=open_file, textvariable=browse_text, font="Ariel", bg="#20bebe", fg="white", height=2, width=15)
# browse_text.set("Browse")
# browse_btn.grid(column=2, row=2)
 
# # Success Message
# success_text = tk.StringVar()
# success_text.set(" ")
# success_label = tk.Label(root, textvariable=success_text)
# success_label.grid(columnspan=5, column=0, row=3)
 
# # Cancel Button
# cancel_btn = tk.Button(root, text="Quit", command=quit, font="Ariel", bg="#20bebe", fg="white", height=2, width=15)
# cancel_btn.grid(column=4, row=2, padx=10)
 
# root.mainloop()