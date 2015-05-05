size = [128,128];
m = zeros(size);  % the simple matrix

period = [4,0];

for i = 1:size(1)
    for j = 1:size(2)
        m(i,j) = 128 + 128*cos(2*pi*period(1)*i/size(1))*cos(2*pi*period(2)*j/size(2));
    end
end

image = mat2gray(m);
imshow(image)
