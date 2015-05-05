# Generate cosine image with given periods in x and y direction
import numpy, pylab, scipy, Image, matplotlib.cm as cm
from scipy.misc import toimage

periodsx = 4.
periodsy = 0.

image_dimensions = [128., 128.]

image = numpy.zeros(image_dimensions, dtype=numpy.uint8)

for i in range(0, int(image_dimensions[0])):
  for j in range(0, int(image_dimensions[1])):
    image[i,j] = 128 + 128*numpy.cos(2*periodsx*numpy.pi*i/image_dimensions[0])*numpy.sin(2*numpy.cos(2*periodsy*numpy.pi*j/image_dimensions[1]))

f = numpy.fft.fft2(image)
psd = numpy.abs(numpy.fft.fftshift(f))
# psd = Image.fromarray(psd)
psd = toimage(psd)

# im = Image.fromarray(image)
im = toimage(image)
psd.save('./images/ft_python.jpg')

# fileName = raw_input("Enter filename to save as: ")
# im.save(fileName)
im.save('./images/40_python.jpg')

pylab.figure()
pylab.imshow(im,  cmap = cm.Greys_r)	# display the image

pylab.figure()
pylab.imshow(psd, cmap = cm.Greys_r)	# display the FT of the image

pylab.show()

