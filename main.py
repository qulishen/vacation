import cv2
###视频灰度处理
#
# vc = cv2.VideoCapture('test.mp4')  //参数为零即打开摄像头
# if vc.isOpened():
#     open, frame = vc.read()
# while open:
#     ret, frame = vc.read()
#     if frame is None:
#         break
#     if ret == True:
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imshow('result', gray)
#         if cv2.waitKey(1) & 0xFF == 27:
#             break
# vc.release()
# cv2.destroyAllWindows()

###截取部分图像
def cv_show(img):
    cv2.imshow('cat', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return
img=cv2.imread('shuangpin.jpg')
# cat=img[0:200,0:200]
# cv_show(cat)

##颜色通道提取
b,g,r=cv2.split(img)
img2=cv2.merge((b,g,r))
cv_show(img2)
