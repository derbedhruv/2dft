# view the ft of an image
import numpy, pylab, matplotlib.cm, Image

fileName = "./images/40_python.jpg"

image = Image.open(fileName).convert("L")

im = numpy.array(image, dtype=numpy.uint8)
f = numpy.fft.fftshift(numpy.fft.fft2(im))
p = numpy.abs(f)

psd = Image.fromarray(p)

pylab.figure()
pylab.imshow(psd)
pylab.show()
