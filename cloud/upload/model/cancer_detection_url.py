from keras.preprocessing import image as im
import cv2
import numpy as np
import PIL
from PIL import Image
from pyimagesearch.cancernet import CancerNet
from keras.optimizers import Adagrad
import image_slicer
from skimage import io
from django.conf import settings
import boto3
from botocore.client import Config

# Use the array data from the first image in this dataset:
NUM_EPOCHS = 40
INIT_LR = 1e-2
opt = Adagrad(lr=INIT_LR, decay=INIT_LR / NUM_EPOCHS)
dim = (48,48)

# load model
model = CancerNet.build(width=48, height=48, depth=3, classes=2)
model.load_weights('/home/visiodeibc/breast-cancer-classification/previous_model/weights00000040.h5')

# image slicer
red = Image.new('RGBA', (50,50), color='red')
red.putalpha(1)

#initial image name
init = 0
temp_img_dir = 'put_temporary_directory_path_here'

def process_image(url, pid):
    image = io.imread(url)
    cv2.imwrite(temp_img_url+str(init)+'.png',image)
    size  = cv2.imread(image)
    size = int((size.shape[0]/50)*(size.shape[0]/50))

    tiles = image_slicer.slice(temp_img_dir+str(init)+'.png', size, save=False)
    
    tile_index = 0

    for tile in tiles:
        # print(tile.image.shape)
        tile = np.array(tile.image)
        #tile = tile[:,:,:-1]   #for png we need this if not we don't reducing alpha
        tile = cv2.resize(tile,dim)
        tile  = im.img_to_array(tile)
        tile  = tile/255
        tile = np.expand_dims(tile, axis=0)
        print(model.predict_classes(tile)[0])
        if(model.predict_classes(tile)[0] == 1):
            
            alpha = tiles[tile_index].image.copy()
            tiles[tile_index].image = alpha.putalpha(1)
            tiles[tile_index].image = Image.alpha_composite(red,alpha)
        tile_index += 1

    tiles = image_slicer.join(tiles)
    #upload the image here 'tiles' is the processed image
    ACCESS_KEY_ID = 'AKIASKKR5242U53BQZ5C'
    ACCESS_SECRET_KEY = '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'
    BUCKET_NAME = '4160-project'
    outputName = "test/prsimg_" + pid + ".jpg"
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )
    s3.Bucket(BUCKET_NAME).put_object(Key=outputName, Body=tiles)
    result_path = 'https://' + '4160-project.s3.amazonaws.com' +'/'+ outputName
    init += 1
    return(result_path) # return the url
    