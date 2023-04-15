#모델 학습 및 평가 시 사용되는 상수 및 데이터 딕셔너리를 정의
#이 파일을 import 하면 아래의 변수(BASE_DIR, IS_UBUNTU, EPS, DIC_CLS_BGR, DIC_CLS_RGB)들을 사용할 수 있게 됨.
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

IS_UBUNTU = False

EPS = np.finfo(float).eps

DIC_CLS_BGR = {
    'Sedan':[0,0,255],
    'Bus or Truck':[0,50,255],
    'Motorcycle':[0,255,0],
    'Bicycle':[0,200,255],
    'Pedestrian':[255,0,0],
    'Pedestrian Group':[255,0,100],
    'Bicycle Group':[255,100,0],
}

DIC_CLS_RGB = {
    'Sedan': [1, 0, 0],
    'Bus or Truck': [1, 0.2, 0],
    'Motorcycle': [0, 1, 0],
    'Bicycle': [1, 0.8, 0],
    'Pedestrian': [0, 0, 1],
    'Pedestrian Group': [0.4, 0, 1],
    'Bicycle Group': [0, 0.8, 1],
}

if __name__ == '__main__':
    print(BASE_DIR)
    print(EPS)
