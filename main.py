# STEP 1
# import libraries
import fitz
from glob import glob

default_images_count = 5


def format_pdf(file):
    """
    Keep first page and all pages that do contain images
    :param file: pdf file to be formatted
    :return: formatted pdf file
    """
    # open the file
    pdf_file = fitz.open(file)
    # STEP 3
    # iterate over PDF pages
    i = len(pdf_file)
    page_index = 1
    while i > 1:
        # get the page itself
        page = pdf_file[page_index]
        image_list = page.get_images()

        # printing number of images found in this page
        if len(image_list) > default_images_count:
            print(f"[+] Found a total of {len(image_list)} images in page {page_index + 1}")
            page_index += 1
        else:
            pdf_file.delete_page(page_index)
        i -= 1
    return pdf_file


if __name__ == '__main__':
    output_pdf = fitz.open()
    for file in glob("input/*.pdf"):
        output_pdf.insert_pdf(format_pdf(file))
    output_pdf.save("output.pdf", garbage=4, deflate=True, clean=True)
