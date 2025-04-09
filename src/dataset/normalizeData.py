from Bio import SeqIO

input_fasta = "data/DMs/p450/P450_All_v2_100_LenCut280_Merge90.pep"
output_fasta = "data/DMs/p450/consensus.fasta"

AA = "ACDEFGHIKLMNPQRSTVWY"

sequences = SeqIO.parse(input_fasta, "fasta")
with open(output_fasta, "w") as output_handle:
    for record in sequences:
        record.seq = record.seq.replace("*", "")
        if any(aa not in AA for aa in record.seq):
            print(record.id)
            print(record.seq)
            print()
            continue
        record.description = ""
        output_handle.write(f">{record.id}\n{str(record.seq)}\n")

print(f"Processed sequences written to {output_fasta}")
