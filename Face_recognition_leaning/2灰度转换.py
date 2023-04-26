# 导入cv模块
import cv2 as cv
# 读取图片
img = cv.imread('face1.jpg')

#灰度转换    (只显示灰度信息，后面的信息可以显示其他的颜色模式)
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 显示灰度图片
cv.imshow('gray',gray_img)
# 保存灰度图片
cv.imwrite('gray_face1.jpg',gray_img)


# 显示图片
cv.imshow('read_img',img)
# 等待   函数里面填的0表示数字达到0时就会结束函数  。但是0是永远都达不到的，所以就会一直运行下去
cv.waitKey(0)
# 释放内存
cv.destroyAllWindows()
