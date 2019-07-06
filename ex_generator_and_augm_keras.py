from itertools import islice
from os import listdir
from os.path import isfile, join
import numpy as np
from keras_preprocessing.image import load_img

from keras.preprocessing.image import ImageDataGenerator

# Define augmentation generator:
image_gen = ImageDataGenerator(rotation_range=15,
                               width_shift_range=0.1,
                               height_shift_range=0.1,
                               shear_range=0.01,
                               zoom_range=[0.9, 1.25],
                               horizontal_flip=True,
                               vertical_flip=False,
                               fill_mode='reflect',
                               data_format='channels_last',
                               brightness_range=[0.5, 1.5])


# Define reading-file generator
def split_every(batch_size, iterable):
    i = iter(iterable)
    batch_train_file_names = list(islice(i, batch_size))
    while batch_train_file_names:
        # print(batch_train_file_names)
        # One by one read images for X_train and y_train batch
        x_train_batch = np.array([np.array(load_img(join(train_dir, '{}.jpg'.format(f)),
                                                    grayscale=False)) / 255 for f in batch_train_file_names])

        y_train_batch = np.array([np.array(load_img(join(train_masks_dir, '{}.png'.format(f)), grayscale=True))
                                  / 255 for f in batch_train_file_names])
        y_train_batch = y_train_batch.reshape((y_train_batch.shape + (1,)))

        # return batch
        yield x_train_batch, y_train_batch
        batch_train_file_names = list(islice(i, batch_size))


# Wrapper over reading-files generator
def create_aug_gen(in_gen):
    for in_x, in_y in in_gen:
        g_x = image_gen.flow(255 * in_x, in_y,
                             batch_size=in_x.shape[0])
        x, y = next(g_x)
        yield x / 255.0, y


# Paths
train_dir = 'data/train'
train_masks_dir = 'data/train_mask'
# 'train' folder had n files with names 1.jpg, 2.jpg, ..., n.jpg.
# 'train_masks' folder had n files with names 1.png, 2.png, ..., n.png.
# 1.jpg corresponds 1.png and so on

# First of all let's get list of all files:
file_names = np.array([f[:f.find('.')] for f in listdir(train_dir) if isfile(join(train_dir, f))])

# Randomly reserve 80% for train and 20% for valid
train_file_names = np.random.permutation(file_names)[:round(0.8 * len(file_names))]
valid_file_names = np.random.permutation(file_names)[round(0.8 * len(file_names)):]

# These prints are just to check that everything is correct.
print(len(file_names))
print(len(set(train_file_names)))
print(len(train_file_names))
print(len(valid_file_names))
print(len(train_file_names) + len(valid_file_names))

batch_size = 16
generator_data = split_every(batch_size, train_file_names)
aug_data = create_aug_gen(generator_data)
# ---------------------------------------------------
# Example of training:
history = model.fit_generator(
    aug_data,
    steps_per_epoch=len(train_file_names) // batch_size,
    epochs=3,
    verbose=1)
print('Fitted!')
