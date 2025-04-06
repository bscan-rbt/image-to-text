from customtkinter import *
from extract_table import convert_image

root = CTk()
layout_frame = CTkFrame(root)

layout_frame.columnconfigure(0, minsize= 100)
layout_frame.columnconfigure(3, minsize= 100)
layout_frame.columnconfigure(1, weight=1)
layout_frame.rowconfigure(0, minsize=110)
layout_frame.rowconfigure(3, minsize=50)


image_file_entry = CTkEntry(layout_frame)

def select_image():
    image_path = filedialog.askopenfilename()
    global image_file_entry
    image_file_entry.configure(placeholder_text = image_path)


image_file_entry.grid(column=1, row=2, sticky = "NSEW")
img_select_label = CTkLabel(layout_frame, text= "Select image to convert...").grid(column = 1, row = 1)
image_select_btn= CTkButton(layout_frame, text= "Select Image...", command = select_image).grid(column=2, row=2, sticky = "NSEW", padx = 10)

dest_file_entry = CTkEntry(layout_frame)
    
def select_dest():
    dest_path = filedialog.asksaveasfilename(defaultextension= ".xlsx")
    global dest_file_entry
    dest_file_entry.configure(placeholder_text= dest_path)

dest_select_label = CTkLabel(layout_frame, text= "Select CSV destination....").grid(column = 1, row = 3, pady= (40,0))
dest_file_entry.grid(column=1, row=4, sticky = "NSEW")
dest_select_btn= CTkButton(layout_frame, text= "Select Folder...", command= select_dest).grid(column=2, row=4, sticky = "NSEW", padx = 10)

convert_btn= CTkButton(layout_frame, text= "Convert", command= lambda: convert_image(image_file_entry.cget("placeholder_text"), dest_file_entry.cget("placeholder_text"))).grid(column=1, row=5, sticky = "NSEW", pady = 30)


layout_frame.pack(expand = True, fill = "both")



root.geometry("800x500")
root.title("Image to Text")

def run():
    root.mainloop()


