import cv2
import os
from moviepy.editor import VideoFileClip
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont
import moviepy.video.io.ImageSequenceClip
from numpy.core.defchararray import upper

choice = input("Would you like to give input from (W)ebcam or (V)ideofile or (I)magefile: ")
choice = upper(choice)
sketch = "A"

if choice == "V":
    Video_path = input("Enter Video path: ")
    # example: bunny.mp4
    Output_path = input("Enter final video path: ")
    # example: final.mp4
    Images_folder = input("Enter the folder path where images from video are to be stored: ")
    # example: ./data
    try:
        # creating a folder named data
        if not os.path.exists(Images_folder):
            os.makedirs(Images_folder)
    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

elif choice == "W":
    print("Webcam ascii videos have only video and no audio")
    real_time = int(input("Enter number of seconds to capture webcam footage: "))
    fps = int(input("Enter fps of your webcam(Mostly 30 or 60): "))
    # example: 30
    Output_path = input("Enter final video path: ")
    # example: final.mp4
    Images_folder = input("Enter the folder path where images from video are to be stored: ")
    # example: ./data
    try:
        # creating a folder named data
        if not os.path.exists(Images_folder):
            os.makedirs(Images_folder)
    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

elif choice == "I":
    sketch = input("Would you like image in (A)scii art or (P)encil sketch ascii art: ")
    sketch = upper(sketch)
    Image_path = input("Enter image path: ")
    Output_path = input("Enter final image path: ")
else:
    print("Error: Wrong choice")
    exit(0)

bg = input("Enter the background color(black or white): ")
# example: black


# EXTRACTING FRAMES OUT OF THE VIDEO
currentframe = 0
if choice == "V":
    # Read the video from specified path
    vid = cv2.VideoCapture(Video_path)

    # Get fps of main video
    fps = int(vid.get(cv2.CAP_PROP_FPS))
    # frame

    while True:

        # reading from frame
        success, frame = vid.read()

        if success:
            # continue creating images until video remains
            name = Images_folder + '/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    # Release all space and windows once done
    vid.release()
    cv2.destroyAllWindows()

elif choice == "W":
    cap = cv2.VideoCapture(0)
    i = 0

    while i < fps*real_time:
        ret, frame = cap.read()

        # This condition prevents from infinite looping
        # incase video ends.
        if ret == False:
            break
        name = Images_folder + '/frame' + str(i) + '.jpg'
        print('Creating...' + name)
        # Save Frame by Frame into disk using imwrite method
        cv2.imwrite(name, frame)
        i += 1
    currentframe = i
    cap.release()
    cv2.destroyAllWindows()

# FUNCTIONS FOR PROCESSING IMAGES INTO ASCII

# Characters used for Mapping to Pixels
Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}


def get_data(mode):
    font = ImageFont.truetype("fonts/DejaVuSansMono.ttf", size=20)
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale


# Making Background Black or White

if bg == "white":
    bg_code = (255, 255, 255)
else:
    bg_code = (0, 0, 0)

# Getting the character List, Font and Scaling characters for square Pixels
char_list, font, scale = get_data("complex")
num_chars = len(char_list)
num_cols = 300

# all images generated should have same size
req_width = 0
req_height = 0


def process(name, out):
    image = cv2.imread(name)
    if image is None:
        return

    # Extracting height and width from Image
    height, width, _ = image.shape

    # Defining height and width of each cell==pixel
    cell_w = width / num_cols
    cell_h = scale * cell_w
    num_rows = int(height / cell_h)

    # Calculating Height and Width of the output Image
    char_width, char_height = font.getsize("A")
    out_width = char_width * num_cols
    out_height = scale * char_height * num_rows

    # Making a new Image using PIL
    out_image = Image.new("RGB", (out_width, out_height), bg_code)
    draw = ImageDraw.Draw(out_image)

    for i in range(num_rows):
        for j in range(num_cols):
            partial_image = image[int(i * cell_h):min(int((i + 1) * cell_h), height),
                            int(j * cell_w):min(int((j + 1) * cell_w), width), :]
            partial_avg_color = np.sum(np.sum(partial_image, axis=0), axis=0) / (cell_h * cell_w)
            partial_avg_color = tuple(partial_avg_color.astype(np.int32).tolist())
            c = char_list[min(int(np.mean(partial_image) * num_chars / 255), num_chars - 1)]
            draw.text((j * char_width, i * char_height), c, fill=partial_avg_color, font=font)

    # Inverting Image and removing excess borders
    if bg == "white":
        cropped_image = ImageOps.invert(out_image).getbbox()
    else:
        cropped_image = out_image.getbbox()

    # Saving the new Image
    out_image = out_image.crop(cropped_image)
    # noting size of first image and making all others same
    if choice == "W" or choice == "V":
        if req_width != 0 and req_height != 0:
            out_image = out_image.resize((req_width, req_height))
    out_image.save(out)
    if sketch == "P":
        original_img = cv2.imread(out)
        gray_image = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
        inverted_gray_image = 255 - gray_image
        blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
        inverted_blurred_image = 255 - blurred_image
        pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
        cv2.imwrite(out, pencil_sketch_image)


# FOR VIDEOS

if choice == "V" or choice == "W":
    image_files = []
    #processing all the images
    for dsx in range(0,currentframe):
        name = Images_folder + "/frame" + str(dsx) + ".jpg"
        print("Processing " + name)
        process(name, name)
        # array of images to be combined into a video
        image_files.append(Images_folder + "/frame" + str(dsx) + ".jpg")
        img = cv2.imread(name)
        req_height, req_width,_ = img.shape
        dsx += 1

    # CREATING A VIDEO OUT OF THE FRAMES

    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)

    # extracting audio from original clip and adding to new video
    if choice == "V":
        vid = VideoFileClip(Video_path)
        audio = vid.audio

        final_clip = clip.set_audio(audio)
        final_clip.write_videofile(Output_path)
    else:
        clip.write_videofile(Output_path)

else:
    # FOR IMAGES
    print("Processing " + Image_path)
    process(Image_path, Output_path)

