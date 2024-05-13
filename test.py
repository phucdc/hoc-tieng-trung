'''
from gtts import gTTS

from playsound import playsound

# Chinese text
chinese_text = "你好,今天过得怎么样?"

# Create a gTTS object
tts = gTTS(text=chinese_text, lang='zh-cn')

# Save the audio file
audio_file = 'chinese_audio.mp3'
tts.save(audio_file)

# Play the audio
playsound(audio_file)
'''

from database import init_db, db_session
from models import Word, Tab

init_db()
db_session.add(Tab(name='test'))
db_session.commit()