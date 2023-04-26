 # 导入cv模块
import cv2 as cv

#定义检测函数
def face_detect_demo(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #添加面部的opencv自带的分类器
    face_detect = cv.CascadeClassifier('F:/opencv/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
#    face = face_detect.detectMultScale(gray,1.01,5,(100,100),(300,300)) 选择的图像，每次缩放大小，确定的次数，最小人脸，最大人脸
    face = face_detect.detectMultiScale(gray,1.1)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=1)
    cv.imshow('result',img)


# 读取图片
img = cv.imread('face1.jpg')

face_detect_demo(img)




# 等待   函数里面填的0表示数字达到0时就会结束函数  。但是0是永远都达不到的，所以就会一直运行下去
# 增加一个判断来判断是否退出
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内存
cv.destroyAllWindows()
