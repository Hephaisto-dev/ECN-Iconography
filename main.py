# import libraries
import fitz
from glob import glob


def format_pdf(file_name):
    """
    Keep first page and all pages that do contain images
    :param file_name: pdf file
    :return: formatted pdf file
    """
    # open the file
    pdf_file = fitz.open(file_name)
    # iterate over PDF pages
    i = len(pdf_file)
    page_index = 1
    while i > 1:
        # get the page itself
        page = pdf_file[page_index]
        image_list = page.get_images()

        # printing number of images found in this page
        for image in image_list:
            # Check width and height to ignore proposition images
            if image[2] not in [717, 718, 719, 720]:
                print(f"[+] Found at least one image in page {page_index + 1}")
                page_index += 1
                break
        else:
            pdf_file.delete_page(page_index)
        i -= 1
    return pdf_file


if __name__ == '__main__':
    output_pdf = fitz.open()
    for file in glob("input/*.pdf"):
        output_pdf.insert_pdf(format_pdf(file))
    output_pdf.save("output.pdf", garbage=4, deflate=True, clean=True)
