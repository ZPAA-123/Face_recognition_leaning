 # 导入cv模块
import cv2 as cv

#定义摄像头
cap = cv.VideoCapture(0)

falg = 1
num = 1
#检测是否处于开启状态
while(cap.isOpened()):
    #得到每一帧的图像
    ret_flag,Vshow = cap.read()
    #显示图像
    cv.imshow('capture_test',Vshow)
    #按键的判断
    k = cv.waitKey(1) & 0xFF
    #保存图片
    if k == ord('s'):
        cv.imwrite("C:/Users/14019/Desktop/工程文件/Facefice/src/"+str(num)+"name"+".jpg",Vshow)
        print("success to save"+str(num)+".jpg")
        num += 1
    elif k == ord(' '):
        break


#释放摄像头
cap.release()
# 释放内存
cv.destroyAllWindows()
