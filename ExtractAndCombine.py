import sys
import os
import cv2
from PIL import Image
from moviepy.editor import VideoFileClip
from tqdm import tqdm  # For progress bar

def get_video(video_path, output_path="output/video_only.mp4"):
    """Extract video without audio"""
    video_object = VideoFileClip(video_path)
    video_object.write_videofile(filename=output_path, audio=False)
    print(f"Video without audio saved to {output_path}")

def get_audio(video_path, output_path=None):
    """Extract audio without video"""
    if output_path is None:
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        output_path = f"output/extracted_{base_name}.wav"

    if os.path.exists(output_path):
        overwrite = input(f"The file '{output_path}' already exists. Do you want to overwrite it? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("Operation canceled.")
            return

    video_object = VideoFileClip(video_path)
    video_object.audio.write_audiofile(filename=output_path)
    print(f"Audio extracted to {output_path}")

def get_frames(video_path, output_dir=None):
    """Extract frames from video with progress bar"""
    if output_dir is None:
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        output_dir = f"output/extracted_{base_name}"

    if os.path.exists(output_dir):
        overwrite = input(f"The folder '{output_dir}' already exists. Do you want to overwrite it? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("Operation canceled.")
            return

    os.makedirs(output_dir, exist_ok=True)
    video_object = VideoFileClip(video_path)
    total_frames = int(video_object.fps * video_object.duration)
    for index, frame in tqdm(enumerate(video_object.iter_frames()), total=total_frames, desc="Extracting Frames"):
        img = Image.fromarray(frame, 'RGB')
        img.save(f'{output_dir}/{index}.png')
    print(f"Frames saved to {output_dir}")

def combine_audio_video(video_frames_dir, audio_path, output_path="output/combined_video.mkv", fps=30):
    """Combine frames and audio into a video"""
    video_path_temp = "output/combined_video_only.mkv"
    os.system(f"ffmpeg -framerate {fps} -i \"{video_frames_dir}/%d.png\" -codec copy {video_path_temp}")
    os.system(f"ffmpeg -i {video_path_temp} -i \"{audio_path}\" -codec copy {output_path}")
    print(f"Combined video saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python ExtractAndCombine.py getvideo [video_path] [output_path (optional)]")
        print("  python ExtractAndCombine.py getaudio [video_path] [output_path (optional)]")
        print("  python ExtractAndCombine.py getframes [video_path] [output_dir (optional)]")
        print("  python ExtractAndCombine.py combine [frames_dir] [audio_path] [output_path (optional)] [fps (optional)]")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "getvideo":
        video_path = sys.argv[2]
        output_path = sys.argv[3] if len(sys.argv) > 3 else "output/video_only.mp4"
        get_video(video_path, output_path)

    elif command == "getaudio":
        video_path = sys.argv[2]
        output_path = sys.argv[3] if len(sys.argv) > 3 else None
        get_audio(video_path, output_path)

    elif command == "getframes":
        video_path = sys.argv[2]
        output_dir = sys.argv[3] if len(sys.argv) > 3 else None
        get_frames(video_path, output_dir)

    elif command == "combine":
        frames_dir = sys.argv[2]
        audio_path = sys.argv[3]
        output_path = sys.argv[4] if len(sys.argv) > 4 else "output/combined_video.mkv"
        fps = sys.argv[5] if len(sys.argv) > 5 else 30
        combine_audio_video(frames_dir, audio_path, output_path, fps)

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)