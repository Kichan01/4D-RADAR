#프로그램 설정값 저장

# Library
import os.path as osp

# User Library
from configs.config_general import BASE_DIR, IS_UBUNTU

# Calibration
# Default Calibration Values: Translation -> Rotation / Lidar -> Radar: Reference is Radar
CALIB = [-2.54, 0.3, 0.] # [m, m, deg] # sequence 25, 레이더와 레이다간의 보정값 저장.
# CALIB = [-2.54, 0., 0.] # [m, m, deg]

# Split
if IS_UBUNTU:
    SPLITTER = '/' # Ubuntu, 우분투의 파일 경로 구분자(/or\) 저장
else:
    SPLITTER = '\\' # Window

# Delay
DELAY_FRAME = 0 #frame간의 delay

# State Global
SG_NORMAL = 0 
SG_START_LABELING = 1

# State Local
# Labeling Box 라벨링 작업시 사용되는 박스 설정(자율주행 관련 데이터를 시각화하고 라벨링하기 위해)
SL_START_LABELING = 0
SL_CLICK_CENTER = 1
SL_CLICK_FRONT = 2
SL_END_LABELING = 3

# Path
# PATH_SEQ = None
#radar 데이터 경로 저장
PATH_SEQ = 'E:\\radar_bin_lidar_bag_files\\generated_files'

PATH_IMG_G = osp.join(BASE_DIR, 'resources', 'imgs', 'prevg.png') #위
PATH_IMG_L = osp.join(BASE_DIR, 'resources', 'imgs', 'prevl.png') #왼

PATH_IMG_F = osp.join(BASE_DIR, 'resources', 'imgs', 'prevf.png') #앞
PATH_IMG_B = osp.join(BASE_DIR, 'resources', 'imgs', 'prevb.png') #뒤뒤

# Font
FONT = 'Times New Roman'
FONT_SIZE = 10

# Image Size 카메라 이미지 크기 저장
W_BEV = 1280 #가로
H_BEV = 800 #세로
W_CAM = 320 #카메라 이미지의 가로
H_CAM = 240 #카메라 이미지의 세로

# Button Type
BT_LEFT = 0
BT_RIGHT = 1
BT_MIDDLE = 2

RANGE_Z = [-3, 3] # [m]

# Class
LIST_CLS_NAME = [
    'Sedan',
    'Bus or Truck',
    'Motorcycle',
    'Bicycle',
    'Pedestrian',
    'Pedestrian Group',
    'Bicycle Group',
]

# BGR
# 객체 클래스별 색상 지정
LIST_CLS_COLOR = [
    [0,255,0],
    [0,50,255],
    [0,0,255],
    [0,200,255],
    [255,0,0],
    [255,0,100],
    [255,200,0],
]
#객체 클래스별 높이중심과 길이 범위 저장
LIST_Z_CEN_LEN = [
    [-1.5,0.95],
    [-1.5,1.5],
    [-1.5,1.5],
    [-1.5,1.5],
    [-1.5,1.5],
    [-1.5,1.5],
    [-1.5,1.5],
]

# Drawing
LINE_WIDTH = 2

# Front & Beside Image
#생성되는 이미지에서 x축,y축 방향으로 표시될 좌표 범위를 지정하는 변수
RANGE_Y_FRONT = [-4,4]  # [m]
RANGE_Z_FRONT = [-8,8]  # [m]
IMG_SIZE_YZ = [300,150] # [pixel]
M_PER_PIX_YZ = 16./300.

RANGE_X_FRONT = [-8,8]  # [m]
RANGE_Z_FRONT = [-8,8]  # [m]
IMG_SIZE_XZ = [300,300] # [pxiel]
M_PER_PIX_XZ = 16./300.
