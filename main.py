from kivy.app import App # подключаем модуль kivy
from kivy.uix.button import Button


from kivy.uix.anchorlayout import AnchorLayout

class BoxApp(App):
	def build(self):

		bl = AnchorLayout(anchor_x = 'left',anchor_y = 'top')

		bl.add_widget(Button(text="Button" , size_hint = [.5, .5]))

		return bl
# следующей строкой мы указываем, что приложение было запущено как самостоятельное
# приложение, а не кк какой-то отдельный модуль


if __name__ == "__main__":
	BoxApp().run()