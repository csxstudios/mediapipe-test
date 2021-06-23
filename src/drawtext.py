import time


def getFpsText(start, nativeFPS):
    end = time.time()
    totalTime = end - start
    fps = nativeFPS if end == start else 1 / totalTime
    text = f"CURRENT FPS: {int(fps)} \n NATIVE FPS: {int(nativeFPS)}"
    return text


def putTextTemplate(cv2, image, text):
    position = (20, 20)  # x, y
    font_scale = 1
    color = (0, 255, 0)
    thickness = 1
    font = cv2.FONT_HERSHEY_PLAIN
    line_type = cv2.LINE_AA

    text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
    line_height = text_size[1] + 5
    x, y0 = position

    for i, line in enumerate(text.split(" \n ")):
        y = y0 + i * line_height
        cv2.putText(image, line, (x, y), font, font_scale, color, thickness, line_type)
