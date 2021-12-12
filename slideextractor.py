import argparse
from itertools import count
from pathlib import Path

import cv2
import numpy as np
from tqdm import tqdm


def video2image(source_file, out_folder):
    cap = cv2.VideoCapture(source_file)
    counter = count()

    if (cap.isOpened() == False):
        print("Error opening video stream or file")

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count/fps

    print(f'processing {source_file}')
    print('fps = ' + str(fps))
    print('number of frames = ' + str(frame_count))
    print('duration (S) = ' + str(duration))
    minutes = int(duration/60)
    seconds = duration % 60
    print('duration (M:S) = ' + str(minutes) + ':' + str(seconds))

    checksum = 0
    for _ in tqdm(range(frame_count)):
        if not cap.isOpened():
            break
        ret, frame = cap.read()
        if ret == True:
            new_checksum = np.mean(frame)
            if abs(new_checksum - checksum) >= 1:
                cv2.imwrite(f'{out_folder}/{next(counter)}.png', frame)
                checksum = new_checksum
        else: 
            break
    cap.release()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert video to image folder. ')
    parser.add_argument('--source', metavar='-s', type=str, 
                        help='Video file to convert')
    parser.add_argument('--out', metavar='-o', type=str,  
                        help='Destination folder where the images will be saved')

    args = parser.parse_args()

    source_file = args.source
    out_folder = args.out
    video2image(source_file, out_folder)