import dropbox
from keys import app_key
#keys is your dropbox api_key

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_delete(file_to)
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = app_key
    transferData = TransferData(access_token)

    file_from = 'health.db'
    file_to = '/Health_DB/health.db'

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()