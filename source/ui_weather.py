# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from source import weather_rc


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 340)
        Form.setStyleSheet(u"#Form{\n"
"	background-color: rgb(2, 137, 255);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title = QHBoxLayout()
        self.title.setObjectName(u"title")
        self.icon_label = QLabel(Form)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setPixmap(QPixmap(u":/title/img/icon.ico"))

        self.title.addWidget(self.icon_label)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.title.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.title.addItem(self.horizontalSpacer)

        self.setting_btn = QPushButton(Form)
        self.setting_btn.setObjectName(u"setting_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_btn.sizePolicy().hasHeightForWidth())
        self.setting_btn.setSizePolicy(sizePolicy)
        self.setting_btn.setMinimumSize(QSize(25, 25))
        self.setting_btn.setMaximumSize(QSize(25, 25))
        self.setting_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_btn.setStyleSheet(u"#setting_btn:hover{\n"
"	\n"
"	border-image: url(:/title/img/title/setting_hover.png);\n"
"}\n"
"#setting_btn:pressed{\n"
"	\n"
"	border-image: url(:/title/img/title/setting_pressed.png);\n"
"}\n"
"\n"
"#setting_btn{\n"
"	\n"
"	border-image: url(:/title/img/title/setting_normal.png);\n"
"}")

        self.title.addWidget(self.setting_btn)

        self.pin_btn = QPushButton(Form)
        self.pin_btn.setObjectName(u"pin_btn")
        sizePolicy.setHeightForWidth(self.pin_btn.sizePolicy().hasHeightForWidth())
        self.pin_btn.setSizePolicy(sizePolicy)
        self.pin_btn.setMinimumSize(QSize(25, 25))
        self.pin_btn.setMaximumSize(QSize(25, 25))
        self.pin_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.pin_btn.setStyleSheet(u"#pin_btn:hover{\n"
"	\n"
"	border-image: url(:/title/img/title/pin_hover.png);\n"
"}\n"
"\n"
"\n"
"#pin_btn:checked{\n"
"	\n"
"	border-image: url(:/title/img/title/pin_true.png);\n"
"}\n"
"\n"
"\n"
"\n"
"#pin_btn{\n"
"	\n"
"	border-image: url(:/title/img/title/pin_normal.png);\n"
"}")
        self.pin_btn.setCheckable(True)

        self.title.addWidget(self.pin_btn)

        self.minimize_btn = QPushButton(Form)
        self.minimize_btn.setObjectName(u"minimize_btn")
        sizePolicy.setHeightForWidth(self.minimize_btn.sizePolicy().hasHeightForWidth())
        self.minimize_btn.setSizePolicy(sizePolicy)
        self.minimize_btn.setMinimumSize(QSize(25, 25))
        self.minimize_btn.setMaximumSize(QSize(25, 25))
        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimize_btn.setStyleSheet(u"#minimize_btn:hover{\n"
"	\n"
"	border-image: url(:/title/img/title/minimize_icon_hover.png);\n"
"}\n"
"#minimize_btn:pressed{\n"
"	\n"
"	border-image: url(:/title/img/title/minimize_icon_pressed.png);\n"
"}\n"
"\n"
"#minimize_btn{\n"
"	\n"
"	border-image: url(:/title/img/title/minimize_icon_normal.png);\n"
"	\n"
"}")

        self.title.addWidget(self.minimize_btn)

        self.close_btn = QPushButton(Form)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
        self.close_btn.setMinimumSize(QSize(25, 25))
        self.close_btn.setMaximumSize(QSize(25, 25))
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_btn.setStyleSheet(u"#close_btn:hover{\n"
"	\n"
"	border-image: url(:/title/img/title/close_icon_hover.png);\n"
"}\n"
"#close_btn:pressed{\n"
"	\n"
"	border-image: url(:/title/img/title/close_icon_pressed.png);\n"
"}\n"
"\n"
"#close_btn{\n"
"	\n"
"	border-image: url(:/title/img/title/close_icon_normal.png);\n"
"}")

        self.title.addWidget(self.close_btn)


        self.verticalLayout_3.addLayout(self.title)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.name = QLabel(Form)
        self.name.setObjectName(u"name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)
        self.name.setMinimumSize(QSize(150, 0))
        self.name.setMaximumSize(QSize(16777215, 16777215))
        self.name.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_3.addWidget(self.name)

        self.change_city = QLabel(Form)
        self.change_city.setObjectName(u"change_city")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.change_city.sizePolicy().hasHeightForWidth())
        self.change_city.setSizePolicy(sizePolicy2)
        self.change_city.setMinimumSize(QSize(70, 0))
        self.change_city.setMaximumSize(QSize(70, 16777215))
        self.change_city.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_3.addWidget(self.change_city)

        self.cities = QComboBox(Form)
        self.cities.setObjectName(u"cities")
        sizePolicy.setHeightForWidth(self.cities.sizePolicy().hasHeightForWidth())
        self.cities.setSizePolicy(sizePolicy)
        self.cities.setMinimumSize(QSize(100, 0))
        self.cities.setMaximumSize(QSize(100, 16777215))
        self.cities.setEditable(True)

        self.horizontalLayout_3.addWidget(self.cities, 0, Qt.AlignBottom)

        self.horizontalLayout_3.setStretch(0, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.week = QLabel(Form)
        self.week.setObjectName(u"week")

        self.verticalLayout_3.addWidget(self.week)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.weather_img = QLabel(Form)
        self.weather_img.setObjectName(u"weather_img")
        self.weather_img.setMinimumSize(QSize(80, 80))
        self.weather_img.setMaximumSize(QSize(80, 80))
        self.weather_img.setScaledContents(True)

        self.horizontalLayout.addWidget(self.weather_img)

        self.temperature = QLabel(Form)
        self.temperature.setObjectName(u"temperature")
        self.temperature.setMinimumSize(QSize(80, 80))
        self.temperature.setMaximumSize(QSize(80, 80))

        self.horizontalLayout.addWidget(self.temperature)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.weather = QLabel(Form)
        self.weather.setObjectName(u"weather")

        self.verticalLayout.addWidget(self.weather)

        self.temperature_range = QLabel(Form)
        self.temperature_range.setObjectName(u"temperature_range")

        self.verticalLayout.addWidget(self.temperature_range)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.humidity = QLabel(Form)
        self.humidity.setObjectName(u"humidity")

        self.horizontalLayout_4.addWidget(self.humidity)

        self.wind_direction = QLabel(Form)
        self.wind_direction.setObjectName(u"wind_direction")

        self.horizontalLayout_4.addWidget(self.wind_direction)

        self.ultraviolet_ras = QLabel(Form)
        self.ultraviolet_ras.setObjectName(u"ultraviolet_ras")

        self.horizontalLayout_4.addWidget(self.ultraviolet_ras)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.air_quality = QLabel(Form)
        self.air_quality.setObjectName(u"air_quality")

        self.horizontalLayout_2.addWidget(self.air_quality)

        self.pm = QLabel(Form)
        self.pm.setObjectName(u"pm")

        self.horizontalLayout_2.addWidget(self.pm)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sunrise_time = QLabel(Form)
        self.sunrise_time.setObjectName(u"sunrise_time")

        self.verticalLayout_2.addWidget(self.sunrise_time)

        self.sunset_time = QLabel(Form)
        self.sunset_time.setObjectName(u"sunset_time")

        self.verticalLayout_2.addWidget(self.sunset_time)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)
        self.cities.currentIndexChanged.connect(Form.get_weather)
        self.minimize_btn.clicked.connect(Form.showMinimized)
        self.close_btn.clicked.connect(Form.close)
        self.setting_btn.clicked.connect(Form.show_setting_pane)
        self.pin_btn.toggled.connect(Form.pin_main_window)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.icon_label.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"godbei\u5929\u6c14", None))
#if QT_CONFIG(tooltip)
        self.setting_btn.setToolTip(QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.setting_btn.setText("")
#if QT_CONFIG(tooltip)
        self.pin_btn.setToolTip(QCoreApplication.translate("Form", u"\u7f6e\u9876", None))
#endif // QT_CONFIG(tooltip)
        self.pin_btn.setText("")
#if QT_CONFIG(tooltip)
        self.minimize_btn.setToolTip(QCoreApplication.translate("Form", u"\u6700\u5c0f\u5316", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.close_btn.setToolTip(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
        self.close_btn.setText("")
        self.name.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>XX\u5929\u6c14</p></body></html>", None))
        self.change_city.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u57ce\u5e02\u5217\u8868</span></p></body></html>", None))
        self.week.setText(QCoreApplication.translate("Form", u"2022\u5e7408\u670831\u65e5", None))
        self.weather_img.setText(QCoreApplication.translate("Form", u"\u5929\u6c14\u56fe\u7247", None))
        self.temperature.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:26pt;\">20</span><span style=\" font-size:26pt; vertical-align:super;\">\u2103</span></p></body></html>", None))
        self.weather.setText(QCoreApplication.translate("Form", u"\u5929\u6c14", None))
        self.temperature_range.setText(QCoreApplication.translate("Form", u"\u6e29\u5ea6\u8303\u56f4", None))
        self.humidity.setText(QCoreApplication.translate("Form", u"\u6e7f\u5ea6", None))
        self.wind_direction.setText(QCoreApplication.translate("Form", u"\u98ce\u5411", None))
        self.ultraviolet_ras.setText(QCoreApplication.translate("Form", u"\u7d2b\u5916\u7ebf", None))
        self.air_quality.setText(QCoreApplication.translate("Form", u"\u7a7a\u6c14\u8d28\u91cf", None))
        self.pm.setText(QCoreApplication.translate("Form", u"pm", None))
        self.sunrise_time.setText(QCoreApplication.translate("Form", u"\u65e5\u51fa\u65f6\u95f4", None))
        self.sunset_time.setText(QCoreApplication.translate("Form", u"\u65e5\u843d\u65f6\u95f4", None))
    # retranslateUi

