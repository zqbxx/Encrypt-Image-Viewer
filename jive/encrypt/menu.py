from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar, QMainWindow

from keymanager.dialogs import KeyMgrDialog


def add_encrypt_menu(menubar: QMenuBar, parent: QMainWindow):

    def _open_key_mgr_dialog():
        open_key_mgr_dialog(parent)

    def _open_encrypt_dialog():
        open_encrypt_dialog(parent)

    def _open_decrypt_dialog():
        open_decrypt_dialog(parent)

    encryptMenu = menubar.addMenu("加密/解密")

    key_mgr_act = QAction("密钥管理", parent)
    key_mgr_act.triggered.connect(_open_key_mgr_dialog)

    encrypt_act = QAction("加密图片", parent)
    encrypt_act.triggered.connect(_open_encrypt_dialog)

    decrypt_act = QAction("解密图片", parent)
    decrypt_act.triggered.connect(_open_decrypt_dialog)

    encryptMenu.addAction(key_mgr_act)
    encryptMenu.addAction(encrypt_act)
    encryptMenu.addAction(decrypt_act)


def open_key_mgr_dialog(parent: QMainWindow):
    dialog = KeyMgrDialog(parent)
    dialog.exec_()


def open_encrypt_dialog(parent: QMainWindow):
    pass


def open_decrypt_dialog(parent: QMainWindow):
    pass
