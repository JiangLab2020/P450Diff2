import numpy as np

data = np.load("lengths_and_offsets.npz")

print("Keys in the .npz file:", data.files)

name_offsets = data['name_offsets']
seq_offsets = data['seq_offsets']
ells = data['ells']


print(name_offsets)
print(seq_offsets)
print(ells)

print(len(name_offsets))
print(len(seq_offsets))
print(len(ells))

data = np.load("consensus.npz")

print("Keys in the .npz file:", data.files)

name_offsets = data['name_offsets']
seq_offsets = data['seq_offsets']
ells = data['ells']


print(name_offsets)
print(seq_offsets)
print(ells)

print(len(name_offsets))
print(len(seq_offsets))
print(len(ells))
