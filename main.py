from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from plyer import flashlight

class FlashApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, orientation='vertical', spacing=20, padding=40)

        self.status = Label(text="اضغط للتشغيل", font_size='24sp', color=(0,0,1,1))
        self.add_widget(self.status)

        btn_on = Button(text="تشغيل 🔦", size_hint_y=0.3, background_color=(0, 0.8, 0, 1))
        btn_on.bind(on_press=self.turn_on)
        self.add_widget(btn_on)

        btn_off = Button(text="إيقاف ⭕", size_hint_y=0.3, background_color=(0.8, 0, 0, 1))
        btn_off.bind(on_press=self.turn_off)
        self.add_widget(btn_off)

    def turn_on(self, instance):
        try:
            flashlight.on()
            self.status.text = "يعمل ✅"
            self.status.color = (0, 0.8, 0, 1)
        except Exception as e:
            self.status.text = f"خطأ: {str(e)}"

    def turn_off(self, instance):
        try:
            flashlight.off()
            self.status.text = "متوقف ⭕"
            self.status.color = (0.8, 0, 0, 1)
        except Exception as e:
            self.status.text = f"خطأ: {str(e)}"

class MainApp(App):
    def build(self):
        return FlashApp()

if __name__ == '__main__':
    MainApp().run()
