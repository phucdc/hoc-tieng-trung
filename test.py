"""
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
"""

import cruds.tab as t_crud
import cruds.word as w_crud
from cruds.association import *
from database.database import init_db

init_db()

t_crud.create(name='Noun')
t_crud.create(name='Verb')
t_crud.create(name='Adj')
