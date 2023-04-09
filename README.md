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
