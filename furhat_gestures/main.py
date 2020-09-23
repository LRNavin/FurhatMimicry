
import time
from furhat_gestures import gesture_gen, gesture_trigger, available_gestures
from face_features_streamer import csv_streamer

def main():
    gesture_type = available_gestures.roll_neck
    gesture_name = "Roll Neck"
    strength = -21.0
    speed = 0.2 #sec
    duration = 3.0 #sec
    reset = "True"

    pose_data = csv_streamer.csv_head_pose_reader()
    smile_data = csv_streamer.csv_smile_intensity_reader()

    for index, row in pose_data.iterrows():
        # pitch (Rx), yaw (Ry), and roll (Rz)
        # ' pose_Rx', ' pose_Ry', ' pose_Rz'

        gesture = gesture_gen.build_gesture_with(gesture_name=gesture_name,
                                                 roll_strength=row[2],
                                                 tilt_strength=row[0],
                                                 pan_strength=row[1],
                                                 speed=speed, duration=duration, reset=reset)

        print(index)
        print(gesture)
        time.sleep(0.2)

        response = gesture_trigger.trigger_custom_gesture(gesture)
        # break
        # print(response)

    return True


if __name__ == '__main__':
    main()
