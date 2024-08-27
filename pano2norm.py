import os
import cv2 
from PIL import Image
import Equirec2Perspec as E2P 
import numpy as np
from matplotlib import pyplot as plt

def batch_process(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for file_name in os.listdir(input_dir):
        if file_name.endswith(('.jpg', '.jpeg', '.png')):
            equ = E2P.Equirectangular(f'{input_dir}/{file_name}')    # Load equirectangular image
            angles = [0,90,120,270] # angles we use to get the street view images 
            for i in angles:
                img = equ.GetPerspective(120, i, 0, 360, 540) # Specify parameters(FOV, theta, phi, height, width)
                cv2.imwrite(f'{output_dir}/{file_name+str(i)}.jpg', img)
                
# Define directories and number of splits






if __name__ == '__main__':

    input_directory = '/Users/siwei/Desktop/900_pano' # replace this with your own directory 
    output_directory = '/Users/siwei/Desktop/3600_svi' # replace this with your own target directory 
    batch_process(input_directory,output_directory)
    #im = Image.fromarray(img)
    #im.save("/Users/siwei/Desktop/output_images/sv1.jpg")
    