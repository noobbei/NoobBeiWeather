import sys

from PySide6.QtWidgets import QApplication, QDialog

from source.ui_setting import Ui_Dialog
from tools.filetool import FileTool


class SettingDialog(QDialog, Ui_Dialog):

    def __init__(self, parent=None, *args, **kwargs):
        super(SettingDialog, self).__init__(parent, *args, **kwargs)

        self.setupUi(self)
        self.setup_ui()
        self.func_list()

    def setup_ui(self):
        pass

    def func_list(self):
        pass

    def save_config(self):
        FileTool.set_config_value(FileTool.Keys.OPACITY, self.opacity_slider.value() / 10)
        FileTool.set_config_value(FileTool.Keys.REQUEST_DURATION, self.request_duration_spin.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = SettingDialog()
    window.show()

    sys.exit(app.exec())
