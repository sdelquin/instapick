import glob
from PIL import Image
import os.path
import shutil
import config

print("Scanning changes...")
for f in glob.glob("{}/*.jpg".format(config.SOURCE_PATH)):
    img = Image.open(f)
    if hasattr(img, "_getexif"):
        exifinfo = img._getexif()
        if exifinfo:
            exif_software = exifinfo.get(config.EXIFTAG_SOFTWARE)
            if exif_software == "Instagram":
                target_path = "{}/{}".format(config.TARGET_PATH,
                                             os.path.basename(f))
                if os.path.exists(target_path):
                    continue
                print("Copying {}...".format(f))
                shutil.copy(f, config.TARGET_PATH)
