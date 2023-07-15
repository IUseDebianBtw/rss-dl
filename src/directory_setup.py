import os
import logging

def setup_directory(download_dir):
    if os.path:
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
            logging.info(f'Download directory did not exist. Created directory: {download_dir}')
        else:
            logging.info(f'Download directory exists. No need to create one.')
    else:
        logging.info(f'Could not create download directory. Assuming you are using Docker and the directory already exists.')