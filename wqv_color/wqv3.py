#WQV PDB Tools for WQV-3, WQV-10.
#Iterates through extracted JPGs, and fixes corruption.

from PIL import Image, ImageTk, ImageOps
import os
import time
import datetime

path = "work//"
dir_list = os.listdir(path)


#Open all images in work directory
for fn in dir_list:
    filename_full = path + fn
    with open(filename_full, "rb") as f:
        ba = bytearray(f.read())
        
        #Search for two bytes beginning with 'DBLK'
        #If they exist, mark the index
        bad_index = 0
        try:
            bad_index = ba.index(b'\x44\x42\x4c\x4b')
            bad_index -= 1
        except ValueError:
            bad_index = -1

        #Create a byte array to store new image
        xs = bytearray()
        position = 0
        
        #look for bad bytes, skip if present
        for byte in ba:
            if ( (bad_index > 0) and (position > bad_index) and (position <= bad_index + 8) ):                                        
                #skip bytes
                check = -1
            else:
                xs.extend(byte.to_bytes(1, 'big'))

            position += 1

        #Output image!
        with open ("out/" + fn, "wb") as binary_file:
            binary_file.write(xs)

