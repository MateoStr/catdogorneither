import tensorflow as tf
import os


#constants
BASE_DIR = "../../data/"
IMAGE_SIZE = (500,500)
BATCH_SIZE = 32
LABEL_MODE = "categorical"



#utility function to create datasets
def create_dataset(directory, image_size = IMAGE_SIZE, batch_size = BATCH_SIZE, label_mode = LABEL_MODE, shuffle = True):
    
    #arguments

    #directory (str): path to the dataset directory
    #image_size (tuple): dimensions of iamge (height/width)
    #batch_size (int): number of images per batch
    #label_mode (str): label encoding format('categorical', 'binary', or None)
    #shuffle (bool): whether or not to shuffle data
#returns:
    #tf.data.Dataset: A prepared dataset for training or evaluation


    return tf.keras.preprocessing.image_dataset_from_directory(
        directory,
        image_size = image_size,
        batch_size = batch_size,
        label_mode = label_mode,
        shuffle = shuffle
    )


train_dir = os.path.join(BASE_DIR, 'train')
val_dir = os.path.join(BASE_DIR, 'val')
test_dir = os.path.join(BASE_DIR, 'test')


#Create Datasets
train_ds = create_dataset(train_dir)
val_ds = create_dataset(val_dir)
test_ds = create_dataset(test_dir)


#normalize datasets
normalization_layer = tf.keras.layers.Rescaling(1./255)

train_ds = train_ds.map(lambda x, y:(normalization_layer(x),y))
val_ds = val_ds.map(lambda x, y:(normalization_layer(x),y))
test_ds = test_ds.map(lambda x, y:(normalization_layer(x),y))


#optimize dataset performance
AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size = AUTOTUNE)
val_ds = val_ds.cache().shuffle(1000).prefetch(buffer_size = AUTOTUNE)
test_ds = test_ds.cache().shuffle(1000).prefetch(buffer_size = AUTOTUNE)


print("Datasets created and process successfully")