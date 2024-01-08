import imageio as iio 
files = ["ImageAsset/painter0.jpg", "ImageAsset/painter01.jpg", "ImageAsset/painter02.jpg", "ImageAsset/painter.jpg"]
images = []
for file in files:
    images.append(iio.imread(file))
iio.mimsave('ImageAsset/mygif2.gif', images, format='GIF',duration=4)