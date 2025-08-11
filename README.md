
Intro:
Welcome to this small project that allows you to download videos from echo360.
This program requires that you can access the videos in your normal browsing but overcomes the issue that there is no download button.
However, it still requires some technical skill.
This program has two parts. First, that which downloads two video streams and one audio stream. Second, one that combines the downloaded files in to a single .mkv file.

History:
I finished university and wanted to make a personal copy of all of the resources that I had access to, just incase access is terminated at some point in the future.
I would like to make it more automated at some point.

How to:
Part 1:-
1.1. Open the copy_videos.py
1.2. Fill-in/replace the details in the top section
1.3. Run the Python file
1.4. Find the downloaded files in the relative folder defined in the Python file

Part 2:-
2.1. Use convert_to_mkv.py to combine the files in each relative folder into a single .mkv file in the outer folder. 

Credits:
Python packages: os, requests, urllib
ChatGTP 4o for rapid prototyping.
carnferg01 for directing and debugging.