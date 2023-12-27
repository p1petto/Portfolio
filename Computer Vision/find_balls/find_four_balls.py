import cv2
import random

cv2.namedWindow("Camera", cv2.WINDOW_KEEPRATIO)
cam = cv2.VideoCapture(0)

lower = (0, 0, 0)
upper = (255, 255, 255)
take_color = False
init = False
guessed = False

position = (10, 10)

# blue, green, orange
colors = [
    (100, 236, 201), (24, 255, 179),  # blue yellow
    (63, 161, 198), (9, 181, 248)      # green orange
]

def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global position
        position = (x, y)
        global take_color
        take_color = True

if __name__ == '__main__':
    cv2.setMouseCallback("Camera", on_mouse_click)

    random.shuffle(colors)
    result_matrix = [[colors[i], colors[i + 1]] for i in range(0, len(colors), 2)]

    for row in result_matrix:
        print(row)

    while cam.isOpened():
        ret, frame = cam.read()
        frame = cv2.GaussianBlur(frame, (21, 21), 0)
        hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        ball_positions = []

        for row in result_matrix:
            for color in row:
                b, g, r = color

                lower = (b * 0.9, g * 0.5, r * 0.5)
                upper = (b * 1.1, 255, 255)
                take_color = False
                init = True

                mask = cv2.inRange(hsvframe, lower, upper)
                mask = cv2.dilate(mask, None, iterations=2)
                cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
                if len(cnts) > 0:
                    c = max(cnts, key=cv2.contourArea)
                    (x, y), radius = cv2.minEnclosingCircle(c)
                    if radius > 30:
                        ball_positions.append((color, int(x), int(y)))

        curr_ball_colors = [color for color, x, y in sorted(ball_positions, key=lambda p: (p[2], p[1]))]

        if (curr_ball_colors == [color for row in result_matrix for color in row] and not guessed):
            print("You guessed it!")
            guessed = True

        if guessed:
            cv2.putText(frame, "You guessed it!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Camera", frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
