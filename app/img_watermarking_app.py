import os
from tkinter import Button, Entry, Label, Tk, filedialog

from PIL import Image, ImageDraw, ImageFont, ImageTk

# Global variables
image_path = None
image_label = None
watermark_text = 'Your Watermark Text'
FONT = ('Modern', 12, 'normal')


def select_img():
    '''Callback function to select an image using a file dialog.

    Opens a file dialog to allow the user to select an image file
    with extensions such as PNG, JPG, JPEG, or GIF. If a file is
    selected, updates the global variable `image_path` and calls
    the `show_img` method to display the selected image.
    '''
    global image_path
    file_path = filedialog.askopenfilename(
        filetypes=[('Image files', ['*.png', '*.jpg', '*.jpeg', '*.gif'])])

    if file_path:
        image_path = file_path
        show_img()


def show_img():
    '''Display the selected image.

    Opens the selected image file using the PIL (Pillow) library.
    Resizes the image to fit the display area and displays it in
    the Tkinter window using a Label widget.
    '''
    global image_path, image_label

    image = Image.open(image_path)

    if image.height != 0:
        height = 250
        width = int((height / float(image.height)) * image.width)
        new_size = (width, height)

        scaled_image = image.resize(new_size)
        photo = ImageTk.PhotoImage(scaled_image)

        if image_label:
            image_label.pack_forget()

        image_label = Label(image=photo)
        image_label.image = photo
        image_label.grid(column=1, row=0)


def add_watermark():
    '''Add a watermark to the selected image.

    Reads the watermark text from the Entry widget. If no text is
    provided, uses a default watermark text. Opens the original
    image file with an alpha channel for transparency. Creates a
    copy of the original image and adds the watermark text at a
    calculated position. Saves the watermarked image and displays
    it in the Tkinter window using the `show_img` method.
    '''
    global image_path, image_label, watermark_text

    if image_path:
        watermark_text = watermark_entry.get()
        if not watermark_text:
            watermark_text = 'Your Watermark Text'

        original_image = Image.open(image_path).convert('RGBA')
        width, height = original_image.size

        watermarked_image = original_image.copy()

        draw = ImageDraw.Draw(watermarked_image)

        font = ImageFont.load_default()
        text_color = (192, 192, 192, 128)

        text_bbox = draw.textbbox((0, 0), watermark_text, font=font)

        x = width - (text_bbox[2] - text_bbox[0]) - 100
        y = height - (text_bbox[3] - text_bbox[1]) - 100

        draw.text((x, y), watermark_text, font=font, fill=text_color)

        watermarked_image.save("watermarked_" + os.path.basename(image_path))

        show_img()


# GUI setup
window = Tk()
window.title('Image Watermarking App')
window.geometry('650x600')
window.config(padx=100, pady=100)

image_label = Label(text='Select an image', font=(
    'Modern', 10, 'normal'), bg='white', fg='black')
image_label.config(width=20, height=10)
image_label.grid(column=1, row=0)

select_button = Button(text='Select Image', font=FONT, command=select_img)
select_button.grid(column=1, row=1, pady=25)

watermark_label = Label(text='Watermark Text:', font=FONT)
watermark_label.grid(column=0, row=2, padx=15)

watermark_entry = Entry(font=('Modern', 10, 'normal'))
watermark_entry.insert(0, watermark_text)
watermark_entry.grid(column=1, row=2, columnspan=2)

watermark_button = Button(text='Add Watermark',
                          font=FONT, command=add_watermark)
watermark_button.grid(column=1, row=4, pady=25)

window.mainloop()
