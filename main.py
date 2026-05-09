from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from plyer import flashlight

class FlashUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, orientation='vertical', spacing=30, padding=50)
        self.lbl = Label(text="جاهز", font_size='28sp', color=(0,0,1,1))
        self.add_widget(self.lbl)
        
        btn = Button(text="تشغيل الفلاش 🔦", size_hint_y=0.3)
        btn.bind(on_press=self.toggle)
        self.add_widget(btn)

    def toggle(self, instance):
        try:
            if "يعمل" not in self.lbl.text:
                flashlight.on()
                self.lbl.text = "يعمل ✅"
                self.lbl.color = (0, 0.8, 0, 1)
            else:
                flashlight.off()
                self.lbl.text = "متوقف ⭕"
                self.lbl.color = (0.8, 0, 0, 1)
        except Exception as e:
            self.lbl.text = f"خطأ: {e}"

class MainApp(App):
    def build(self):
        return FlashUI()

if __name__ == '__main__':
    MainApp().run()
