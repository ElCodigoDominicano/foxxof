"""
  A script that can detect if web images are in the same working directory as 
  the script itself written in python using its built-in os module.
  
  works on many operating systems; works on Manjaro linux Works in Windows 11. 
  (I Haven't tried it on a MACOSX system)
  
  More information about images used on modern websites:
    https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types
  
  Author: AERivas
  Date: 12/15/2022
"""
import os

WEBIMAGETYPES: list[str] = [
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


# Per PEP-0317 => https://peps.python.org/pep-0317/
class NoImageFile(FileNotFoundError):
    pass


def find_web_images():
    """ Displays a list containing the detected web images filename
    and file extensions obtained from a current working directory
    including hidden image files ex: .temp.jpg"""
    
    list_of_image_filenames: list[str] = []
    for files_and_folder_names in os.listdir():
        dot_notation = files_and_folder_names.rfind(os.extsep)
        file_type = files_and_folder_names[dot_notation:]
        if os.path.isfile(files_and_folder_names):
            if file_type in WEBIMAGETYPES:
                list_of_image_filenames.append(files_and_folder_names)

    if len(list_of_image_filenames) == 0:
       raise NoImageFile(f"No image detected within the current working directory => {os.getcwd}")
    print(list_of_image_filenames)
  
  
if __name__ == "__main__":
    find_web_images()
