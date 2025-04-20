# Video Steganography Tool User Guide

![alt text](image.png)

# Step by step demo

- Install libraries

`pip install -r requirements.txt`

- Extracting Frames from Video

`python ExtractAndCombine.py getframes [input_video_file_path]`

![alt text](image-1.png)
![alt text](image-2.png)

- Extracting Audio from Video

`python ExtractAndCombine.py getaudio [input_video_file_path]`

![alt text](image-3.png)

![alt text](image-4.png)

- Hiding Data in Frames

`python Encoder.py`

- select start and end frame where data will be hidden at
- select frames extraction location
- select file to hide

![alt text](image-5.png)

- Hiding Data in Audio

- `python wav-steg.py -h -d "[file to hide]" -s "[input audio file]" -o "[output audio file]" -n "[number of bits]"`

![alt text](image-6.png)

![alt text](image-7.png)

- Combine Frames and Audio into a Video

`python  .\ExtractAndCombine.py combine [frames_dir] [audio_path]`

![alt text](image-8.png)
![alt text](image-9.png)
![alt text](image-10.png)

- Extracting Frames from Steg Video

![alt text](image-11.png)
![alt text](image-12.png)

- Decode Hidden Data in Frames

![alt text](image-13.png)
![alt text](image-14.png)

- Decode Hidden Data in Audio

![alt text](image-15.png)
![alt text](image-16.png)
