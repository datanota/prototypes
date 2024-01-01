
import webbrowser
from kivy.core.window import Window
import datetime


class Common:
    def __init__(self):
        self.project = 'Datanota-Prototypes'

    @staticmethod
    def dn_ss():
        img_nm = datetime.datetime.now().strftime("%Y_%m%d%H%M_")
        Window.screenshot(name=img_nm + '.png')

    @staticmethod
    def dn_demo(web_address):
        webbrowser.open(web_address)
