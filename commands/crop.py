from . import command


@command
def dismiss_crop():
    return {"command": "dismiss_crop"}


dismiss_crop_result = (
    {
        "command": "dismiss_crop_result",
        "error_code": 0,
        "error_description": "",
        "result": True,
    },
)


@command
def cancel_crop_move(delay_frames=6):
    return {"command": "cancel_crop_move", "delay_frames": delay_frames}


cancel_crop_move_result = {
    "command": "cancel_crop_move_result",
    "current_crop_height": 720.0,
    "current_crop_width": 1279.999755859375,
    "current_crop_x": 818.3285522460938,
    "current_crop_y": 275.9733581542969,
    "discarded_frames": 13,
    "error_code": 0,
    "error_description": "",
    "remaining_frames": 6,
    "result": True,
}


@command
def set_crop_cut(x, y, w, h):
    # Sets crop immediately
    # TODO bounds check
    return {
        "command": "set_crop",
        "transition_aray": [
            {"h": float(h), "w": float(w), "x": float(x), "y": float(y)}
        ],
        "transition_type": "cut",  # or 'crop_move'
    }


def slerp(xi, xf, n=10):
    dx = (xf - xi) / (n - 1)
    return [xi + k * dx for k in range(n - 1)] + [xf]


@command
def set_crop_lerp(xi, yi, wi, hi, xf, yf, wf, hf, n=10):
    # NB: There are two modes, cut and move. The move one could use an arbitrary sequence of boxes, not just a smooth transition (?)
    # TODO: bounds check
    # TODO: I hope the digit precision doesnt matter
    lx = slerp(xi, xf, n)
    ly = slerp(yi, yf, n)
    lw = slerp(wi, wf, n)
    lh = slerp(hi, hf, n)
    transition_arRay = [
        {"x": k[0], "y": k[1], "w": k[2], "h": k[3]} for k in list(zip(lx, ly, lw, lh))
    ]
    return {
        "command": "set_crop",
        "transition_aray": transition_arRay,
        "transition_type": "crop_move",
    }


set_crop_result = (
    {
        "accepted_items": 1,
        "command": "set_crop_result",
        "error_code": 0,
        "error_description": "",
        "result": True,
        "total_items": 1,
    },
)
