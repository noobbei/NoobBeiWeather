import os.path
import sys

from PySide6.QtCore import QPoint, QRect, Qt, Signal
from PySide6.QtGui import QFont, QPixmap,  QMouseEvent, QPaintEvent, QPainter, QWindow
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QToolTip, QCompleter, QPushButton

from API.weatherAPI import WeatherAPI
from entity.WeatherInfo import WeatherInfo
from source.ui_weather import Ui_Form
from util import get_base_dir
from widget import dealMouseEvent


class MainWindow(QWidget, Ui_Form):
    # 信号
    get_weather_signal = Signal(str)  # 获取指定城市的天气
    show_setting_pane_signal = Signal()  # 显示设置面板

    def __init__(self, parent=None, *args, **kwargs):
        super(MainWindow, self).__init__(parent, *args, **kwargs)

        self.isLocked = False
        self.setWindowFlag(Qt.FramelessWindowHint)
        path = os.path.join(get_base_dir(), 'source', 'img', 'background_mask.png')
        self.background = QPixmap(path)
        self.background = self.background.scaled(400, 340)
        self.setMask(self.background.mask())

        # 信息提示框
        self.tt = QToolTip(self)

        self.setupUi(self)

        self.setup_ui()

    def setup_ui(self):
        font_12 = QFont('微软雅黑', 12)
        for widget in self.findChildren(QLabel):
            widget.setFont(font_12)
            widget.setStyleSheet('color:white')

        self.tt.setFont(QFont('微软雅黑', 16))

        font_14 = QFont('微软雅黑', 14)
        self.name.setFont(QFont('微软雅黑', 20))
        self.week.setFont(font_14)
        self.temperature.setText(f'<span style=" font-size:35pt;">20</span><span style=" font-size:30pt; '
                                 f'vertical-align:super;">℃</span>')
        self.weather.setFont(font_14)

        self.cities.addItems(WeatherAPI.city_url_dict.keys())  # 设置城市数据
        self.cities.setCompleter(QCompleter(WeatherAPI.city_url_dict.keys(), self))

    def paintEvent(self, event: QPaintEvent) -> None:
        # painter = QPainter(self)
        # painter.drawPixmap(0, 0, self.width(), self.height(), self.background)
        pass

    # region 槽函数
    def setLocked(self, isLocked: bool):
        if self.isLocked == isLocked:
            return

        self.isLocked = isLocked
        self.setAttribute(Qt.WA_TransparentForMouseEvents, isLocked)

    def show_data(self, wi: WeatherInfo):
        """
        展示数据
        :param wi: WeatherIno, 天气数据对象
        """

        self.name.setText(wi.name)

        self.week.setText(wi.week)

        self.weather.setText(wi.weather)

        self.temperature.setText(f'<span style=" font-size:35pt;">{wi.temperature}</span><span style=" font-size:30pt; '
                                 f'vertical-align:super;">℃</span>')

        self.temperature_range.setText(wi.temperature_range)

        pix = QPixmap()
        pix.loadFromData(wi.weather_img)
        self.weather_img.setPixmap(pix)

        self.humidity.setText(wi.humidity)

        self.wind_direction.setText(wi.wind_direction)

        self.ultraviolet_ras.setText(wi.ultraviolet_rays)

        self.air_quality.setText(wi.air_quality)

        self.pm.setText(wi.pm)

        self.sunrise_time.setText('日出:' + wi.sunrise_time)

        self.sunset_time.setText('日落:' + wi.sunset_time)

    def show_tip(self, tip):
        """
        展示错误信息
        :param tip: str, 错误信息
        """
        self.tt.showText(self.change_city.mapToGlobal(QPoint(0, 25)), tip, self, QRect(0, 0, 100, 100), 2000)

    def get_weather(self, index):
        print(index)
        cites = list(WeatherAPI.city_url_dict.keys())
        self.get_weather_signal.emit(cites[index])

    def show_setting_pane(self):
        self.show_setting_pane_signal.emit()

    def pin_main_window(self, pin):
        """
        置顶或取消置顶
        :param pin: bool, 是否置顶
        """
        wh = self.windowHandle()
        if pin:
            wh.setFlags(wh.flags() | Qt.WindowStaysOnTopHint)
            tooltip = '取消置顶'
        else:
            wh.setFlags(wh.flags() & ~Qt.WindowStaysOnTopHint)
            tooltip = '置顶'
        self.pin_btn.setToolTip(tooltip)

    # endregion

    def mousePressEvent(self, event: QMouseEvent):
        """重写鼠标点击事件，点击主面板之后，让所有其他面板隐藏"""
        dealMouseEvent.mousePressEvent(self, event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        dealMouseEvent.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        dealMouseEvent.mouseReleaseEvent(self, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
