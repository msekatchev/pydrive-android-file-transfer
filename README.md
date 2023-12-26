# pydrive-android-file-transfer
Python scripts for transferring files from an Android phone to Google Drive via PyDrive through Termux

`backup.py` uploads all of the files in `local_folder_path` to a folder titled `drive_folder_title` that it creates on the Google Drive home page.

## Setup
Requires:
### Termux
- Download on Google Play Store.
- Setup access to local phone storage by executing `termux-setup-storage`.
  - See [Termux Wiki](https://wiki.termux.com/wiki/Internal_and_external_storage) for details.
### Python
- Execute `pkg install python`.
### PyDrive
- Execute `pip install pydrive`.
### Google Drive OAuth
- Obtain a `client_secrets.json` file by following the instructions [here](https://pythonhosted.org/PyDrive/quickstart.html#authentication).
- Add your Google Account as a test user by following the instructions [here](https://stackoverflow.com/questions/75454425/access-blocked-project-has-not-completed-the-google-verification-process).

## Running `backup.py`
- Modify lines `5` and `6` of `backup.py` appropriately:
```python
local_folder_path  = "../Screenshots" # folder from which to upload
drive_folder_title = "Screenshots_Backup" # new folder to upload to
```
- Place the `backup.py` script and the `client_secrets.json` in a desired location on the phone.
- Navigate to this location and execute `python3 backup.py`.
