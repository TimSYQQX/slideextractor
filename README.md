# slideextractor
A simple tool to convert video to slides. Only works when there is no other moving objects in the video other than slides. More features may be added in the future. 

## Dependency 
python3
opencv
tqdm
numpy 

## usage
```
slideextractor.py --source $SOURCEFILE --out $OUTFOLDER 
```
Where $SOURCEFILE is the path to the video(e.g. 'video.mp4'), and $OUTFOLDER is the folder where the slides would be exported to. 
