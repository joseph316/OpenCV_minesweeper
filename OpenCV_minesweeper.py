
import numpy as np
import cv2 #openCV package

#print(cv2.__version__)

def handle_image():
    #이미지 읽어오기
    imgfile = 'magic.jpg'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR) #사진을 컬러로 읽어오기 

    #이미지 화면에 출력
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2_imshow(img)

    #이미지 저장
    cv2.imwrite('magic2.jpg',img)

#함수 실행
if __name__ == '__main__':
    handle_image()