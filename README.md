# slideextractor
A simple tool to convert video to slides. Only works when there is no other moving objects in the video other than slides. More features may be added in the future. 

## Dependency 
- python3
- opencv
- tqdm
- numpy 

## usage
Single File conversion
```
python slideextractor.py --source $SOURCEFILE --out $OUTFOLDER 
```
Where $SOURCEFILE is the path to the video(e.g. 'video.mp4'), and $OUTFOLDER is the folder where the slides would be exported to. 
Multifile conversion
```
python batch_conversion.py --source $SOURCEFOLDER --out $OUTFOLDER 
```
Where $SOURCEFOLDER is the path to the video folder, and $OUTFOLDER is the folder where the slides would be exported to. 
Multifile conversion