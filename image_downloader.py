import config
import cv2
import datetime
import os
import json


# download a still jpg image from the rtsp stream
def download_image():
    # Create an RTSP connection
    cap = cv2.VideoCapture(f"rtsp://{config.rstp_user}:{config.rstp_pass}@{config.rstp_host}:{config.rstp_port}/{config.rstp_path}")
    # Read a frame from the stream
    ret, frame = cap.read()
    # Release the connection
    cap.release()
    # Current time: 2021-09-29 12:00:00
    # Current time formatted as iso: 2021-09-29T12:00:00
    time = datetime.datetime.now().isoformat()
    # cut off microseconds
    time = time.split(".")[0]
    # Save the frame as a jpg image with the current iso formatted timestamp as the filename
    cv2.imwrite(f"images/{time}.jpg", frame)
    # Return the frame
    return frame


# create a file called 'content.json' that includes all the filenames in the 'iages' folder without extension
def create_content_json():
    # Get all the filenames in the 'images' folder
    files = os.listdir("images")
    # Remove the extension from the filenames
    files = [file.split(".")[0] for file in files]
    # Create a dictionary with the filenames as keys and the filenames as values
    # content = [file for file in files]
    # Write the dictionary to a file called 'content.json'
    with open("content.json", "w") as file:
        json.dump(files, file)


# Download an image from the RTSP stream
download_image()
# Create a file called 'content.json' that includes all the filenames in the 'images' folder without extension
create_content_json()
