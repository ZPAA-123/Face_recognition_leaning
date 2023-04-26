# 导入cv模块
import cv2 as cv
# 读取图片
img = cv.imread('face1.jpg')

#坐标
x,y,w,h = 100,100,100,100
#绘制矩形
cv.rectangle(img,(x,y,x+w,y+h),color=(0,255,0),thickness=2)
#绘制圆形
cv.circle(img,center=(x+w,y+h),radius=100,color=(255,0,0),thickness=1)
# 显示
cv.imshow('img',img)

# 等待   函数里面填的0表示数字达到0时就会结束函数  。但是0是永远都达不到的，所以就会一直运行下去
# 增加一个判断来判断是否退出
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内存
cv.destroyAllWindows()
