import math
import os

from Bio import SeqIO


def split_fasta(input_fasta, n, output_dir):
    # 读取FASTA文件中的所有序列
    records = list(SeqIO.parse(input_fasta, "fasta"))
    total_records = len(records)

    # 计算每个子文件应包含的序列数
    records_per_file = math.ceil(total_records / n)

    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 分割并写入子FASTA文件
    for i in range(n):
        start_idx = i * records_per_file
        end_idx = min((i + 1) * records_per_file, total_records)

        if start_idx >= total_records:
            break  # 防止空文件

        output_file = os.path.join(output_dir, f"split_{i + 1}.fasta")
        with open(output_file, "w") as out_handle:
            SeqIO.write(records[start_idx:end_idx], out_handle, "fasta")

        print(f"Written: {output_file} ({end_idx - start_idx} sequences)")


# 使用示例
split_fasta(
    "data/DMs/p450/filtered_test_sequences.fasta",
    8,
    "data/DMs/p450/4test/",
)
