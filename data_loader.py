import scipy
from glob import glob
import numpy as np
import os
import matplotlib.pyplot as plt
import tensorflow as tf


class DataLoader():
    def __init__(self, dataset_name, img_res=(64, 64)):
        self.dataset_name = dataset_name
        self.img_res = img_res

    def load_data(self, batch_size=1, is_testing=False):
        data_type = "train" if not is_testing else "test"

        if is_testing:
            path = glob('./datasets/CelebATest/*')
        else:
            path = glob('./datasets/CelebATrain/*')

        batch_images = np.random.choice(path, size=batch_size)

        imgs_hr = []
        imgs_lr = []
        for img_path in batch_images:
            img = self.imread(img_path)

            img_hr = scipy.misc.imresize(img, (64, 64))
            img_lr = scipy.misc.imresize(img, (16, 16))

            # If training => do random flip
            if not is_testing and np.random.random() < 0.5:
                img_hr = np.fliplr(img_hr)
                img_lr = np.fliplr(img_lr)

            imgs_hr.append(img_hr)
            imgs_lr.append(img_lr)

        imgs_hr = np.array(imgs_hr) / 127.5 - 1.
        imgs_lr = np.array(imgs_lr) / 127.5 - 1.

        return imgs_hr, imgs_lr

    def load_dataforIdentities(self, path):
        imgs_hr = []
        imgs_lr = []
        os.chdir(path)
        path2 = glob("./test/*")
        batch_images = np.random.choice(path2, size=1)
        for img_path in batch_images:
            img = self.imread(img_path)

            img_hr = scipy.misc.imresize(img, (64, 64))
            img_lr = scipy.misc.imresize(img, (16, 16))


            imgs_hr.append(img_hr)
            imgs_lr.append(img_lr)

        imgs_hr = np.array(imgs_hr) / 127.5 - 1.
        imgs_lr = np.array(imgs_lr) / 127.5 - 1.

        return imgs_hr, imgs_lr


    def imread(self, path):
        return scipy.misc.imread(path, mode='RGB').astype(np.float)
