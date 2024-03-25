import time
from PIL import Image

def get_performance(func, params) -> float:
    start = time.perf_counter()
    func(params)
    end = time.perf_counter()

    return round(end-start, 2)

def inverse_img_colors(chunk):
    result = Image.eval(chunk, lambda x: 255 - x)
    return result

# ------ The following funcitons where my first approach ------
# Note that they need around 12 seconds to process all the image compared to < 0.5 with the functions above


# def _inverse_colors(pixel) -> tuple[int, int, int]:
#     # retrieve original color values and inverse them
#     r = 255 - pixel[0]
#     g = 255 - pixel[1]
#     b = 255 - pixel[2]
    
#     # update the pixel
#     return (r,g,b)

# def inverse_img_colors(img):
#     width = img.size[0]
#     height = img.size[1]

#     pixels = img.load()
#     for x in range(width):
#         for y in range(height):
#             pixels[x,y] = _inverse_colors(pixels[x,y])
    
#     return img
