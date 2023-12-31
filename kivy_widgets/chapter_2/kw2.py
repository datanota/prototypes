
from utilities.common import Common
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class KivyWidgetsContent(BoxLayout):
    pass


class KW2App(MDApp, Common):
    def __init__(self):
        super().__init__()

    # ############################################################### navbar top-right tip

    def tip_dialog(self, title, tip):
        dialog = MDDialog(
            title=title,
            text='[color=222222]' + tip,
            buttons=[
                MDFlatButton(
                    text='Dismiss',
                    theme_text_color='Custom',
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: dialog.dismiss()
                )
            ],
        )
        dialog.open()

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        self.title = 'kivy-widgets - ch2'
        return KivyWidgetsContent()


if __name__ == '__main__':
    KW2App().run()



