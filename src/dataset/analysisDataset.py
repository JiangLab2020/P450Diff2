# to analyze the dataset sequence length distribution
import matplotlib.pyplot as plt
from Bio import SeqIO

# 读取FASTA文件
# fasta_file = "data/DMs/p450/consensus.fasta"
# fasta_file = "data/others/generate/1.fasta"
fasta_file = "data/DMs/fine-tune/merged.fasta"

seq_lengths = [len(record.seq) for record in SeqIO.parse(fasta_file, "fasta")]

# 画直方图
plt.figure(figsize=(8, 6))
plt.hist(seq_lengths, bins=20, edgecolor="black", alpha=0.7)
plt.xlabel("Sequence Length")
plt.ylabel("Frequency")
plt.title("Histogram of Sequence Lengths")
plt.grid(axis="y", linestyle="--", alpha=0.6)
# plt.savefig(
#     "data/DMs/fine-tune/sequence_length_histogram.png", dpi=300, bbox_inches="tight"
# )
plt.savefig(
    "data/DMs/fine-tune/sequence_length_histogram.png", dpi=300, bbox_inches="tight"
)
# 显示图表
plt.show()
