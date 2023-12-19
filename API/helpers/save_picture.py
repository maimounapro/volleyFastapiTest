# from fastapi import UploadFile, File
# import aiofiles


# async def save_picture(fileName: str = None, in_file: UploadFile = File(...)):
#     async with aiofiles.open(f"static/{fileName}.jpg", "wb") as out_file:
#         while content := await in_file.read(1024):  # async read chunk
#             await out_file.write(content)




import os
from uuid import uuid4
from PIL import Image

static = 'static'

def save_picture(file, folderName: str = '', fileName: str = None):
    randon_uid = str(uuid4())
    _, f_ext = os.path.splitext(file.filename)
    
    picture_name = (randon_uid if fileName==None else fileName.lower().replace(' ', '')) + f_ext 

    path = os.path.join(static,folderName)
    if not os.path.exists(path):
        os.makedirs(path)
        
    picture_path = os.path.join(path,picture_name)

    output_size = (125,125)
    img = Image.open(file.file)
    
    img.thumbnail(output_size)
    img.save(picture_path)
    
    return f'{static}/{folderName}/{picture_name}'