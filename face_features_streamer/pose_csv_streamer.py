import constants as c

import pandas as pd
import matplotlib.pyplot as plt

plot_pose = True

def csv_head_pose_reader():

    pose_data  = pd.read_csv(c.csv_file).loc[:, c.head_rotation]*c.head_pose_scaler

    for col in pose_data.columns:
        if c.move_avg_pose:
            pose_data[col] = pose_data[col].rolling(window=c.window_size).mean()
        plt.plot(pose_data[col], label='MA-Pose-' + col)

    pose_data = pose_data.iloc[::c.skip_frames, :]

    if plot_pose:
        plt.legend(loc='upper right')
        plt.show()

    return pose_data

def csv_smile_intensity_reader():
    smile_data = pd.read_csv(c.csv_file).loc[:, c.lip_move_au]/c.smile_auc_scaler
    smile_data["Happy"] = smile_data[" AU06_r"] + smile_data[" AU12_r"]

    for col in smile_data.columns:
        if c.move_avg_pose:
            smile_data[col] = smile_data[col].rolling(window=c.window_size).mean()
        plt.plot(smile_data[col], label='Lip-' + col)

    smile_data = smile_data.iloc[::c.skip_frames, :]

    if plot_pose:
        plt.legend(loc='upper right')
        plt.show()

    return smile_data


if __name__ == '__main__':
    csv_head_pose_reader()
    csv_smile_intensity_reader()


