import os
from get_trained_models import get_model
from edit_yaml import get_char_count, update_yaml_config

# get_trained_models
get_model()


# edit yaml
char_count = get_char_count('./gen_char_kor.txt')
config_data = {
    'dropout': 0.1,
    'chara_nums': 11172,
    'diffusion_steps': 1000,
    'noise_schedule': 'linear',
    'image_size': 128,
    'num_channels': 128,
    'num_res_blocks': 3,
    'batch_size': char_count,
    'num_samples': char_count,
    'attention_resolutions': '40, 20, 10',
    'use_ddim': True,
    'timestep_respacing': 'ddim25',
    'stroke_path': './korean_stroke.txt',
    'model_path': './trained_models/ema_0.9999_800000.pt',
    'sty_img_path': './1.png',
    'total_txt_file': './total_kor.txt',
    'gen_txt_file': './gen_char_kor.txt',
    'img_save_path': './result',
    'classifier_free': True,
    'cont_scale': 3.0,
    'sk_scale': 3.0
}
file_path = './cfg/test_cfg.yaml'
update_yaml_config(file_path, config_data)


# Inference
os.system("python sample.py --cfg_path cfg/test_cfg.yaml")
