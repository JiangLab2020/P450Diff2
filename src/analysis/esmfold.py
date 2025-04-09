import argparse
import os

import biotite.structure.io as bsio
import esm
import torch

# Load ESM-Fold model
model = esm.pretrained.esmfold_v1()
model = model.eval().cuda()
parser = argparse.ArgumentParser()
parser.add_argument("--input_file", required=True, help="input file path")
parser.add_argument("--output_path", required=True, help="output path")
args = parser.parse_args()
# Path to input FASTA file and output directory
fasta_file = args.input_file
output_dir = args.output_path

# Create output directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

# Read sequences from FASTA file
with open(fasta_file, "r") as f:
    fasta_content = f.read().strip().split(">")[1:]

# Create a list to store RMSD and pLDDT results
results = []

# Iterate over sequences
for entry in fasta_content:
    lines = entry.strip().split("\n")
    seq_id = lines[0].strip()
    sequence = "".join(lines[1:])

    # Perform structure inference
    with torch.no_grad():
        output = model.infer_pdb(sequence)

    # Write output structure to PDB file
    pdb_filename = os.path.join(output_dir, f"{seq_id}.pdb")
    with open(pdb_filename, "w") as f:
        f.write(output)

    # Load structure and compute mean B factor (pLDDT)
    struct = bsio.load_structure(pdb_filename, extra_fields=["b_factor"])
    plddt = struct.b_factor.mean()

    # Append results
    results.append((seq_id, plddt))

# Write RMSD and pLDDT results to a text file
result_filename = os.path.join(output_dir, "results.txt")
with open(result_filename, "w") as f:
    f.write("Sequence ID\t pLDDT\n")
    for result in results:
        f.write(f"{result[0]}\t {result[1]:.4f}\n")

print(f"results saved to: {result_filename}")
