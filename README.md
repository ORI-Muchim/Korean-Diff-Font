# Korean-Diff-Font

Official code implementation based on pytorch for paper, Diff-Font: Diffusion Model for Robust One-Shot Font Generation.  [Arvix](https://arxiv.org/pdf/2212.05895.pdf)


## Table of Contents 
- [Dependencies](#dependencies)
- [Datasets](#datasets)
- [Usage](#usage)
- [Inference](#inference)
- [FAQ](#faq)
- [References](#references)



## Dependencies

```python
pytorch>=1.10.0
tqdm
opencv-python
sklearn
pillow
tensorboardX
blobfile>=1.0.5
mpi4py
attrdict
yaml
```



## Datasets

[안심글꼴](https://gongu.copyright.or.kr/gongu/bbs/B0000018/list.do?menuNo=200195) I trained using the safe-font provided by the Korean Copyright Commission.

Example Directory:

```python
data_dir
    |--- id_0
    |--- id_1
           |--- 00000.png
           |--- 00001.png
           |--- ...
    |--- ...
```



## Usage

### Prepare datasets

```python
python font2img.py --ttf_path ./ttf_folder --chara total_kor.txt --save_path ./data_dir --img_size 128 --chara_size 100
```

### Conditional training

- Modify the configuration file cfg/train_cfg.yaml

  Key setting for conditional training:

  ```yaml
  data_dir: ''./data_dir/'
  chara_nums: 11172  # num of characters
  train_steps: 420000 # conditional training steps
  sty_encoder_path: './pretrained_models/korean_styenc.ckpt' # path to pre-trained style encoder
  model_save_dir: './trained_models' # path to save trained models
  stroke_path: './korean_stroke.txt' # encoded strokes
  classifier_free: False # False for conditional training
  resume_checkpoint: ""
  ```

- Then, Run:

  ```python
  python train.py --cfg_path cfg/train_cfg.yaml
  ```

### Fine-tuning

After conditional training , we suggest an additional fine-tuning step.

- Modify the configuration file cfg/train_cfg.yaml

  Key setting for fine-tuning:

  ```yaml
  data_dir: './data_dir/'
  chara_nums: 11172  # num of characters
  model_save_dir: './trained_models' # path to save trained models
  stroke_path: './korean_stroke.txt' # encoded strokes
  classifier_free: True  # True for fine-tuning
  total_train_steps: 800000 # total number of training steps for conditional training and fine-tuning
  resume_checkpoint: "./trained_models/model700000.pt" # path to conditional trained model, required for fine-tuning
  ```

- Then, Run:

  ```python
  python train.py --cfg_path cfg/train_cfg.yaml
  ```

### Inference

Modify the configuration file cfg/test_cfg.yaml

Key setting for testing:

```yaml
chara_nums: 11172
num_samples: 5 # Number of characters in ('./gen_char_kor.txt')
stroke_path: './korean_stroke.txt'
model_path: './trained_models/ema_0.9999_700000.pt'
sty_img_path: './1.png'
total_txt_file: './total_kor.txt'
gen_txt_file: './gen_char_kor.txt' # txt file for generation
img_save_path: './result' # path to save generated images
classifier_free: True 
cont_scale: 3.0 # content guidance sacle
sk_scale: 3.0 # stroke guidance sacle
```

Then, Run:

```python
python sample.py --cfg_path cfg/test_cfg.yaml
```



## FAQ

**1. The generated characters content are incorrect**.

Please check whether each font in the dataset used for training contains all characters in the '.txt ' file.

**2. The generated character images are unclear and structurally incomplete.**

This phenomenon indicates that the model training is not sufficient. Please continue to train the model.





# References

------

This project is based on [openai/guided-diffusion](https://github.com/openai/guided-diffusion) and [DG-Font](https://github.com/ecnuycxie/DG-Font).
