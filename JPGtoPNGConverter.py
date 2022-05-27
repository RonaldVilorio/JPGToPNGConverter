import sys
from pathlib import Path
from PIL import Image

oldFolderName = sys.argv[1]
newFolderName = sys.argv[2]

oldFolder = Path(f"/Users/ron/Desktop/image_playground/{oldFolderName}")
newFolder = Path(f"/Users/ron/Desktop/image_playground/{newFolderName}")

if newFolder:
    # we have the new folder already
    pass
else:
    # create the new folder
    Path(f"/Users/ron/Desktop/image_playground/{newFolderName}").mkdir()

for child in oldFolder.iterdir():
    img = Image.open(child)
    img.save((str(newFolder)+"/"+child.name)[0:-3]+"png", "png")


