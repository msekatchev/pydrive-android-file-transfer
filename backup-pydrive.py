import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

local_folder_path = "/data/data/com.termux/files/home/storage/dcim/Camera" # folder from which to upload
drive_folder_title = "Camera" # new folder to upload to
relocate_uploaded_files = False # set to true if you want photos to be moved to a different location after upload
final_folder_title = "../camera-roll" # where photos are moved after being uploaded (if `relocate_uploaded_files` is True)


# Authenticate and get GoogleDrive client
gauth = GoogleAuth()
gauth.LocalWebserverAuth() # will require site login for approval
drive = GoogleDrive(gauth)

# create folder on the drive
drive_folder = drive.CreateFile({'title': drive_folder_title, 'mimeType': 'application/vnd.google-apps.folder'})
drive_folder.Upload()

# Upload files to the created folder
count = 1
for root, dirs, files in os.walk(local_folder_path):
    for file_name in files:
        print(count, "\t", file_name)
        count = count+1
        
        # Create empty file
        local_file_path = os.path.join(root, file_name)
        drive_file = drive.CreateFile({'title': file_name, 'parents': [{'id': drive_folder['id']}]})

        # Set the content of the file
        drive_file.SetContentFile(local_file_path)

        # Upload the file
        drive_file.Upload()

        if relocate_uploaded_files:
            os.rename(local_folder_path+"/"+ file_name, final_folder_title+"/"+file_name) 
