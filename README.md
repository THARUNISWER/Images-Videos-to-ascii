# Images-Videos-to-ascii
A python program to convert Images/Videos to ascii frames

STEPS TO RUN:
1)  Download the video-to-ascii python file along with the fonts.
2)  The following libraries are required.
    i. OpenCV
    ii. os
    iii. moviepy
    iv. numpy
    v. PILLOW
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
    i) This is a very basic implementation to convert normal images to pencil sketches which I used for converting ascii images to pencil sketches.
    ii) The ascii image of an image is first got.
    iii) The ascii image is converted into grayscale.
    iv) Then the colours are inverted.
    v) The image is then blurred.
    vi) Now again the colours are inverted.
    vii) Then the pixel arrays of the gray image and the inverted blurred image are divided to get the output pencil sketch.
    
LEARNINGS:
Learnt about python image processing in general. Learnt the various commands in python image processing libraries especially Open CV. Learnt that you could do video editing also with python. Apart from coding language perspective, understood about luminosity of pixels. Learnt how different ascii characters show different luminosity. Mainly learnt how to google a lot of python coding stuff as coding also involves a large part of googling.

REFERENCES:
https://en.wikipedia.org/wiki/ASCII_art#Types_and_styles
https://www.geeksforgeeks.org/extract-images-from-video-in-python/
https://stackoverflow.com/questions/44732602/convert-image-sequence-to-video-using-moviepy
https://analyticsindiamag.com/converting-image-into-a-pencil-sketch-in-python/
https://www.geeksforgeeks.org/moviepy-assigning-audio-clip-to-video-file/

Sample processed images and videos are attached.
The video demo has been attached along in the repository itself
