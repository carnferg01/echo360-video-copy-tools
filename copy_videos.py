import os
import requests
from urllib.parse import urljoin

##################################################################################################################
### Make changes to this section to suit your needs ##############################################################
##################################################################################################################


# User edits:
output_directory = '2'

# Plug in the base URL of the echo360 page
url_folder='''
https://content.echo360.org.uk/0000.75f1696a-068b-4ce7-83c0-b03455c0fa36/c19531bd-e5e4-4bb7-b805-c0d9f46ba4db/1/
'''

# Plug in the cookies from your browser
cookies = {
"CloudFront-Key-Pair-Id":"APKAIPMYRDQXV3PXG2XA",
"CloudFront-Policy":"eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vKi5lY2hvMzYwLm9yZy51ay8qNzVmMTY5NmEtMDY4Yi00Y2U3LTgzYzAtYjAzNDU1YzBmYTM2LyoiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NTQ5MjY4NjB9fX1dfQ__",
"CloudFront-Signature":"q3gcKnfPgeRDmC-P6hbsJM7p1k38ZTs25-C8Gv1iCdc0Fky1-Ks23KWP6fy21jOAC2l3NPlQZSvNjF~nR82CKDYnKhciy2ltxty3ZdmSRoj-1usD-a7LpoHgRY~eUqEAuCiKvBnG-JtWwtVVMwQD3z2G1Mrd0mvsulytqRxmN0ezpzgUjReswltzaKGwIYjsthxUTurLRI-O1hVHhqlOTVrVNXc6sjk0i8kG4DWFTBhBc2k1HS8S9q091nsmO-0FOiI~PQx2aa6-72y56hA3FoEArHYzqP90Xf7YApqHPK60gnICBFk8SWmM2~a85mBMwXqDPQpXRd63X4aSTkJTwQ__",
"CloudFront-Tracking2":"MTc1NDkyMzI2MDM4NOKQn+KQn+KQn+KQnzc1ZjE2OTZhLTA2OGItNGNlNy04M2MwLWIwMzQ1NWMwZmEzNuKQn+KQn+KQn+KQny5lY2hvMzYwLm9yZy51a+KQn+KQny8",
"ECHO_JWT":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJFY2hvMzYwLkF1dGhuIiwic3ViIjoiczIxODA2ODRAZWQuYWMudWsiLCJleHAiOjE3NTQ5Njc4NTEsImlhdCI6MTc1NDkyMTA1MSwianRpIjoiMzAyZDVhMDAtMzY4Mi00YjMxLWE1YzAtZjY2MGRiNDM5M2Y4IiwiY29udGVudCI6eyJzZXNzaW9uSWQiOiI0YTVlZGZhOS01ZWE4LTRlMGYtYWVjMy1kZmU5NTc4OWQ0MjkiLCJ1c2VySWQiOiIwMjkyZjI3OC0wZTBkLTRiYmEtOWY2YS0xMzkwY2I0NzZmNzUiLCJpbnN0aXR1dGlvbklkIjoiNzVmMTY5NmEtMDY4Yi00Y2U3LTgzYzAtYjAzNDU1YzBmYTM2IiwiZG9tYWluIjoiZWNobzM2MC5vcmcudWsiLCJrZXlJZCI6IjVkODA3YzQ3LWRkMzEtNDc2My04ZTRhLTliN2YxNTEyOTU4YyIsInNzb0lkIjoiczIxODA2ODRAZWQuYWMudWsiLCJycXJvbGUiOiJzdHVkZW50In19.rhysD8jLAfcuyrMTrhID2arYY5Sdr4dpp_AiQchkXkE",
"i18next":"en-GB",
"PLAY_SESSION":"90e8c344552706401ba9b5fa522977adb73ad731-inIframe=false&ltiContextId=ff228a99578c4ceaa32a015e9ff7f43c&returnUrl=https%3A%2F%2Fwww.learn.ed.ac.uk%2Fwebapps%2Fblackboard%2Fexecute%2Fblti%2FlaunchReturn%3Fcourse_id%3D_117318_1%26content_id%3D_10023335_1%26toGC%3Dfalse%26nonce%3D28ae468dc3cc4c9398812e4ebfe11b9c%26launch_id%3D4e59379f-164b-4fe7-85bb-1db9f53cf0a0%26link_id%3D_10023335_1%26launch_time%3D1754921050653&lmsResourceId=_10023335_1&ltiRequestRoute=Other&isHomeworkContentRequest=false&role=student&LTI=true&institution=75f1696a-068b-4ce7-83c0-b03455c0fa36&d2LEmbed=false&isSecureLink=false&courseSectionSourcedId=&isContentItemMessageRequest=false&externalLtiHierarchyId=&isAuthEmbedSupported=false&lmsName=Blackboard&roles=Student&productFamilyCode=Blackboard&csrfToken=1bdcbd03dde083b833abd198ccf8e30b8f018517-1754921051736-b6f5cec299d4fd6dfb2dd234&contextTitle=Nuclear+Physics+%282024-2025%29%5BSEM2%5D&isEmbedContentRequest=false&lmsProfileId=badffe4a-e87d-419a-8fc7-6ad53ee878b2&contentItemMessageData=&sessionExpiresAt=2025-08-11T18%3A04%3A11.686Z&lmsPluginVersion=&contextLabel=PHYS110412024-5SV1SEM2&user=0292f278-0e0d-4bba-9f6a-1390cb476f75&msTokenState=&sessionCode=",
}


###################################################################
### Do not change anything below this line
###################################################################

# Choose the file type on the server (if one doesn't work try the other)
file_names=['s0q1.m4s','s1q1.m4s','s2q1.m4s']
#file_names=['s0q1.mp4','s1q1.mp4','s2q1.mp4']

# List urls for the files
urls= [urljoin(url_folder, file_name) for file_name in file_names]

# Local dir configuration
current_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(current_dir, output_directory), exist_ok=True)

# Download the files
print("Download started")
for i in range(len(file_names)):
    response = requests.get(urls[i], cookies=cookies, stream=True)
    response.raise_for_status()  # Raises HTTPError for bad responses

    with open(os.path.join(current_dir, output_directory, file_names[i]), 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print(f"Downloaded: {file_names[i]}")
    print(f"Progress: {i+1}/{len(file_names)}")
    print()