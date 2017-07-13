"""
author: Fang Ren (SSRL)

5/2/2017
"""
from PIL import Image
import glob, os

path = 'C:\Research_FangRen\Data\Metallic_glasses_data\FeNbTi\Qchi_thumbnails\\'
# filename = path +  'Sample1_24x24_t30_0001_Qchi.png'

os.chdir(path)
for file in glob.glob("*.png"):
    # My image is a 200x374 jpeg that is 102kb large
    foo = Image.open(file)
     # I downsize the image with an ANTIALIAS filter (gives the highest quality)
    foo = foo.resize((200,150),Image.ANTIALIAS)
    foo.save(file,quality=95)
