import subprocess
import os
import shutil

current_dir = os.path.dirname(os.path.abspath(__file__))

for entry in os.listdir(current_dir):
    path = os.path.join(current_dir, entry)
    if os.path.isdir(path):
        # Input files
        if os.path.isfile(os.path.join(current_dir, entry,'s1q1.m4s')):
            video1 = os.path.join(current_dir, entry,'s1q1.m4s')
            video2 = os.path.join(current_dir, entry,'s2q1.m4s')
            audio = os.path.join(current_dir, entry,'s0q1.m4s')
        else:
            video1 = os.path.join(current_dir, entry,'s1q1.mp4')
            video2 = os.path.join(current_dir, entry,'s2q1.mp4')
            audio = os.path.join(current_dir, entry,'s0q1.mp4')
        output = os.path.join(current_dir, f'Lecture {entry}.mkv')

        ffmpeg_path = r'C:\Users\carnf\OneDrive\Documents\Programs (portable)\ffmpeg\ffmpeg-2025-05-21-git-4099d53759-full_build\bin\ffmpeg.exe'

        # ffmpeg command to combine the streams
        cmd = [
            ffmpeg_path,
            '-i', video1,
            '-i', video2,
            '-i', audio,
            '-map', '0:v:0',    # map first video stream
            '-map', '1:v:0',    # map second video stream
            '-map', '2:a:0',    # map audio stream
            '-c', 'copy',       # copy all streams without re-encoding
            output
        ]
        # cmd = [
        #     ffmpeg_path,
        #     '-i', video2,
        #     '-i', audio,
        #     '-map', '0:v:0',    # map first video stream
        #     '-map', '1:a:0',    # map audio stream
        #     '-c', 'copy',       # copy all streams without re-encoding
        #     output
        # ]

        # Run the command
        subprocess.run(cmd, check=True)

        # Delete folder
        print(path)
        shutil.rmtree(path) ####### TODO: Not working