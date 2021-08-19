from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)

        n = 3
        for i in range(n):
            button = Button(text=('Button No' + str(i+1)))

            self.add_widget(button)


class NewApp(App):

    def build(self):
        pass


if __name__ == '__main__':
    NewApp().run()
