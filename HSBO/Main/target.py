import pandas as pd
import numpy as np

# warezmaster, warezclient, ftp_write, guess_passwd, imap, multihop, phf, spy - R2L attack
# teardrop, smurf, back, land, neptune, pod   - Dos
# ipsweep, portsweep, satan, nmap - Probe
# buffer_overflow, loadmodule, perl, rootkit - U2R

Data = pd.read_csv("Dataset/KDDTrain+.csv", header=None)
Data = np.array(Data)

label_colum = Data[:, -2]       # target data

print(np.unique(label_colum))

R2L = ["warezmaster", "warezclient", "ftp_write", "guess_passwd", "imap", 'multihop', "phf", 'spy']
Dos = ["teardrop", "smurf", 'back', 'land', 'neptune', 'pod']
Probe = ["ipsweep", "portsweep", "satan", "nmap"]
U2R = ["buffer_overflow", "loadmodule", 'perl', "rootkit"]

Label = []

for i in range(len(label_colum)):
    print(i)

    if label_colum[i] == "normal":
        Label.append(0)

    elif label_colum[i] in Dos:         # Dos attack
        Label.append(1)

    elif label_colum[i] in Probe:       # Probe attack
        Label.append(2)

    elif label_colum[i] in R2L:         # R2L attack
        Label.append(3)

    else:
        Label.append(4)                 # U2R attack

# Save target
# np.savetxt("Label.csv", Label, delimiter=",", fmt="%d")