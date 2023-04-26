 # 导入cv模块
import cv2 as cv

#定义图片检测函数
def face_detect_demo(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #添加面部的opencv自带的分类器
    face_detect = cv.CascadeClassifier('F:/opencv/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
#    face = face_detect.detectMultScale(gray,1.01,5,(100,100),(300,300)) 选择的图像，每次缩放大小，确定的次数，最小人脸，最大人脸
    face = face_detect.detectMultiScale(gray,1.1)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=1)
    cv.imshow('result',img)


#读取摄像头   VideoCapture()里面的数字不同代表读取不同的摄像头
# cap = cv.VideoCapture(0)
#在里面添加视频地址时就会读取视频
cap = cv.VideoCapture('1.flv')

#循环读取关键帧,并且识别每一帧的图像
while True:
    flag,kframe = cap.read()
    if not flag:
        break
    face_detect_demo(kframe)
    if ord('q') == cv.waitKey(0):
        break


# 释放内存
cv.destroyAllWindows()
#释放摄像头
cap.release()