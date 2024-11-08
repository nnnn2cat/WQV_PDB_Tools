#WQV PDB Tools Monochrome (WQV-1, WQV-2)
#Iterates through data in work folder and
#converts to 8-bit greyscale BMP
from PIL import ImageTk, Image, ImageOps
import os
import time
import datetime
import sys

path = "work//"
dir_list = os.listdir(path)


#iterate through all files in work dir
idx = 0
for fn in dir_list:
    filename_full = path + fn
    if ".pdr" in filename_full :
        sys.stdout.write("Converting: " + fn + "\n")
        with open(filename_full, "rb") as f:
            xs = bytearray()
            idx += 1

            #ignore the header bytes
            ignore_offset = 0
            while (byte := f.read(1)):
                ignore_offset += 1
                if (ignore_offset >= 37):

                    #initial image is stores as 4-bit greyscale;
                    #split all bytes and multiply by 16 to convert
                    #to 8-bit greyscale so that python can
                    #generate an image
                    decimal = int_val = int.from_bytes(byte, "big")
                    high = (decimal >> 4) & 0xf
                    low = (decimal) & 0xf
                    high *= 16
                    low *= 16
                    bytes_high = high.to_bytes(1, 'big')
                    bytes_low = low.to_bytes(1, 'big')
                    xs.extend(bytes_high)
                    xs.extend(bytes_low)     
                                            

            #output result
            img = Image.frombytes("L", (120, 120), xs)
            img_invert = ImageOps.invert(img)
            img_invert.save("out/" + str(idx) + ".png")
