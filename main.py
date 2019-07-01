from kivy.app import App # подключаем модуль kivy
from kivy.uix.button import Button # подключаем модуль uix - кнопка
from kivy.uix.codeinput import CodeInput # подключаем модуль для добавления виджета "редактор кода"
from pygments.lexers import HtmlLexer # подклюаем модуль подсветки синтаксиса

# Создаём эземплары классов================================
from kivy.config import Config

from kivy.uix.floatlayout import FloatLayout

from kivy.uix.scatter import Scatter
# =========================================================

# Конфигурация окна приложения=============================
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 640)
Config.set('graphics', 'height', 480)
# =========================================================

# Создаём и описываем основной класс=======================
class MyApp(App):
	def build(self):
		# Создаём модуль scatter для поворота экрана 2 прикосновениями
		s = Scatter()
# Содаём FlostLayout, чтобы элементы выстроились в одну линию (wdgh,height)
		fl = FloatLayout(size = (300,300))
		s.add_widget(fl) # добавляем виджет в объект scatter
		fl.add_widget(Button(text = "Это моя первая кнопка", # Добавляем виджет кнопки в объект FloatLayout
			font_size = 16,
			on_press = self.btn_press,
			background_color = [1,0,0,1],
			background_normal = '',
			size_hint =(.5,.25),
			pos = (640/2 - 160,0)) , 480/2);

		return s
# описываем функцию - обработчик в теле класса MyApp
	
	def btn_press(self, instance):

		print("Кнопка нажата")
		instance.text = "Hello world"


if __name__ == "__main__":
	MyApp().run()