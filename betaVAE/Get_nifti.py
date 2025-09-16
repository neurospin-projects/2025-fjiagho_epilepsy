from soma import aims
import numpy as np
import pandas as pd

#data = pd.read_pickle('/neurospin/dico/data/deep_folding/current/datasets/hcp/crops/2mm/S.C.-sylv./mask/Rskeleton.pkl')
#data = np.load('/neurospin/dico/data/deep_folding/current/datasets/UkBioBank40/crops/2mm/S.C.-sylv./mask/Rskeleton.npy')

#print(data.shape)

out_path = "/neurospin/dico/fred/Runs/01_betaVAE/Output/2025-09-12/17-10-55/"

for vol in ['input','output']:
    vol_npy = np.load(out_path+vol+'.npy')[0,0,:,:,:].astype(np.float32)
    print('Volume shape',vol_npy.shape)
    vol_nifty = aims.Volume(vol_npy)
    aims.write(vol_nifty, out_path+vol+'.nii.gz')

# hcp
#for sub in ['100206', '100307', '100408']:
# UKB
for sub in ['1000021','1000325','1000458']:
    for vol in ['_input','_output']:
        vol_npy = np.load(out_path+'subjects/'+sub+vol+'.npy').astype(np.float32)
        print('Volume shape',vol_npy.shape)
        vol_nifty = aims.Volume(vol_npy)
        aims.write(vol_nifty, out_path+'/subjects/'+sub+vol+'.nii.gz')