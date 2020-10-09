import time
import constants

from furhat_gestures import gesture_gen, gesture_trigger
from face_features_streamer import pose_csv_streamer as csv_streamer

def main():

    pose_data = csv_streamer.csv_head_pose_reader()
    smile_data = csv_streamer.csv_smile_intensity_reader()

    # pitch (Rx), yaw (Ry), and roll (Rz)
    # ' pose_Rx', ' pose_Ry', ' pose_Rz'
    for index, (pose_row, smile_row) in enumerate(zip(pose_data.iterrows(), smile_data.iterrows())):

        pose_row  = pose_row[1]
        smile_row = smile_row[1]

        print(index)

        gesture = gesture_gen.build_gesture_with(gesture_name=constants.gesture_name,
                                                 roll_strength=pose_row[" pose_Rz"],
                                                 tilt_strength=pose_row[" pose_Rx"],
                                                 pan_strength=pose_row[" pose_Ry"],
                                                 happy_strength=smile_row["Happy"],
                                                 smile_strength=smile_row[" AU25_r"],
                                                 speed=constants.speed, duration=constants.duration,
                                                 reset=constants.reset)

        time.sleep(0.2)

        response = gesture_trigger.trigger_custom_gesture(gesture)
        # break
        # print(response)

    return True


if __name__ == '__main__':
    main()
