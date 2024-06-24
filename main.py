from PIL import ImageGrab
import webbrowser
import time
import os


def is_brown(pixel):
    r, g, b = pixel
    white_threshold = 240
    gray_threshold = 30

    # Check if the pixel is not white
    not_white = r < white_threshold and g < white_threshold and b < white_threshold

    # Check if the pixel is not gray
    not_gray = abs(r - g) > gray_threshold or abs(r - b) > gray_threshold or abs(g - b) > gray_threshold

    return not_white and not_gray


def analyze_screenshot(screenshot):
    # Convert the screenshot to RGB mode to ensure the pixel values are in RGB format
    screenshot = screenshot.convert("RGB")
    url = "https://www.chess.com"

    start_x = 2477
    end_x = 2620
    y = 430

    print(f"pixel: {screenshot.getpixel((2550, y))}")

    for x in range(start_x, end_x):
        pixel = screenshot.getpixel((x, y))
        if is_brown(pixel):
            return True
    return False


def take_and_analyze_screenshots():
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    combination = ""
    chess = "https://www.chess.com"
    youtube = "https://www.youtube.com"
    flashon = "http://192.168.0.4/on"
    flashoff = "http://192.168.0.4/off"

    try:
        while True:
            print("Analyzing screenshot...")
            # Capture the entire screen
            screenshot = ImageGrab.grab()
            crossed = "false"

            if analyze_screenshot(screenshot):
                combination = combination + "1"
                crossed = "true"
                print(f"Brown brainwave crossed 800 at screenshot_{int(time.time())}.png")
            else:
                if len(combination) != 0:
                    combination = combination + "0"

            if len(combination) == 3:
                print(combination)
                if combination == "110":
                    webbrowser.open(chess)
                elif combination == "101":
                    webbrowser.open(youtube)
                elif combination == "111":
                    webbrowser.open(flashon)
                elif combination == "100":
                    webbrowser.open(flashoff)
                break

            # Generate a unique filename based on the current timestamp

            filename = os.path.join(screenshot_dir, f"screenshot_{int(time.time())}{crossed}.png")


            screenshot.save(filename)



            # Introduce a short sleep to limit capture frequency (adjust as needed)
            time.sleep(3)

    except KeyboardInterrupt:
        print("Stopping screenshot capture...")


if __name__ == "__main__":
    take_and_analyze_screenshots()
