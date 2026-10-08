from Main import Read_data, Pre_processing
from Main import Feature_selection
import pandas as pd
from Cloudsim import Run
from Proposed_HSBOA_QRNN import QRNN
import numpy as np
from Comparative import RF_RBFNN, IMFL_IDSCS
from Comparative import FEFS_DLM, CybS_CC_SACGAN_COA


def call_main(tr):
    Input_data = Run.cloud_sim()                # Input network traffic data

    print("\nTotal number of samples: ", len(Input_data))

    Process_data = Pre_processing.Read_process(Input_data)          # Pre_processed data

    N = 10

    target = pd.read_csv("Label.csv", header=None)
    S_feature = Feature_selection.feature_select(Process_data, target, N)      # Selected features

    ACC, TPR, TNR = [], [], []

    target = np.array(target)

    # ------------- Intrusion Detection -------------
    QRNN.call_proposed(S_feature, target, tr, ACC, TPR, TNR, epoch=20)        # Proposed method

    print("\n>>>>>>>>>>>>>>>>> Comparative Methods Running <<<<<<<<<<<<<<<<")

    IMFL_IDSCS.detection(S_feature, target, tr, ACC, TPR, TNR)
    FEFS_DLM.call_method(S_feature, target, tr, ACC, TPR, TNR)
    RF_RBFNN.detection(S_feature, target, tr, ACC, TPR, TNR)
    CybS_CC_SACGAN_COA.call_method(S_feature, target, tr, ACC, TPR, TNR)

    return ACC, TPR, TNR
