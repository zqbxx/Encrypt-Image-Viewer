from PySide6.QtGui import QPixmap

from keymanager.encryptor import decrypt_data, is_encrypt_data
from keymanager.utils import read_file
from keymanager.key import KEY_CACHE as cache


def load_encrypt_image(path: str) -> QPixmap:

    try:
        raw_data = read_file(path)

        image_data = raw_data

        if is_encrypt_data(raw_data):
            image_data = decrypt_data(cache.get_cur_key().key, raw_data)

        pixmap = QPixmap()

        pixmap.loadFromData(image_data)
    except Exception as e:
        print(e)

    return pixmap, len(image_data)
