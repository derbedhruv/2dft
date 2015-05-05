# view the ft of an image
import numpy, pylab, matplotlib.cm as cm, Image
from scipy.misc import toimage

fileName = "./images/40.jpg"

image = Image.open(fileName).convert("L")

im = numpy.array(image, dtype=numpy.uint8)
f = numpy.fft.fftshift(numpy.fft.fft2(im))
p = numpy.abs(f)

psd = toimage(p, mode='P')

pylab.figure()
pylab.imshow(psd)
pylab.show()
