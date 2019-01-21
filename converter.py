from utils import *
import pickle as pk

path = "barbell/barbell_0010/hmr.pkl"
f = open(path, 'rb')
data = pk.load(f)


output_file = open('fixed.txt', 'w')

frame_duration = 1.0/24

output_file.write('{\n"Loop": "wrap", \n"Frames":\n[\n')

for i, SMPL_pose in enumerate(data['poses']):
    line = []
    line += [frame_duration]
    pos = np.array([0.00, 0.76, 0.00])  - data['cams'][i] + data['cams'][0]
    line.extend(pos)

    for k, joint in enumerate(joints):
     
        corresponding_joints = joint_mapping[joint]
        corresponding_rotations = [get_axisangle(jnt, SMPL_pose) for jnt in corresponding_joints]
        if k in oneDjoints :
            if k in [4, 9]: #knees
                line.append(-rot_angle(corresponding_rotations[0]))
            else:
                line.append(rot_angle(corresponding_rotations[0]))
        else:
            quat = np.quaternion(1, 0, 0, 0)
            if k==0:
                quat = quaternion.from_rotation_vector(np.array([0, 0, np.pi]))
            if k == 6:
                quat = quaternion.from_rotation_vector(np.array([-np.pi/2, 0, 0]))
            if k == 11:
                quat = quaternion.from_rotation_vector(np.array([np.pi/2, 0, 0]))
            for jnt, rot in enumerate(corresponding_rotations):
                #if k == 6: #right shoulder
                    #rot = [-rot[0], rot[1], rot[2]] 
                #if k == 11: #left shoulder
                    #rot = [-rot[0], rot[1], rot[2]]
                quat = quat * quaternion.from_rotation_vector(rot)

            line.extend(quaternion.as_float_array(quat))
    output_file.write(str(line))

    if i < len(data['poses']) - 1:
        output_file.write(',')
    output_file.write('\n')

output_file.write(']\n}\n')
output_file.close()
