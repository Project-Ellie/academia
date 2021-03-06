import gzip
import numpy
import os


DATA_DIR = "../data/"
img_train = os.path.join(DATA_DIR, "train-images-idx3-ubyte.gz")
lbl_train = os.path.join(DATA_DIR, "train-labels-idx1-ubyte.gz")
img_test = os.path.join(DATA_DIR, "t10k-images-idx3-ubyte.gz")
lbl_test = os.path.join(DATA_DIR, "t10k-labels-idx1-ubyte.gz")


class MnistBatcher:

    """
    A mini-batch provider for MNIST Images
    """

    def __init__(self, img_file, lbl_file, num_samples):
        self.IMAGE_SIZE = 28
        self.PIXEL_DEPTH = 255
        self.img_file = img_file
        self.lbl_file = lbl_file
        self.num_samples = num_samples
        self.current_image = 0
        self.preprocessor = None
        (self.imgs, self.lbls) = self.extract_data()

    def extract_data(self):
        with gzip.open(self.img_file) as bytestream:
            bytestream.read(16)

            buf = bytestream.read(self.IMAGE_SIZE * self.IMAGE_SIZE * self.num_samples)
            imgs = numpy.frombuffer(buf, dtype=numpy.uint8).astype(numpy.float32)
            imgs = (imgs - (self.PIXEL_DEPTH / 2.0)) / self.PIXEL_DEPTH
            imgs = imgs.reshape(self.num_samples, self.IMAGE_SIZE, self.IMAGE_SIZE, 1)

        with gzip.open(self.lbl_file) as bytestream:
            bytestream.read(8)

            buf = bytestream.read(self.IMAGE_SIZE * self.IMAGE_SIZE * self.num_samples)
            lbls = numpy.frombuffer(buf, dtype=numpy.uint8).astype(numpy.float32)

        return imgs, lbls

    def next_batch(self, batch_size):
        last_index = min(self.num_samples, self.current_image + batch_size)
        imgs = self.imgs[self.current_image:last_index, :, :, 0]
        lbls = self.lbls[self.current_image:last_index]
        self.current_image = last_index
        if self.preprocessor is not None:
            imgs = self.preprocessor(imgs)
        return imgs, lbls

    def has_more(self):
        return self.current_image < self.num_samples

    def reset(self):
        self.current_image = 0

    def set_preprocessor(self, preprocessor):
        self.preprocessor = preprocessor
