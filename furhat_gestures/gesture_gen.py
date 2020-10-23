import json
from utilities import constants
from furhat_gestures import available_gestures

# pitch (Rx), yaw (Ry), and roll (Rz)
def single_gesture_gen(gesture_type, gesture_name, strength, speed, duration, reset="True"):
    gesture_def = constants.gesture_template.copy()
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

    if False:
        if abs_pan > abs_roll and abs_pan > abs_tilt:
            return {available_gestures.pan_neck: pan_strength}
        elif abs_roll > abs_pan and abs_roll > abs_tilt:
            return {available_gestures.roll_neck: roll_strength}
        elif abs_tilt > abs_pan and abs_tilt > abs_roll:
            return {available_gestures.tilt_neck: tilt_strength}

    return {available_gestures.pan_neck: pan_strength,
            available_gestures.roll_neck: roll_strength,
            available_gestures.tilt_neck: tilt_strength}


def set_head_pose_gesture(temp_dict, roll_strength, tilt_strength, pan_strength):

    # Set directly scaled values of Head Pose
    temp_dict["params"][available_gestures.pan_neck] = pan_strength
    temp_dict["params"][available_gestures.roll_neck] = roll_strength
    temp_dict["params"][available_gestures.tilt_neck] = tilt_strength

    return temp_dict

def set_smile_gesture(temp_dict, happy_strength, smile_strength):

    # Set Smile boolean
    if happy_strength > constants.happy_threshold:
        # Happiness Detected AU_06 + AU_12
        temp_dict["params"][available_gestures.open_smile] = smile_strength
    else:
        # Not Happy.
        if smile_strength > constants.mouth_open_threshold:
            # Not Happy but mouth Open, where mouth Open = AU_25 (smile strength)
            temp_dict["params"][available_gestures.say_big_aah] = smile_strength/2

    return temp_dict

# available_gestures.roll_neck: roll_strength,
# available_gestures.tilt_neck: tilt_strength
def build_gesture_with(gesture_name, roll_strength, tilt_strength, pan_strength,
                       happy_strength, smile_strength,
                       speed=1.0, duration=2.0, reset="True"):

    gesture_def = {}
    gesture_def["class"] = constants.gesture_class
    gesture_def["name"] = gesture_name

    gesture_detail = []
    # Create Gesture Type
    temp_dict = {"time": [speed], "params": {}}
    # Set Head Pose Gesture
    temp_dict = set_head_pose_gesture(temp_dict, roll_strength, tilt_strength, pan_strength)
    # Set Smile Gesture
    temp_dict = set_smile_gesture(temp_dict, happy_strength, smile_strength)
    # Add More Gestures here ->>>>>>


    gesture_detail.append(temp_dict)

    # Create Gesture Reseter
    temp_dict = {"time": [duration], "params": {"reset": reset.lower()}}
    gesture_detail.append(temp_dict)

    # Setter
    gesture_def["frames"] = gesture_detail

    print(gesture_def)
    return json.dumps(gesture_def)

