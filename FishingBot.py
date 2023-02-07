import pyautogui
import numpy as np
import cv2


def Capture_Monitor(monitorSize):
    imageSource = pyautogui.screenshot()

    imageResult = np.array(imageSource)
    imageResult = cv2.cvtColor(imageResult, cv2.COLOR_BGR2RGB)
    imageResult = cv2.resize(imageResult, dsize=(int(monitorSize[0] / 2), int(monitorSize[1] / 2)), interpolation=cv2.INTER_AREA)

    return imageResult


if __name__ == '__main__':
    monitorSize = pyautogui.size()

    while True:

        monitorImage = Capture_Monitor(monitorSize)
        cv2.imshow('Lost Ark', monitorImage)

        if cv2.waitKey(1) == 27:
            break
        

    cv2.destroyAllWindows()
