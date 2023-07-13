import os
import logging

def setup_directory(download_dir):
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        logging.info(f'Download directory did not exist. Created directory: {download_dir}')
    else:
        logging.info(f'Download directory exists. No need to create one.')
