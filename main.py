from kivy.app import App
from kivy.lang import Builder
from jnius import autoclass
import webbrowser

Locale = autoclass('java.util.Locale')
PythonActivity = autoclass('org.kivy.android.PythonActivity')

KV = '''
BoxLayout:
 orientation: 'vertical'
 padding: 20
 spacing: 15
 Label:
  text: 'FRIDAY PRO'
  font_size: '28sp'
  color: 0,0.9,1,1
 Label:
  id: msg
  text: 'Ready Boss'
  color: 1,1,1,1
 Button:
  text: 'FRIDAY'
  size_hint_y: .3
  on_press: app.speak_yes_boss()
 Button:
  text: 'Open WhatsApp'
  on_press: app.open_app("com.whatsapp")
'''

class FridayApp(App):
 tts = None
 def build(self):
  return Builder.load_string(KV)

 def speak_yes_boss(self):
  self.speak_hindi("Yes Boss")

 def speak_hindi(self, text):
  try:
   act = PythonActivity.mActivity
   if not self.tts:
    TTS = autoclass('android.speech.tts.TextToSpeech')
    self.tts = TTS(act, None)
    self.tts.setLanguage(Locale("hi","IN"))
    self.tts.setSpeechRate(0.85)
   self.tts.speak(text, 0, None)
   self.root.ids.msg.text = text
  except:
   self.root.ids.msg.text = text

 def open_app(self, pkg):
  try:
   pm = PythonActivity.mActivity.getPackageManager()
   intent = pm.getLaunchIntentForPackage(pkg)
   PythonActivity.mActivity.startActivity(intent)
  except:
   webbrowser.open("https://google.com")

FridayApp().run()
