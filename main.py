from kivy.app import App
from kivy.lang import Builder
from jnius import autoclass
import webbrowser
import datetime
import random

PythonActivity = autoclass('org.kivy.android.PythonActivity')
TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
Locale = autoclass('java.util.Locale')
Intent = autoclass('android.content.Intent')
Uri = autoclass('android.net.Uri')

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 15
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: 'FRIDAY PRO AI'
        font_size: '28sp'
        bold: True
        color: 0, 0.8, 1, 1
        size_hint_y: 0.15
    Image:
        source: 'logo.png'
        size_hint_y: 0.4
    Label:
        id: status_label
        text: 'How can I help you, Sir?'
        font_size: '18sp'
        color: 1,1,1,1
        size_hint_y: 0.2
    TextInput:
        id: command_input
        hint_text: 'Type your command here...'
        size_hint_y: 0.15
        multiline: False
        on_text_validate: app.process_command(self.text)
    BoxLayout:
        size_hint_y: 0.2
        spacing: 10
        Button:
            text: 'ASK FRIDAY'
            background_color: 0, 0.8, 1, 1
            on_press: app.process_command(command_input.text)
        Button:
            text: 'CLEAR'
            background_color: 1, 0.2, 0.2, 1
            on_press: command_input.text = ''
'''

class FridayApp(App):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        try:
            self.tts = TextToSpeech(PythonActivity.mActivity, None)
            self.speak("System Online. I am Friday Pro, Ready to serve you Sir.")
        except Exception as e:
            print(f"TTS Error: {e}")

    def speak(self, text):
        try:
            if hasattr(self, 'tts'):
                self.tts.speak(text, TextToSpeech.QUEUE_FLUSH, None)
            self.root.ids.status_label.text = text
        except Exception as e:
            print(e)

    def process_command(self, command):
        cmd = command.lower().strip()
        if not cmd:
            return

        if 'hello' in cmd or 'hi' in cmd:
            self.speak("Hello Sir, How can I help you?")
        elif 'time' in cmd:
            now = datetime.datetime.now().strftime("%I:%M %p")
            self.speak(f"Sir, Current time is {now}")
        elif 'date' in cmd or 'day' in cmd:
            today = datetime.datetime.now().strftime("%A, %d %B %Y")
            self.speak(f"Today is {today}")
        elif 'youtube' in cmd:
            self.speak("Opening YouTube Sir")
            webbrowser.open("https://youtube.com")
        elif 'google' in cmd and 'search' not in cmd:
            self.speak("Opening Google Sir")
            webbrowser.open("https://google.com")
        elif 'instagram' in cmd:
            self.speak("Opening Instagram")
            webbrowser.open("https://instagram.com")
        elif 'search' in cmd or 'google' in cmd:
            query = cmd.replace('search','').replace('google','').replace('for','').strip()
            if query:
                self.speak(f"Searching for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                self.speak("What should I search Sir?")
        elif 'play' in cmd and ('music' in cmd or 'song' in cmd):
            song = cmd.replace('play','').replace('music','').replace('song','').strip()
            if song:
                self.speak(f"Playing {song} on YouTube")
                webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
            else:
                self.speak("Playing your favourite music Sir")
                webbrowser.open("https://www.youtube.com/results?search_query=trending+songs")
        elif 'whatsapp' in cmd:
            self.speak("Opening WhatsApp Sir")
            try:
                intent = Intent(Intent.ACTION_VIEW)
                intent.setData(Uri.parse("https://wa.me/"))
                PythonActivity.mActivity.startActivity(intent)
            except:
                webbrowser.open("https://wa.me/")
        elif 'call' in cmd:
            self.speak("Please tell me the number Sir, opening dialer")
            intent = Intent(Intent.ACTION_VIEW)
            intent.setData(Uri.parse("tel:"))
            PythonActivity.mActivity.startActivity(intent)
        elif 'joke' in cmd:
            jokes = ["Why did the developer go broke? Because he used up all his cache!", "I am not lazy Sir, I am on energy saving mode."]
            self.speak(random.choice(jokes))
        elif 'shayari' in cmd or 'motivate' in cmd:
            self.speak("Zindagi me kabhi haar mat man-na Sir, kyuki FRIDAY hamesha aapke saath hai.")
        elif 'who are you' in cmd:
            self.speak("I am Friday Pro, Your personal AI assistant created by Saurabh Sir.")
        else:
            self.speak(f"You said {command}, I will search it for you Sir.")
            webbrowser.open(f"https://www.google.com/search?q={cmd}")

FridayApp().run()
