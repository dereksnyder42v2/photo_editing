#!/usr/bin/python3

from PIL import Image
import sys
import copy

def main():
    for idx in range(1, len(sys.argv)):
        filename = sys.argv[idx]
        print(f"Converting {filename}...")
        try:
            new_filename = f"{filename.split('.')[0]}_gray.{filename.split('.')[1]}"
            with Image.open(filename) as im:
                im_out = copy.deepcopy(im)
                del(im)
                im_out = im_out.convert('L')
                im_out.save(new_filename)
                del(im_out)    
        except Exception as err:
            print(f"Exception processing {filename};")
            print(err)
            quit(1)
        

if __name__=="__main__":
    main()
