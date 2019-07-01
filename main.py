from kivy.app import App # подключаем модуль kivy
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

class BoxApp(App):
	def build(self):
		al = AnchorLayout()
		bl = BoxLayout(orientation = 'vertical', size_hint=[.4, .4])

		bl.add_widget(TextInput())
		bl.add_widget(TextInput())
		bl.add_widget(Button(text="Enter"))

		al.add_widget(bl)
		return al
# следующей строкой мы указываем, что приложение было запущено как самостоятельное
# приложение, а не кк какой-то отдельный модуль


if __name__ == "__main__":
	BoxApp().run()