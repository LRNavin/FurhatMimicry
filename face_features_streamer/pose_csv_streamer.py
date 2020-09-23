import pandas as pd
import matplotlib.pyplot as plt

# csv_file = "../openface_datasets/first_test_high.csv"
csv_file = "../openface_datasets/first_test_l_r.csv"
# csv_file = "../openface_datasets/first_test_roll.csv"
# csv_file = "../openface_datasets/first_test_round.csv"

# pose_Tx, pose_Ty, pose_Tz, pose_Rx, pose_Ry, pose_Rz
head_location = [" pose_Tx", " pose_Ty", " pose_Tz"]
head_rotation = [" pose_Rx", " pose_Ry", " pose_Rz"]

# AU12_r, - Lip Corner Puller
# AU25_r, - Lip Stretch
lip_move_au = [" AU12_r", " AU25_r"]

skip_frames = 3
ma_pose = False
scale_pose = True
head_pose_scaler = 50
smile_auc_scaler = 5

plot_pose = False

def csv_head_pose_reader():

    pose_data  = pd.read_csv(csv_file).loc[:, head_rotation]*head_pose_scaler

    for col in pose_data.columns:
        if ma_pose:
            pose_data[col] = pose_data[col].rolling(window=3).mean()
        plt.plot(pose_data[col], label='MA-Pose-' + col)

    pose_data = pose_data.iloc[::skip_frames, :]
    print(len(pose_data[" pose_Rz"]))

    if plot_pose:
        plt.legend(loc='upper right')
        plt.show()

    return pose_data

def csv_smile_intensity_reader():
    smile_data = pd.read_csv(csv_file).loc[:, lip_move_au]/smile_auc_scaler
    smile_data["Happy"] = smile_data[" AU06_r"] + smile_data[" AU12_r"]

    for col in smile_data.columns:
        if ma_pose:
            smile_data[col] = smile_data[col].rolling(window=3).mean()
        plt.plot(smile_data[col], label='Lip-' + col)

    smile_data = smile_data.iloc[::skip_frames, :]
    print(len(smile_data[" AU06_r"]))

    if plot_pose:
        plt.legend(loc='upper right')
        plt.show()

    return smile_data


if __name__ == '__main__':
    csv_head_pose_reader()
    csv_smile_intensity_reader()


