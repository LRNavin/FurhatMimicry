# Constant File
import furhat_gestures.available_gestures as available_gestures

## Furhat Experimental API
headers = {
    'Content-type': 'application/json',
}

base_url = "http://localhost"
port = "54321"


## Gestures Builder
gesture_template = {
    "frames": [],
    "class": "furhatos.gestures.Gesture"
}
gesture_class = "furhatos.gestures.Gesture"

## Gesture Dict Values
gesture_type = available_gestures.roll_neck
gesture_name = "Roll Neck"
strength = -21.0
speed = 0.2  # sec
duration = 1.0  # sec
reset = "True"

## Gesture Thresholds
happy_threshold = 0.4
mouth_open_threshold = 0.4


## Open Face File Output Columns:
### pose_Tx, pose_Ty, pose_Tz, pose_Rx, pose_Ry, pose_Rz
head_location = [" pose_Tx", " pose_Ty", " pose_Tz"]
head_rotation = [" pose_Rx", " pose_Ry", " pose_Rz"]

### AU12_r, - Lip Corner Puller
### AU25_r, - Lip Stretch
lip_move_au = [" AU06_r", " AU12_r", " AU25_r"]


## Open Face Output Filepath
# csv_file = "../openface_datasets/first_test_l_r.csv"
# csv_file = "../openface_datasets/first_test_roll.csv"
# csv_file = "../openface_datasets/smile_close_open.csv"
# csv_file = "../openface_datasets/lips_open_close.csv"
# csv_file = "../openface_datasets/lips_open_just.csv"
# csv_file = "../openface_datasets/first_test_high.csv"
# csv_file = "../openface_datasets/lips_open_close-4.csv"
# csv_file = "../openface_datasets/first_test_roll.csv"
# csv_file = "../openface_datasets/first_test_round.csv"

csv_file = "../openface_datasets/lips_open_just-4.csv"

## Open Face output pre-processing constants
skip_frames = 3
move_avg_pose = False
scale_pose = True
head_pose_scaler = 50
smile_auc_scaler = 5
window_size = 3