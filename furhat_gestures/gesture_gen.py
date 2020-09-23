import json
from furhat_gestures import available_gestures

gesture_template = {
    "frames": [],
    "class": "furhatos.gestures.Gesture"
    }

# pitch (Rx), yaw (Ry), and roll (Rz)

def single_gesture_gen(gesture_type, gesture_name, strength, speed, duration, reset="True"):
    gesture_def = gesture_template.copy()
    gesture_def["name"] = gesture_name

    gesture_detail = gesture_def["frames"]
    # Create Gesture Type
    temp_dict = {"time": [speed], "params": {gesture_type: strength}}
    gesture_detail.append(temp_dict)

    # Create Gesture Reseter
    temp_dict = {"time": [duration], "params": {"reset": reset.lower()}}
    gesture_detail.append(temp_dict)

    return json.dumps(gesture_def)

def select_max_headpose_channel(roll_strength, tilt_strength, pan_strength):
    abs_roll = abs(roll_strength)
    abs_tilt = abs(tilt_strength)
    abs_pan  = abs(pan_strength)

    # print(abs_roll)
    # print(abs_tilt)
    # print(abs_pan)
    #
    # print(roll_strength)
    # print(tilt_strength)
    # print(pan_strength)

    # if abs_pan > abs_roll and abs_pan > abs_tilt:
    #     return {available_gestures.pan_neck: pan_strength}
    # elif abs_roll > abs_pan and abs_roll > abs_tilt:
    #     return {available_gestures.roll_neck: roll_strength}
    # elif abs_tilt > abs_pan and abs_tilt > abs_roll:
    #     return {available_gestures.tilt_neck: tilt_strength}

    return {available_gestures.pan_neck: pan_strength,
            available_gestures.roll_neck: roll_strength,
            available_gestures.tilt_neck: tilt_strength}


def set_head_pose_gesture(temp_dict, roll_strength, tilt_strength, pan_strength):

    # Set directly scaled values of Head Pose
    temp_dict["params"][available_gestures.pan_neck] = pan_strength
    temp_dict["params"][available_gestures.roll_neck] = roll_strength
    temp_dict["params"][available_gestures.tilt_neck] = tilt_strength

    return temp_dict

def set_smile_gesture(temp_dict, smile_strength=1.0):

    # Set Smile boolean
    temp_dict["params"][available_gestures.open_smile] = smile_strength

    return temp_dict

# available_gestures.roll_neck: roll_strength,
# available_gestures.tilt_neck: tilt_strength
def build_gesture_with(gesture_name, roll_strength, tilt_strength,
                            pan_strength, speed=1.0, duration=2.0, reset="True",
                            head_pose=True, smile_pose=False):

    gesture_def = {}
    gesture_def["class"] = "furhatos.gestures.Gesture"
    gesture_def["name"] = gesture_name

    gesture_detail = []
    # Create Gesture Type
    temp_dict = {"time": [speed], "params": {}}
    if head_pose:
        temp_dict = set_head_pose_gesture(temp_dict, roll_strength, tilt_strength, pan_strength)
    if smile_pose:
        temp_dict = set_smile_gesture(temp_dict)

    gesture_detail.append(temp_dict)

    # Create Gesture Reseter
    temp_dict = {"time": [duration], "params": {"reset": reset.lower()}}
    gesture_detail.append(temp_dict)

    # Setter
    gesture_def["frames"] = gesture_detail

    return json.dumps(gesture_def)

