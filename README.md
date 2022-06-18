# Images-Videos-to-ascii
A python program to convert Images/Videos to ascii frames

STEPS TO RUN:
1)  Download the video-to-ascii python file
2)  The following libraries are required.
    1)OpenCV
    2)os
    3)moviepy
    4)numpy
    5)PILLOW
4)  Then run the python file however you like without any command line arguments
5)  As the program asks queries, reply to it
6)  Then the image or video will get processed

FEATURES IMPLEMENTED:(Along with internal working)
1)  The program basically is capable of converting images to ascii pictures with either black or white background.
    1) This has been implemented as explained in the project sessions. The function **process** does this.
2)  Additionally the program can also process videos.
    1) It splits videos into frames using OpenCV library. Those frames are stored in an images folder.
    2) Then it converts each frame into ascii frames using the function **process**.
    3) Then all the ascii frames are merged into a video using moviepy library.
    4) Then audio from the initial video is also added to final video using moviepy library.
3) The program can also process webcam footage.
    1) It initially records webcam footage using OpenCV's video capture.(Only video no audio)
    2) Then that recorded video is processed exactly as a video will as explained in 2.
4) The program can also generate pencil sketches of ascii art.
    1)This is a very basic implementation to convert normal images to pencil sketches which I used for converting ascii images to pencil sketches.
    2)The ascii image of an image is first got.
    3)The ascii image is converted into grayscale.
    4)Then the colours are inverted.
    5)The image is then blurred.
    6)Now again the colours are inverted.
    7)Then the pixel arrays of the gray image and the inverted blurred image are divided to get the output pencil sketch.

Sample processed images are attached.
