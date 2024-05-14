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
from sqlalchemy import select
from crud import get_tab_by_id, add_tab, delete_tab_by_id, add_word

init_db()
# db_session.add(Tab(name='test_tab'))
# db_session.add(Tab(name='test_tab2'))
# word = Word(word="test", meaning="kiem tra")
# db_session.add(word)
# db_session.commit()
#
# tab = get_tab_by_id(1)
# tab2 = get_tab_by_id(2)
# tab.words.append(word)
# tab2.words.append(word)
# db_session.commit()

add_word(word="多谢多谢", meaning="khong biet")

