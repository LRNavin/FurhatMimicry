import pandas as pd
import matplotlib.pyplot as plt


# pose_Tx, pose_Ty, pose_Tz, pose_Rx, pose_Ry, pose_Rz
head_location = [" pose_Tx", " pose_Ty", " pose_Tz"]
head_rotation = [" pose_Rx", " pose_Ry", " pose_Rz"]

# AU12_r, - Lip Corner Puller
# AU25_r, - Lip Stretch
lip_move_au = [" AU06_r", " AU12_r", " AU25_r"]

skip_frames = 3
scale_pose = True
head_pose_scaler = 50
smile_auc_scaler = 5
data_focus = "smile"
pose_name = "Lip"

def plot_head_pose_data(csv_file):
    csv_data = pd.read_csv(csv_file)

    pose_data  = csv_data.loc[:, head_rotation]*head_pose_scaler
    smile_data = csv_data.loc[:, lip_move_au]/smile_auc_scaler
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
    # csv_file = "../openface_datasets/first_test_l_r.csv"
    # csv_file = "../openface_datasets/first_test_roll.csv"

    # csv_file = "../openface_datasets/smile_close_open.csv"
    # csv_file = "../openface_datasets/lips_open_close.csv"
    csv_file = "../openface_datasets/lips_open_just.csv"

    plot_head_pose_data(csv_file)

