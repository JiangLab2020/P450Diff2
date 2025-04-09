#!/bin/bash
#SBATCH --job-name=train    # 作业名称
#SBATCH --output=dev/output.txt       # 标准输出文件
#SBATCH --error=dev/error.txt         # 标准错误输出文件
#SBATCH --cpus-per-task=10        # 每个任务使用的 CPU 核心数
#SBATCH --partition=qgpu_a40     # 提交到的分区
#SBATCH --gres=gpu:3
#SBATCH --mem=20G

python src/train.py src/config/config640Mp450.json data/model/fineTune --pretrained  --gpus 3 --warmup --final_norm --model_size 640M --checkpoint_freq 5 --note 1e-10 | tee dev/train.logs