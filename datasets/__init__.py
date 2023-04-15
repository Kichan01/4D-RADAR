from .kradar_detection_v1_0 import KRadarDetection_v1_0
# from .kradar_detection_v1_1 import KRadarDetection_v1_1
#all 변수를 설정하여 모듈 외부에서 "KRadarDetection_v1_0" 클래스에 직접적으로 접근할 수 있도록 설정
__all__ = {
    'KRadarDetection_v1_0': KRadarDetection_v1_0,
    # 'KRadarDetection_v1_1': KRadarDetection_v1_1,
}
