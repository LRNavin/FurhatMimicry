
import time
from furhat_gestures import gesture_gen, gesture_trigger, available_gestures
from face_features_streamer import pose_csv_streamer

def main():
    gesture_type = available_gestures.roll_neck
    gesture_name = "Roll Neck"
    strength = -21.0
    speed = 2.0 #sec
    duration = 3.0 #sec
    reset = True

    pose_data = pose_csv_streamer.csv_head_pose_reader()

    for index, row in pose_data.iterrows():
        # pitch (Rx), yaw (Ry), and roll (Rz)
        # ' pose_Rx', ' pose_Ry', ' pose_Rz'

        gesture = gesture_gen.head_rotate_gesture_gen(gesture_name=gesture_name,
                                                      roll_strength=row[2]*400,
                                                      tilt_strength=row[1]*400,
                                                      pan_strength=row[0]*400,
                                                      speed=1.0, duration=2.0, reset="False")

        print(gesture)
        time.sleep(1.0)

        response = gesture_trigger.trigger_custom_gesture(gesture)
        # break
        # print(response)

        # break

    return True


if __name__ == '__main__':
    main()