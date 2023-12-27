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
colors = [(100, 236, 201), (63, 161, 198), (9, 181, 248)]


def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global position
        position = (x, y)
        global take_color
        take_color = True


if __name__ == '__main__':
    cv2.setMouseCallback("Camera", on_mouse_click)
    random.shuffle(colors)
    print(colors)

    while cam.isOpened():
        ret, frame = cam.read()
        frame = cv2.GaussianBlur(frame, (21, 21), 0)
        hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        ball_positions = []

        for color in colors:
            h, s, v = color[0], color[1], color[2]

            lower = (h * 0.9, s * 0.5, v * 0.5)
            upper = (h * 1.1, 255, 255)
            take_color = False
            init = True

            mask = cv2.inRange(hsvframe, lower, upper)
            mask = cv2.dilate(mask, None, iterations=2)
            cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
            if len(cnts) > 0:
                c = max(cnts, key=cv2.contourArea)
                (x, y), radius = cv2.minEnclosingCircle(c)
                if radius > 30:
                    ball_positions.append((color, int(x)))


        curr_ball_colors = [color for color, position in sorted(ball_positions, key=lambda x: x[1])]
        # print("Current line ball colors:", curr_ball_colors)
        if (curr_ball_colors == colors and not guessed):
            print ("You guessed it!")
            guessed = True

        if guessed:
            cv2.putText(frame, "You guessed it!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Camera", frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
