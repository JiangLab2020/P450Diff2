# P450Diff2: A diffusion model-based method for generating P450 enzyme sequences
# Contents
- [P450Diff2: A diffusion model-based method for generating P450 enzyme sequences](#p450diff2-a-diffusion-model-based-method-for-generating-p450-enzyme-sequences)
- [Contents](#contents)
- [Introduction](#introduction)
- [Usage](#usage)
  - [train](#train)
    - [init](#init)
    - [train](#train-1)
    - [generate](#generate)
- [Install](#install)

# Introduction
Cytochrome P450 enzymes represent the largest superfamily of oxidoreductases in nature, playing pivotal roles in drug metabolism, plant secondary metabolism, and the biotransformation of environmental pollutants. In this study, we propose P450Diff2, a novel P450 sequence generation method based on a diffusion framework. The model is built upon the EvoDiff-Seq architecture, comprising 640 million parameters, and is trained on a comprehensive dataset of 1,041,254 non-redundant P450 protein sequences curated from NCBI, Gmind annotations, RNA-Seq assemblies, and metagenomic databases. P450Diff2 is designed to generate synthetic P450 enzyme sequences with high fidelity and diversity. During training, the model exhibited a continuous decline in loss and steady improvements in accuracy, ultimately reaching convergence. Sequence generation using the trained model was evaluated across multiple dimensions, including amino acid composition, sequence feature space, similarity distribution, and structural plausibility. Results demonstrate that P450Diff2 outperforms the previously proposed P450Diffusion model across all metrics. Notably, the generated sequences achieved an average pLDDT score of 72, indicating that the method not only preserves key characteristics of natural sequences but also exhibits strong generative capabilities and promising structural reliability.
# Usage
## train
### init
```bash
conda activate evodiff
```
### train
```bash
CUDA_VISIBLE_DEVICES=1,2,3,4,5,6 python src/train.py src/config/config640Mp450.json data/model/fineTune --pretrained  --gpus 6 --warmup --final_norm --model_size 640M --checkpoint_freq 5 | tee dev/train.log
```
### generate
```bash
python src/evodiff/generate.py --num-seqs 1600 --seed 0 --seq_len 500
```
# Install
```bash
conda create --name evodiff python=3.9
pip install torch==2.1 torchvision torchaudio
pip install torch-scatter -f https://data.pyg.org/whl/torch-2.1.0+cu121.html
pip install torch_geometric
pip install sequence-models
pip install pandas
pip install biopython
pip install fair-esm
pip install matplotlib
pip install seaborn
pip install lmdb
pip install scipy
pip install scikit-learn
pip install numpy==1.26
pip install tensorboard
```