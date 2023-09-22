import os
import sys

from PySide6.QtCore import QThread, QTimer, Signal
from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QApplication

from API.IPAPI import IPAPI
from API.weatherAPI import WeatherAPI
from entity.WeatherInfo import WeatherInfo
from tools.filetool import FileTool
from util import get_base_dir
from widget.setting_pane import SettingDialog
from widget.weather import MainWindow

app = QApplication(sys.argv)
window = MainWindow()


def get_current_city():
    """
    获取当前选择的城市
    :return: str, 当前选择的城市
    """
    return list(WeatherAPI.city_url_dict.keys())[window.cities.currentIndex()]


current_city = get_current_city()  # 当前城市


class GetWeatherThread(QThread):
    data_ready = Signal(WeatherInfo)  # 数据准备好的信号
    data_error = Signal(str)  # 错误信号

    def __init__(self, city_name, parent=None):
        super(GetWeatherThread, self).__init__(parent)
        self.city_name = city_name

    def run(self) -> None:
        data = WeatherAPI.get_weather_by_city_name(self.city_name)
        if type(data) == WeatherInfo:
            self.data_ready.emit(data)
        else:
            self.data_error.emit(data)


class GetLocationThread(QThread):
    data_ready = Signal()

    def __init__(self, parent=None):
        super(GetLocationThread, self).__init__(parent)

    def run(self) -> None:
        global current_city
        current_city = IPAPI.get_location_by_ip(IPAPI.get_my_ip())
        self.data_ready.emit()


def get_weather():
    """
    执行获取天气线程
    """
    window.cities.setEditText(current_city)

    t = GetWeatherThread(current_city, window)

    t.data_ready.connect(window.show_data)  # 成功数据
    t.data_error.connect(window.show_tip)  # 错误信息
    t.start()


def start_timer():
    """
    开启定时器,隔一段时间查询一次,获取最新的天气信息
    """
    if timer.isActive():
        timer.stop()  # 停止计时
    global current_city
    current_city = get_current_city()  # 获取当前城市
    get_weather()
    timer.start(request_duration)  # 重新计时


def connect_signals_slots():
    """
    连接信号与槽
    """
    glt = GetLocationThread(window)
    glt.data_ready.connect(get_weather)
    glt.start()
    timer.start(request_duration)

    window.get_weather_signal.connect(start_timer)

    def show_setting():
        setting = SettingDialog(window)
        setting.request_duration_spin.setValue(FileTool.get_config_value(FileTool.Keys.REQUEST_DURATION))
        setting.opacity_slider.setValue(FileTool.get_config_value(FileTool.Keys.OPACITY) * 10)
        setting.opacity_slider.valueChanged.connect(lambda value: window.setWindowOpacity(value / 10))

        def set_duration(value):
            global request_duration
            request_duration = value * 1000 * 60

        setting.request_duration_spin.valueChanged.connect(set_duration)

        setting.show()

    window.show_setting_pane_signal.connect(show_setting)


def load_config():
    """
    加载配置文件
    """
    config = FileTool.load_configs()
    window.setWindowOpacity(config[FileTool.Keys.OPACITY])


def main():
    """
    主方法
    """
    window.setWindowTitle('Godbei天气')
    window.setWindowIcon(QPixmap(os.path.join(get_base_dir(), 'source', 'img', 'icon.ico')))

    connect_signals_slots()
    load_config()

    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    app.setStyle('Fusion')
    # 定时器
    timer = QTimer(window)
    timer.timeout.connect(get_weather)
    window.setAttribute(Qt.WA_TransparentForMouseEvents, True)
    # 请求间隔
    request_duration = FileTool.get_config_value(FileTool.Keys.REQUEST_DURATION) * 1000 * 60

    main()
