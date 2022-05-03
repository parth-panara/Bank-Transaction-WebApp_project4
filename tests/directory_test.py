
import os
from app.db import config


# this test checks if the uploads folder is created for csv file#15
def test_create_uploads_folder():
    root = config.Config.BASE_DIR
    # set the name of the apps uploads folder for csv file
    uploadfolder = os.path.join(root, '..', config.Config.UPLOAD_FOLDER)
    # make a directory if it doesn't exist
    assert os.path.exists(uploadfolder) == True