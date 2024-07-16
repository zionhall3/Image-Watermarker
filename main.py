from PIL import Image as PILImage 
from tkinter import *
import os
from tkinter import filedialog, messagebox
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


def restart():
        global image_selected
        image_selected = False
        global image_to_edit
        image_to_edit = ""

        global watermark_selected 
        watermark_selected = False
        global watermark_to_add
        watermark_to_add = ""


        global output_folder_selected 
        output_folder_selected = False
        global output_folder
        output_folder = ""

        select_button.config(text=Image_Select_Text1)
        watermark_button.config(text=Watermark_Select_Text1)
        folder_button.config(text=Folder_Select_Text1)


def convert_image():
        if image_selected and watermark_selected and output_folder:
                image_path = os.path.join(image_to_edit)
                watermark_path = os.path.join(watermark_to_add)
                image_filename = os.path.basename(image_path)
                extension = os.path.splitext(image_path)[1]
                finished_img_name = image_filename + " WM."
                output_path = os.path.join(output_folder, os.path.splitext(finished_img_name)[0]+extension)

                image = PILImage.open(image_path)
                
                wm_image = PILImage.open(watermark_path)
                
                wm_resized = wm_image.resize((round(image.size[0]*.35), round(image.size[1]*.35)))
                wm_mask = wm_resized.convert("RGBA")
                position = (image.size[0] - wm_resized.size[0], image.size[1] - wm_resized.size[1])

                transparent = PILImage.new('RGBA', image.size, (0,0,0,0))
                transparent.paste(image, (0, 0))
                transparent.paste(wm_mask, position, mask=wm_mask)

                finished_img = transparent.convert("RGB")
                finished_img.save(output_path)
                messagebox.showinfo("Finished!", "The image now has a watermark!")
                os.startfile(output_folder)
                restart()

        
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