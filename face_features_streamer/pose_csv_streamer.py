import pandas as pd

csv_file = "../openface_datasets/first_test_l_r.csv"

# pose_Tx, pose_Ty, pose_Tz, pose_Rx, pose_Ry, pose_Rz
head_location = [" pose_Tx", " pose_Ty", " pose_Tz"]
head_rotation = [" pose_Rx", " pose_Ry", " pose_Rz"]

skip_frames = 3

def csv_head_pose_reader():
    pose_data = pd.read_csv(csv_file).loc[:, head_rotation].iloc[::skip_frames, :]
    print(len(pose_data))
    return pose_data

if __name__ == '__main__':
    csv_head_pose_reader()

