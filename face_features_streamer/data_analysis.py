from utilities import constants

import pandas as pd
import matplotlib.pyplot as plt

skip_frames = 3
scale_pose = True
head_pose_scaler = 50
smile_auc_scaler = 5

data_focus = "smile"
pose_name = "Lip"

def plot_head_pose_data(csv_file):
    csv_data = pd.read_csv(csv_file)

    pose_data  = csv_data.loc[:, constants.head_rotation] * head_pose_scaler
    smile_data = csv_data.loc[:, constants.lip_move_au] / smile_auc_scaler
    smile_data["Happy"] = smile_data[" AU06_r"] + smile_data[" AU12_r"]

    print(pd.read_csv(csv_file).columns)
    if data_focus == "head":
        for col in pose_data.columns:
            plt.plot(pose_data[col], label=pose_name+'-Pose-' + col)
    elif data_focus == "smile":
        for col in smile_data.columns:
            plt.plot(smile_data[col], label=pose_name + '-' + col)

    plt.legend(loc='upper right')
    plt.show()

    return True

if __name__ == '__main__':
    plot_head_pose_data(constants.csv_file)

