import pandas as pd
from Algorithm import CSA_QRNN, POA_QRNN
from Algorithm import SBOA_QRNN, Proposed_HSBOA_qrnn
import numpy as np

target = np.array(pd.read_csv("Label.csv", header=None))
S_feature = np.array(pd.read_csv("S_Feature.csv", header=None))  # Selected features

Swarm_size = [10, 20, 30, 40, 50]           # Swarm size

for i in range(len(Swarm_size)):
    ACC, TPR, TNR = [], [], []
    CSA_QRNN.call_proposed(S_feature, target, 0.9, ACC, TPR, TNR, 20, Swarm_size[i])
    POA_QRNN.call_proposed(S_feature, target, 0.9, ACC, TPR, TNR, 20, Swarm_size[i])
    SBOA_QRNN.call_proposed(S_feature, target, 0.9, ACC, TPR, TNR, 20, Swarm_size[i])
    Proposed_HSBOA_qrnn.call_proposed(S_feature, target, 0.9, ACC, TPR, TNR, 20, Swarm_size[i])


