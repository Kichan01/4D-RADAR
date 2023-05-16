'''
* Copyright (c) AVELab, KAIST. All rights reserved.
* author: Donghee Paek & Kevin Tirta Wijaya, AVELab, KAIST
* e-mail: donghee.paek@kaist.ac.kr, kevin.tirta@kaist.ac.kr
'''

import os
os.environ['CUDA_VISIBLE_DEVICES']= '0'

from pipelines.pipeline_detection_v1_0 import PipelineDetection_v1_0

PATH_CONFIG = './configs/cfg_RTNH.yml'

if __name__ == '__main__':
    pline = PipelineDetection_v1_0(path_cfg=PATH_CONFIG, mode='train')

    ### Save this file for checking ###
    import shutil
    shutil.copy2(os.path.realpath(__file__), os.path.join(pline.path_log, 'executed_code.txt'))
    #현재 스크립트 파일의 절대경로 복사. executed_code.txt라는 이름으로 pline.path_log 디렉터리로 복사.
    ### Save this file for checking ###

    pline.train_network()

    # conditional evaluation for last epoch
    pline.validate_kitti_conditional(list_conf_thr=[0.3], is_subset=False, is_print_memory=False)
    
