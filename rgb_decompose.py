#!/usr/bin/python3

from PIL import Image
import copy

def main():
    rgb_color = {}
    rgb_color['red'] = (255,0,0)
    rgb_color['yellow'] = (255,255,0)
    rgb_color['green'] = (0,255,0)
    rgb_color['cyan'] = (0,255,255)
    rgb_color['blue'] = (0,0,255)
    rgb_color['magenta'] = (255,0,255)

    R, G, B = 0, 1, 2

    #with Image.open('pinwheel.jpg') as im_in:
    im_in = Image.open('pinwheel.jpg')
    im_out = copy.deepcopy(im_in)
    im_in.close()
    del(im_in)

    im_r = copy.deepcopy(im_out)
    im_g = copy.deepcopy(im_out)
    im_b = copy.deepcopy(im_out)
    del(im_out)
    #im_out = im_out.convert('L') # convert to grayscale
    w, l = im_r.size
    for x in range(w):
        for y in range(l):
            r, g, b = im_r.getpixel((x,y))
            im_r.putpixel((x,y), (r,0,0))
            im_g.putpixel((x,y), (0,g,0))
            im_b.putpixel((x,y), (0,0,b))
            
    im_r.save('output_R.jpg')
    im_g.save('output_G.jpg')
    im_b.save('output_B.jpg')
    '''
    bands = im_out.split() 
    r_band = bands[R]
    g_band = bands[G]
    b_band = bands[B]
    
    print(r_band)
    '''

    #im_out.save('output.jpg')
    #im_out.close()
    

if __name__=="__main__":
    main()

