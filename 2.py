from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Choose book'
            on_press: root.manager.current = 'books'
        Button:
            text: 'Quit'
            on_press: app.stop()

<BooksScreen>:
    BoxLayout:
        Button:
            text: 'Starlight 11'
            on_press: root.manager.current = 'st11'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'menu'
            
<Starlight11>:
    BoxLayout:
        Button:
            text: 'Choose module'
            on_press: root.manager.current = 'st11_modules'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'books'

<ST11_ModulesScreen>:
    BoxLayout:
        Button:
            text: 'Module 1'
            on_press: root.manager.current = 'st11_module_1'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'st11'
            

<ST11_Module1Screen>:
    BoxLayout:
        Button:
            text: 'Unit 1.1'
            on_press: root.manager.current = 'st11_1-1'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'st11_modules'

<ST11_11Screen>:  
    BoxLayout:      
        Button:
            text: 'Reading'
            on_press: root.manager.current = 'reading'
        Button:
            text: 'Learning'
            on_press: root.manager.current = 'learning'            

<ReadingScreen>:
    BoxLayout:
        Button:
            text: 'Ex 1'
            on_press: root.manager.current = 'r_st11_11_1'
        Button:
            text: 'Ex 2'
        Button:
            text: 'Back'
            on_press: root.manager.current = 'st11_module_1'
            
<LearningScreen>:
    BoxLayout:
        Button:
            text: 'Ex 1'
            on_press: root.manager.current = 'l_st11_11_1'
        Button:
            text: 'Ex 2'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'st11_module_1' 
               
<R_11_11_1>:
    BoxLayout:
        Button:
            text: 'Play'
            on_press: app.button1Callback()
        Label:
            text: "Irish Rovers. *Some text*"
        Button:
            text: 'Back'
            on_press: app.stopMusic()
            on_press: root.manager.current = 'reading'
<L_11_11_1>:
    BoxLayout:
        Label:
            text: "Dog"
        Label:
            text: "|dɒɡ|"
        Label:
            text: "Собака"
        Button:
            text: "Pronounce"
                    
""")

# Declare both screens


class MenuScreen(Screen):
    pass


class ReadingScreen(Screen):
    pass


class ST11_11Screen(Screen):
    pass


class ST11_Module1Screen(Screen):
    pass


class LearningScreen(Screen):
    pass


class Starlight11(Screen):
    pass


class ST11_ModulesScreen(Screen):
    pass


class BooksScreen(Screen):
    pass


class R_11_11_1(Screen):
    pass


class L_11_11_1(Screen):
    pass

# Create the screen manager


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ReadingScreen(name='reading'))
sm.add_widget(BooksScreen(name='books'))
sm.add_widget(Starlight11(name='st11'))
sm.add_widget(ST11_ModulesScreen(name="st11_modules"))
sm.add_widget(ST11_11Screen(name='st11_1-1'))
sm.add_widget(LearningScreen(name='learning'))
sm.add_widget(ST11_Module1Screen(name='st11_module_1'))
sm.add_widget(R_11_11_1(name="r_st11_11_1"))
sm.add_widget(L_11_11_1(name="l_st11_11_1"))


class TestApp(App):

    def build(self):
        self.sound = SoundLoader.load('11_1_1_1.mp3')
        return sm

    def button1Callback(self):
        self.sound.play()

    def stopMusic(self):
        self.sound.stop()


if __name__ == '__main__':
    TestApp().run()
