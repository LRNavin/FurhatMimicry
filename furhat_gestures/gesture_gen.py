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

def head_rotate_gesture_gen(gesture_name, roll_strength, tilt_strength, pan_strength, speed=1.0, duration=2.0, reset="True"):

    gesture_def = {}
    gesture_def["class"] = "furhatos.gestures.Gesture"
    gesture_def["name"] = gesture_name

    gesture_detail = []
    # Create Gesture Type
    temp_dict = {"time": [speed], "params": {available_gestures.pan_neck: pan_strength}}
    gesture_detail.append(temp_dict)

    # Create Gesture Reseter
    # temp_dict = {"time": [duration], "params": {"reset": 0}}
    # gesture_detail.append(temp_dict)

    # Setter
    gesture_def["frames"] = gesture_detail

    return json.dumps(gesture_def)
