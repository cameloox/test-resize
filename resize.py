import cv2, glob

print("Hello World!")
images=glob.glob("image2.jpg")

for image in images:
	img=cv2.imread(image, 1)

	re=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("image resize",re)

cv2.waitKey(500)


cv2.imwrite("result"+image, re)
