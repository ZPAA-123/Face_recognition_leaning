import os
import cv2
from PIL import Image
import numpy as np

def getImageAndLabels(path):
    #储存人脸数据
    faceSamples=[]
    #储存姓名数据
    ids=[]
    #储存图片信息
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    #加载分类器
    face_detector = cv2.CascadeClassifier('F:/opencv/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')
    #b遍历列表中的图片
    for imagePath in imagePaths:
        #打开图片，灰度化，PIL有九种不同的模式：1，L，P，RGB，RGBA，CMYK，YCbCr，I，F
        PIL_img = Image.open(imagePath).convert('L')
        #将图像转为数组，并且以黑白深浅
        img_numpy = np.array(PIL_img,'uint8')
        #获取图片人脸特征
        faces = face_detector.detectMultiScale(img_numpy)
        #获取每张图片的id和姓名
        id = int(os.path.split(imagePath)[1].split('.')[0])
        #预防无面容图片
        for x,y,w,h in faces:
            ids,append(id)
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            #打印面部特征和id
            print('id:',id)
            print('fs',faceSamples)
            return faceSamples,ids

if __name__ == '__main__':
    #图片路径
    path = 'asdjka'
    #获取图像数组和id标签数组和名字
    face,ids = getImageAndLabels(path)
    #加载识别器
    recognizer = cv2.face.LBHFaceRecognizer_create()
    #训练
    recognizer.train(faces,np.array(ids))
    #保存文件
    recognizer.write('trainer/trainer.yml')
