import subprocess
import os
import shutil

### Summary: For each sibling folder, combine its contents into a single .mkv file and save it in the outer directory.

### Edit the path to your ffmpeg executable here
ffmpeg_path = r''





# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# For each (folder) entry in the current directory (e.g. sibling folders)
for entry in os.listdir(current_dir):
    # Ignore .git folder
    if entry == '.git':
        continue 

    # Construct the full path to the entry
    path = os.path.join(current_dir, entry)
    if os.path.isdir(path):
        # Get file paths
        if os.path.isfile(os.path.join(current_dir, entry,'s1q1.m4s')):
            audio = os.path.join(current_dir, entry,'s0q1.m4s')
            video1 = os.path.join(current_dir, entry,'s1q1.m4s')
            video2 = os.path.join(current_dir, entry,'s2q1.m4s')
            
        else:
            audio = os.path.join(current_dir, entry,'s0q1.mp4')
            video1 = os.path.join(current_dir, entry,'s1q1.mp4')
            video2 = os.path.join(current_dir, entry,'s2q1.mp4')
            

        # Specify output file path
        output = os.path.join(current_dir, f'Lecture {entry}.mkv')

        
        ## Choose what videos to combine
        if os.path.isfile(audio) and os.path.isfile(video1) and os.path.isfile(video2):
            cmd = [
                ffmpeg_path,
                '-i', audio,
                '-i', video1,
                '-i', video2,
                '-map', '0:a:0',    # map audio stream
                '-map', '1:v:0',    # map second video stream
                '-map', '2:v:0',    # map first video stream
                '-c', 'copy',       # copy all streams without re-encoding
                output
            ]
        elif os.path.exists(audio) and os.path.exists(video1):
            # Only use the second video and audio
            cmd = [
                ffmpeg_path,
                '-i', audio,
                '-i', video1,
                '-map', '0:a:0',    # map audio stream
                '-map', '1:v:0',    # map first video stream
                '-c', 'copy',       # copy all streams without re-encoding
                output
            ]
        elif os.path.exists(audio) and os.path.exists(video2):
            # Only use the second video and audio
            cmd = [
                ffmpeg_path,
                '-i', audio,
                '-i', video2,
                '-map', '0:a:0',    # map audio stream
                '-map', '1:v:0',    # map first video stream
                '-c', 'copy',       # copy all streams without re-encoding
                output
            ]
        else:
            raise FileNotFoundError(f"Required files not found. Please manually specify the cmd property.")



        # Run the combine command
        subprocess.run(cmd, check=True)

        # Delete folder containing the original files (Requires admin privileges)
        try:
            shutil.rmtree(path) ####### TODO: Not working
        except:    
            print("Failed to delete: ", path)