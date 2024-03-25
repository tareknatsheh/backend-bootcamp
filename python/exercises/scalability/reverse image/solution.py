"""
Image inverse
"""

import concurrent.futures
from utils.helpers import get_performance, inverse_img_colors

from PIL import Image

def combine_chunks(chunks):
    """
    Takes the 4 pieces that represent the whole image and paste them together
    Each 'chunk' is of type Image from PIL

    returns the resulted complete image
    """

    total_width = chunks[0].width + chunks[1].width
    total_height = chunks[0].height + chunks[2].height

    # Create a new image with the dimensions
    result_image = Image.new('RGB', (total_width, total_height))

    # Paste each chunk at the correct position in the image
    result_image.paste(chunks[0], (0, 0))
    result_image.paste(chunks[1], (chunks[0].width, 0))
    result_image.paste(chunks[2], (0, chunks[0].height))
    result_image.paste(chunks[3], (chunks[0].width, chunks[2].height))

    return result_image


def with_multipreccessing(img) -> None:
    """
    Using the power of multiprocessing to process the image
    It's cropped into 4 pieces, then each piece is processes in parallel
    """
    width = img.size[0]
    height = img.size[1]
    # divide image into chunks
    top_left = img.crop((0, 0, width // 2, height // 2))
    top_right = img.crop((width // 2, 0, width, height // 2))
    bottom_left = img.crop((0, height // 2, width // 2, height))
    bottom_right = img.crop((width // 2, height // 2, width, height))

    chunks = [top_left, top_right, bottom_left, bottom_right]

    # the .map function takes a list of inputs and passes them one by one
    # to the function that processes them in parallel
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(inverse_img_colors, chunks)

    result_image = combine_chunks(list(results))
    # --- uncomment the following line to save the result in a jpg file ---
    # result_image.save('with_multipro.jpg')
    

def without_multiproccessing(img):
    result_image = inverse_img_colors(img)
    # --- uncomment the following line to save the result in a jpg file ---
    # result_image.save("without.jpg")


def main():
    img = Image.open('img1.jpg')
    print("Without:", get_performance(without_multiproccessing, img)) # takes around 0.52 seconds the first time you run it
    print("With:", get_performance(with_multipreccessing, img)) # this guy takes around 0.18 seconds (about triple the speed!)
    pass



if __name__ == "__main__":
    main()