"""
  A script that can detect if web images are in the same 
  working directory as the script itself written in python using its built-in os module.
  
  works on many operating systems; works on Manjaro linux Works in Windows 11. 
  (I can't afford a mac to test it on a OSX system)
  
  More information about images used in modern websites:
    https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types
  Author: AERivas
  Date: 12/15/2022
"""
import os

WEB_IMAGE_TYPES: list[str] = [
    ".jpeg",
    ".jpg",
    ".jfif",
    ".pjp",
    ".pjpeg",
    ".gif",
    ".svg",
    ".webp",
    ".png",
    ".apng",
    ".avif",
    ".bmp",
    ".tif",
    ".tiff",
    ".ico",
    ".cur"]

  
class NoImageFile(FileNotFoundError):
    """ custom err msg """
    def __init__(self):
        raise FileNotFoundError(f"No compatible web image detected within {os.getcwd()}") from None


def find_web_images():
    """ slightwork """
    list_of_image_file_names: list[str] = []
    for files_and_folder_names in os.listdir():
        dot_notation = files_and_folder_names.rfind(os.extsep)
        file_type = files_and_folder_names[dot_notation:]
        if os.path.isfile(files_and_folder_names):
            if file_type in WEB_IMAGE_TYPES:
                list_of_image_file_names.append(files_and_folder_names)

    if len(list_of_image_file_names) == 0:
       raise NoImageFile from None

    return list_of_image_file_names
  
  
if __name__ == "__main__":
  print(find_web_images())
