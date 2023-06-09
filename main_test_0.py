'''
* Copyright (c) AVELab, KAIST. All rights reserved.
* author: Donghee Paek & Kevin Tirta Wijaya, AVELab, KAIST
* e-mail: donghee.paek@kaist.ac.kr, kevin.tirta@kaist.ac.kr
'''

import os
os.environ['CUDA_VISIBLE_DEVICES'] = '1'

EXP_NAME = 'exp_230106_103233_RTNH'
MODEL_EPOCH = 10
SAMPLE_INDICES = [30,70]
CONFIDENCE_THR = 0.55

from pipelines.pipeline_detection_v1_0 import PipelineDetection_v1_0 #import file 

if __name__ == '__main__':
    PATH_CONFIG = './logs/' + EXP_NAME + '/config.yml' #변수 path 지정
    PATH_MODEL = './logs/' + EXP_NAME + f'/models/model_{MODEL_EPOCH}.pt' #model path 지정

    pline = PipelineDetection_v1_0(PATH_CONFIG, mode='vis')
    pline.load_dict_model(PATH_MODEL) #딕셔너리 파일 load하여 모델 초기화
    pline.vis_infer(sample_indices=SAMPLE_INDICES, conf_thr=CONFIDENCE_THR) #시각화 추론 후 결과 시각화
    
