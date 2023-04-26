# 导入cv模块
import cv2 as cv
# 读取图片
img = cv.imread('face1.jpg')

# 修改尺寸
resize_img = cv.resize(img,dsize=(250,250))\
# 显示原图
cv.imshow('img',img)
# 显示修改后的
cv.imshow('resize_img',resize_img)
# 打印原图的大小和修改后的大小
print('未修改',img.shape)
print('已修改',resize_img.shape)


# 等待   函数里面填的0表示数字达到0时就会结束函数  。但是0是永远都达不到的，所以就会一直运行下去
# 增加一个判断来判断是否退出
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内存
cv.destroyAllWindows()
