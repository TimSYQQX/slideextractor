import argparse
from pathlib import Path
from slideextractor import video2image


def batch_convert(source_folder, out_folder):
    source_folder = "./source"
    out_folder = './out'

    source_path = Path(source_folder)
    out_path = Path(out_folder)

    for video in source_path.iterdir():
        if video.name.split('.')[-1] == 'mp4':
            cur_folder = Path(str(out_path), video.name.split('.')[0])
            cur_folder.mkdir(parents=True, exist_ok=True)
            video2image(str(video), str(cur_folder))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert batch of video to image folders. ')
    parser.add_argument('--source', metavar='-s', type=str, default='source', 
                        help='Video folder to convert')
    parser.add_argument('--out', metavar='-o', type=str,  default='out',
                        help='Destination folder where the images will be saved')
    args = parser.parse_args()
    batch_convert(args.source, args.out)
