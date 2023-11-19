# Image Watermarking App

This Python script implements a simple GUI application for adding watermarks to images. The application is built using the Tkinter library for the graphical user interface and the Pillow library (PIL) for image processing.

## Features

* __Select Image__: Use the 'Select Image' button to open a file dialog and choose an image file with extensions such as PNG, JPG, JPEG, or GIF.
* __Display Image__: Once an image is selected, it is displayed in the Tkinter window. The image is resized to fit the display area.
* __Add Watermark__: Enter the desired watermark text in the provided Entry widget. Click the 'Add Watermark' button to add the watermark to the selected image. The watermarked image is displayed in the Tkinter window and saved with the filename prefixed by 'watermarked_'.

## Prerequisites

Ensure you have the following libraries installed from requirements.txt:
`
pip install -r requirements.txt
`

## Usage

Run the script and use the GUI to perform the following actions:

1. Click the 'Select Image' button to choose an image file.
2. Enter the desired watermark text in the 'Watermark Text' Entry widget.
3. Click the 'Add Watermark' button to add the watermark to the selected image.

Next step watermarked file will be saved to root folder.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
