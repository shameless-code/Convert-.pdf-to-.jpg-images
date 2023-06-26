#!/usr/bin/env python

from pdf2image import convert_from_path
import os


def pdf_to_img(page_name, path_to_PDF):
    """Converts PDF file into images. The images have a name define in 'page_name'."""

    # Creating directory for images
    path_to_location = os.path.dirname(path_to_PDF)
    output_dir = os.path.join(path_to_location, page_name)
    os.makedirs(output_dir, exist_ok=True)

    try:  # to convert the PDF into images
        print('Converting PDF, please wait.')
        pages = convert_from_path(path_to_PDF)
        for i, page in enumerate(pages):
            # iterate over pages of the PDF and provides for each image a corresponding number
            image_name = f"{i} {page_name}.jpg"
            image_path = os.path.join(output_dir, image_name)
            print(f'Saving image: {image_name}')
            page.save(image_path, 'JPEG')

    except Exception as e:  # problems with finding PDF or conversion itself
        print(f"Error while converting the PDF:\n{e}")


def main():
    """Ask the user for the name of the output directory (this will also be the base name for output files)
       and for  PDF file's directory.
       Each filename for created images will be distinguished by a corresponding number.
       The output directory will be created in the PDF file's directory."""

    # Ask the user for the name for output directory and output .jpg files
    name = input('File name:\n').strip()
    # Ask the user for the path to the PDF file
    file_loc = input('File location:\n').strip()

    # Convert the PDF into .jpg images and save them to the specified folder
    pdf_to_img(name, file_loc)


if __name__ == '__main__':
    main()
