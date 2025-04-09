import os

from Bio import SeqIO

# BUG DONOT HAVE 6
fasta_files = [
    "data/DMs/fine-tune/generated_samples_string_0.fasta",
    "data/DMs/fine-tune/generated_samples_string_1.fasta",
    "data/DMs/fine-tune/generated_samples_string_2.fasta",
    "data/DMs/fine-tune/generated_samples_string_3.fasta",
    "data/DMs/fine-tune/generated_samples_string_4.fasta",
    "data/DMs/fine-tune/generated_samples_string_5.fasta",
    "data/DMs/fine-tune/generated_samples_string_6.fasta",
    "data/DMs/fine-tune/generated_samples_string_7.fasta",
]


output_file = "data/DMs/fine-tune/merged.fasta"


all_seqs = []

for file_path in fasta_files:
    filename = os.path.splitext(os.path.basename(file_path))[0]
    for record in SeqIO.parse(file_path, "fasta"):
        record.id = f"{filename}_{record.id}"
        all_seqs.append(record)


SeqIO.write(all_seqs, output_file, "fasta")
