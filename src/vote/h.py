a = ''.join(choice(ascii_letters) for i in range(8))
b = ''.join(choice(ascii_letters) for i in range(8))
c = ''.join(choice(ascii_letters) for i in range(8))
d = ''.join(choice(ascii_letters) for i in range(8))
e = a + ' ' + b + ' ' + c + ' ' + d
img_bw = np.ones([350, 350], dtype=np.uint8) * 255
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img_bw, a, (20, 75), font, 2, (0, 0, 0), 5, cv2.LINE_AA)
cv2.putText(img_bw, b, (20, 150), font, 2, (0, 0, 0), 5, cv2.LINE_AA)
cv2.putText(img_bw, c, (20, 225), font, 2, (0, 0, 0), 5, cv2.LINE_AA)
cv2.putText(img_bw, d, (20, 300), font, 2, (0, 0, 0), 5, cv2.LINE_AA)
image = Image.fromarray(img_bw)
outfile = Image.new('1', outfile1.size)
for x in range(outfile1.size[0]):
    for y in range(outfile1.size[1]):
        outfile.putpixel((x, y), max(outfile1.getpixel((x, y)), outfile2.getpixel((x, y))))

outfile.show()
