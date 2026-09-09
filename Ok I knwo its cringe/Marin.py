import imageio.v3 as iio
filenames = ['Image 1.png', 'Image 2.png', 'Image 3.png', 'Image 4.png']
images =[ ]
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('Kitagawa.gif', images, duration=350, loop=0)
                