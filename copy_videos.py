from os import makedirs, path
from requests import get
from urllib.parse import urljoin

##################################################################################################################
### Make changes to this section to suit your needs ##############################################################
##################################################################################################################


# User edits:
output_directory = '1'

# Plug in the base URL of the echo360 page
# To find it: Goto Inspect -> Network -> Reload the page -> Search .m3u8 -> Click on any .m3u8 file -> Look at the Headers -> Look at the Request URL -> use everything before the s1_v.m3u8 (or similar)
url_folder='''
https://content.echo360.org.uk/0000.75f1696a-068b-4ce7-83c0-b03455c0fa36/a9441daf-a18f-4da6-bb4c-b2d8dd2b9d82/1/
'''

# Plug in the cookies from your browser
# To find it: Goto Inspect -> Application -> Storage -> Cookies -> Click on the echo360.org.uk domain
cookies = {
"CloudFront-Key-Pair-Id":"",
"CloudFront-Policy":"",
"CloudFront-Signature":"",
"CloudFront-Tracking2":"",
"ECHO_JWT":"",
"i18next":"",
"PLAY_SESSION":"",
}

# Choose the file type on the server
# If you get an error as follows, just try the other file type
# requests.exceptions.HTTPError: 403 Client Error: Forbidden for url: https://content.echo360.org.uk/0000.75f1696a-068b-4ce7-83c0-b03455c0fa36/cf043bc8-3cf4-419a-a609-6ecdade08c76/1/s2q1.m4s
file_names=['s0q1.m4s','s1q1.m4s','s2q1.m4s']
#file_names=['s0q1.mp4','s1q1.mp4','s2q1.mp4']



###################################################################
### Do not change anything below this line
###################################################################

# List urls for the files
urls= [urljoin(url_folder, file_name) for file_name in file_names]

# Local dir configuration
current_dir = path.dirname(path.abspath(__file__))
makedirs(path.join(current_dir, output_directory), exist_ok=True)

# Download the files

for i in range(len(file_names)):
    print("Downloading: ", file_names[i])
    response = get(urls[i], cookies=cookies, stream=True)
    response.raise_for_status()  # Raises HTTPError for bad responses

    with open(path.join(current_dir, output_directory, file_names[i]), 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print(f"Downloaded: {file_names[i]}")
    print(f"Progress: {i+1}/{len(file_names)}")
    print()