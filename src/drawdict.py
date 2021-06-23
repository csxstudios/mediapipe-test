def drawLandmarks(image, results, mp_holistic, mp_drawing):
    drawDict = {
        "face": {
            "active": True,
            "image": image,
            "landmarks": results.face_landmarks,
            "connections": mp_holistic.FACE_CONNECTIONS,
            "pointColor": (255, 0, 0),  # B, G, R
            "lineColor": (0, 0, 255),
        },
        "right_and": {
            "active": True,
            "image": image,
            "landmarks": results.right_hand_landmarks,
            "connections": mp_holistic.HAND_CONNECTIONS,
            "pointColor": (0, 255, 0),  # B, G, R
            "lineColor": (0, 0, 255),
        },
        "left_hand": {
            "active": True,
            "image": image,
            "landmarks": results.left_hand_landmarks,
            "connections": mp_holistic.HAND_CONNECTIONS,
            "pointColor": (0, 0, 255),  # B, G, R
            "lineColor": (0, 255, 0),
        },
        "pose": {
            "active": True,
            "image": image,
            "landmarks": results.pose_landmarks,
            "connections": mp_holistic.POSE_CONNECTIONS,
            "pointColor": (0, 255, 0),  # B, G, R
            "lineColor": (255, 0, 255),
        },
    }
    for draw in drawDict:
        if drawDict[draw]["active"]:
            mp_drawing.draw_landmarks(
                drawDict[draw]["image"],
                drawDict[draw]["landmarks"],
                drawDict[draw]["connections"],
                mp_drawing.DrawingSpec(
                    color=drawDict[draw]["pointColor"], thickness=2, circle_radius=2
                ),
                mp_drawing.DrawingSpec(
                    color=drawDict[draw]["lineColor"], thickness=1, circle_radius=1
                ),
            )
