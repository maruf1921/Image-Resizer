# Image Resizer

This is a simple Python script that allows you to resize an image using the Python Imaging Library (PIL) and the Tkinter library for file selection. It provides a user-friendly interface for selecting an image file, specifying the desired size, and saving the resized image.

## Requirements

- Python 3.x
- Python Imaging Library (PIL) (You can install it using `pip install pillow`)
- Tkinter (Usually comes pre-installed with Python)

## How to Use

1. Clone the repository to your local machine or download the [zip file](link-to-your-repo) and extract it.
2. Ensure you have Python 3.x installed on your system.
3. Install the required libraries using pip:
   ```
   pip install pillow
   ```
4. Run the script:
   ```
   python resize_image.py
   ```
5. The script will open a file dialog where you can select the image you want to resize.
6. After selecting the image, you will be prompted to enter the desired width (x) and height (y) of the resized image.
7. The resized image will be saved as `resized_image.png` in the same directory as the script.

## Example

Here's an example of how to use the script:

```
$ python resize_image.py
Current size: (1920, 1080)
What size do you want to save (x*y)?
Type the value of x: 800
Type the value of y: 600
Successfully resized
```

The script will display the current size of the selected image and prompt you to enter the new width and height. Once you've provided the values, the script will save the resized image as `resized_image.png`.

## Contributing

If you have any suggestions or improvements, feel free to submit a pull request. I'd be happy to collaborate and make this script even better!

## License

This project is licensed under the MIT License - see the [LICENSE](link-to-your-license-file) file for details.
