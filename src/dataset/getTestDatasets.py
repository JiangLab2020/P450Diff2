import json
import random

from Bio import SeqIO

FASTA_PATH = "data/DMs/p450/consensus.fasta"
JSON_PATH = "data/DMs/p450/splits.json"
OUTPUT_PATH = "data/DMs/p450/filtered_test_sequences.fasta"

# 读取FASTA所有序列
all_sequences = list(SeqIO.parse(FASTA_PATH, "fasta"))

# 读取JSON
with open(JSON_PATH, "r") as f:
    splits = json.load(f)

# 获取rtest索引（这些是第几条序列的编号，从0开始）
rtest_indices = splits.get("rtest", [])

# 从rtest中选出长度在450-550之间的序列
filtered_sequences = [
    all_sequences[i] for i in rtest_indices if 450 <= len(all_sequences[i].seq) <= 550
]

# 检查是否足够12800条
if len(filtered_sequences) < 12800:
    raise ValueError(f"只有 {len(filtered_sequences)} 条符合条件的序列，不足12800。")

# 随机采样12800条
selected_sequences = random.sample(filtered_sequences, 12800)

# 保存结果到新的FASTA
SeqIO.write(selected_sequences, OUTPUT_PATH, "fasta")
print(f"保存了 {len(selected_sequences)} 条序列到 {OUTPUT_PATH}")
