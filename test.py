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

word1 = w_crud.create(word='你好', meaning='xin chao')
word2 = w_crud.create(word='对不起', meaning='xin loi')

tab1 = t_crud.create(name="greetings")
tab2 = t_crud.create(name="sayings")

add_words_to_tab(t=tab1, w=word1)
add_words_to_tab(t=tab2, w=word1)

t_crud.delete(tab1.id)
