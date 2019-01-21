import numpy as np
import quaternion

def rot_angle(axang):
    return np.linalg.norm(axang)

def get_axisangle(jointId, SMPL_pose):
    v = SMPL_pose[3*jointId: 3*jointId + 3]
    return np.array([v[2], v[1], -v[0]])

#DeepMimic default humanoid joints
joints = [
    'root',
    'chest',
    'neck',
    'right hip',
    'right knee ',
    'right ankle',
    'right shoulder',
    'right elbow ',
    'left hip',
    'left knee ',
    'left ankle',
    'left shoulder',
    'left elbow ' ]
#Corresponding joint index in SMPL
joint_mapping = {
    'root': [0],
    'chest': [3, 6],
    'neck': [9, 12],
    'right hip': [2],
    'right knee ': [5],
    'right ankle': [8],
    'right shoulder': [14, 17],
    'right elbow ': [19],
    'left hip': [1],
    'left knee ': [4],
    'left ankle': [7],
    'left shoulder': [13, 16],
    'left elbow ': [18]}
#1D joints
oneDjoints = set([4, 7, 9, 12])
