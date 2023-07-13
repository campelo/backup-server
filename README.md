[[_TOC_]]

# backup-server

## config.py
Create a config.py to hold your server configurations.

**AUTHORIZED_ACCOUNTS** is used to limitate what accounts can use this server
**CLIENT_ID** application id registered on google.
**CLIENT_SECRET** application secret registered for this application
**REDIRECT_URI** application redirect uri registered on google
**UPLOAD_FOLDER** local folder name to save documents.

Your **config.py** should look like this.

```python
AUTHORIZED_ACCOUNTS = ["email1@gmail.com", "email2@gmail.com"]
CLIENT_ID = 'client-id'
CLIENT_SECRET = 'client-secret'
REDIRECT_URI = 'redirect-uri'
UPLOAD_FOLDER = '/home/{usr}/backup'
```

## Dependencies
```bash
sudo apt-get update
sudo apt-get install python3-pip
```

It might be necessary to add this repository
```bash
sudo add-apt-repository universe
```

exifread
```bash
pip install exifread
```

ffprobe
``` bash
sudo apt-get install ffmpeg
```

# file-manager

Move/organize all media files on classified subfolders year/month/day. Metadata is used to find all date information to create those folders.

## Exemple

If we use /my-folder/pictures all data will be moved to /my-folder/pictures/yyyy/mm/dd.

## Running

```
python3 file-manager.py /mnt/c/Users/myUser/Pictures
```