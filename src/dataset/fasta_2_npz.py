import json
import random
import sys

import numpy as np
from Bio import SeqIO

fasta_file = sys.argv[1]  # 输入FASTA文件
# 去除文件名 使用路径读取
out_path = sys.argv[1].split("/")[:-1]
out_path = "/".join(out_path)

# 初始化列表来存储每个序列的名称偏移、序列偏移和长度
name_offsets = []
seq_offsets = []
lengths = []

npz_file = out_path + "/lengths_and_offsets.npz"  # 输出npz文件

offset = 0  # 初始化偏移量

# 逐个序列读取
with open(fasta_file, "r") as file:
    for record in SeqIO.parse(file, "fasta"):
        # 记录每个序列名称的偏移
        name_offsets.append(offset)
        # 将偏移更新为下一个序列的开始位置
        offset += len(record.description) + 1  # 名称行的长度（包括“>”）
        offset += 1
        # 记录该序列内容的偏移和长度
        seq_offsets.append(offset)
        lengths.append(len(record.seq))

        # 更新偏移量：包含序列的长度加上换行符的长度
        offset += len(record.seq) + 1

# 将数据存入npz文件
np.savez_compressed(
    npz_file, name_offsets=name_offsets, seq_offsets=seq_offsets, ells=lengths
)

print(
    f"Generated {npz_file} with name_offsets, seq_offsets, and lengths (ells) arrays."
)


output_json_path = out_path + "/splits.json"  # 输出JSON文件路径

# 读入序列
sequences = list(SeqIO.parse(fasta_file, "fasta"))

total_sequences = len(sequences)

# 创建序号列表
sequence_indices = list(range(total_sequences))

# 计算每个数据集的大小
train_size = int(total_sequences * 0.90)
test_size = int(total_sequences * 0.05)
val_size = total_sequences - train_size - test_size

# 随机抽取测试集和验证集的索引
test_indices = sorted(random.sample(sequence_indices, test_size))
remaining_indices = list(set(sequence_indices) - set(test_indices))
val_indices = sorted(random.sample(remaining_indices, val_size))
train_indices = list(set(remaining_indices) - set(val_indices))

# 构建 JSON 格式的数据集
splits = {"train": train_indices, "rtest": test_indices, "valid": val_indices}

# 保存到 JSON 文件
with open(output_json_path, "w") as json_file:
    json.dump(splits, json_file, indent=2)

print(
    f"splits.json has been saved with {train_size} training, {test_size} test, and {val_size} validation sequences."
)
