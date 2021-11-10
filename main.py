import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import importlib
importlib.reload(sys)
import pickle

def check_is_vague(image):
    """
    检查照片是否模糊 使用Laplacian算法，当出现椒盐噪声，需要我们先进行滤波处理
    :param image: 地址
    :param threshold: 阈值
    :return: Ture or False
    """
    #start = time.time()
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #转化为灰度图像
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()
    #print('image vague is {}'.format(fm), end = " ")
    #elapsed = (time.time() - start)
    #print("time used:", elapsed, end = " ")
    if fm <= 30:
        return True #模糊
    return False

def check_is_dark(image):
    """
    判断图像是否是偏暗，设置阈值为0.78，我们计算偏暗的像素个数，再除于像素总个数得到百分比
    :param image:
    :param threshold:
    :return:
    """
    #start = time.time()
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    r,c = gray.shape[:2]
    dark_sum = 0
    dark_prop = 0
    piexs_sum = r * c
    
    dark_points = (gray < 40)
    target_array = gray[dark_points]
    dark_sum = target_array.size
    
    dark_prop = dark_sum / (piexs_sum)
    #print('image dark is {}'.format(dark_prop), end = " ")
    #elapsed = (time.time() - start)
    #print("time used:", elapsed, end = " ")
    if dark_prop >= 0.78:
        return True #确认为偏暗图像
    return False

def check_is_exposure(image):
    """
    判定图像是否过度曝光，首先将图像转为灰度直方图图，过度曝光的图片的灰度直方图大多集中于左侧
    :param image:
    :param threshold:
    :return:
    """
    #start = time.time()
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ######绘制回灰度直方图
    """
    image_ravel = img.ravel()
    plt.hist(image_ravel, 256, [0, 256])
    plt.show()
    """
    ###############
    r,c = gray.shape[:2]
    whith_sum = 0
    whith_prop = 0
    piexs_sum = r * c

    whith_points = (gray > 220)
    target_array = gray[whith_points]
    whith_sum = target_array.size
    
    whith_prop = whith_sum / piexs_sum
    #print('image exposure is {}'.format(whith_prop))
    #elapsed = (time.time() - start)
    #print("time used:", elapsed, end = " ")
    if whith_prop >= 0.5:
        return True #认定为过度曝光图像
    return False

def check_is_all(image):
    """
    :param image:
    :return: 判断是否完全满足
    """
    #start = time.time()
    img = cv2.imread(image)
    # 转化为灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 判断模糊
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()

    # 判断过暗 判断过曝
    r, c = gray.shape[:2]
    dark_sum = 0
    dark_prop = 0

    whith_sum = 0
    whith_prop = 0
    piexs_sum = r * c
    
    #dark_prop = dark_sum / piexs_sum
    #whith_prop = whith_sum / piexs_sum
    #elapsed = (time.time() - strat)
    #print("used time:", elapsed, end = " ")
    if (fm <= 30 or (dark_sum / piexs_sum) >= 0.78 or (whith_sum / piexs_sum) >= 0.5):
        print(1)
    else:
        print(0)

def test(image):
   if (check_is_vague(image) or check_is_dark(image) or check_is_exposure(image)):
       print(1)
   else:
       print(0)

if __name__ == '__main__':
    """
    fileList = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg', '20.jpg', '21.jpg', '22.jpg', '23.jpg', '24.jpg', '25.jpg', '26.jpg', '27.jpg', '28.jpg', '29.jpg', '30.jpg', '31.jpg', '32.jpg', '33.jpg', '34.jpg', '35.jpg', '36.jpg', '37.jpg', '38.jpg', '39.jpg', '40.jpg', '41.jpg', '42.jpg', '43.jpg', '44.jpg', '45.jpg', '46.jpg', '47.jpg', '48.jpg', '49.jpg', '50.jpg', '51.jpg', '52.jpg', '53.jpg', '54.jpg', '55.jpg', '56.jpg', '57.jpg', '58.jpg', '59.jpg', '60.jpg', '61.jpg', '62.jpg', '63.jpg']
    i = 0
    for f in fileList:
        print(i, end=" ")
        i += 1
        check_is_vague(f)
        check_is_exposure(f)
        check_is_dark(f)
    """

    image = "E:\\Picture\\15.jpg"
    #image = "tes.png"
    #Linux路径
    #image = "/home/user922/basa.JPG"
    #image = "/home/ElectriBox/Sever/picture/less.jpg"
    #check_is_all(image)

    
    if (check_is_vague(image)):
        print(0)
    else:
        print(1)

    if (check_is_dark(image)):
        print(0)
    else:
        print(1)

    if (check_is_exposure(image)):
        print(0)
    else:
        print(1)


#test(sys.argv[1])





