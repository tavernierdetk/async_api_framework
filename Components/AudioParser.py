import requests
from newspaper import Article
from urllib.parse import urlparse
from time import sleep

import speech_recognition as sr
import os.path
from os import path
import shutil
from pydub import AudioSegment
import datetime
from abc import ABC, abstractmethod

class AudioParser(object):
    def __init__(self, audio_files_dir):
        self.audio_files_dir = audio_files_dir
        self.lang_lookup = {
            "fr" : "fr-CA"
        }
        self.r = sr.Recognizer()

    def _reset_variables(self):
        self.url = ''
        self.audio_filepath = ''
        self.lang = 'fr'
        self.date_name_string = ''
        self.audio_filename = ''
        self.output_filepath = ''
        self.article = {}

    def parse_article(self, url, lang, summarizer):
        self._reset_variables()

        self.summarizer = summarizer
        self.lang = lang
        self.url = url
        domain = urlparse(self.url).netloc.replace('www.','')
        if domain not in self.domain_parsing_method_lookup:
            self._parse_with_newspaper3k()
        else:
            self.domain_parsing_method_lookup[domain][0](self.domain_parsing_method_lookup[domain][1])

        return self.article

    def _update_directory(self):
        self.date_name_string = datetime.datetime.now().strftime('%Y-%m-%d')
        if not path.exists(f'{self.audio_files_dir}/{self.date_name_string}'):
            for file_or_dir in os.listdir(path=self.audio_files_dir):
                if file_or_dir != "Archive":
                    # path_to = ""
                    # path_from = ""
                    shutil.move(f'{self.audio_files_dir}/{file_or_dir}', f'{self.audio_files_dir}/Archive')
            os.mkdir(f'{self.audio_files_dir}/{self.date_name_string}')

    def _mp3_to_text(self):
        self._update_directory()

        self.audio_filename = self.audio_filepath.rsplit('/')[-1]

        self._get_and_convert_mp3()

        self._parse_text_from_wav()

        self.article = {
            "title": "",
            "text": "",
            "url": "",
            "summary": "",
        }

    def _get_and_convert_mp3(self):
        self.output_filepath = f'{self.audio_files_dir}/{self.date_name_string}/{self.audio_filename}'[:-4]+'.wav'
        audio_file = requests.get(self.audio_filepath)

        with open(f'{self.audio_files_dir}/{self.date_name_string}/{self.audio_filename}', 'wb') as f:
            f.write(audio_file.content)

        # convert mp3 to wav
        sound = AudioSegment.from_mp3(f'{self.audio_files_dir}/{self.date_name_string}/{self.audio_filename}')
        sound.export(str(self.output_filepath), format="wav")

    def _parse_985fm(self, key):
        #TODO method to extract URL
        print("Parsing 985fm")
        self._fetch_audio_file_source()
        self._mp3_to_text()

    def _parse_tva_audio(self, key):
        #TODO method to extract URL
        print("Parsing Audio from TVA")
        self._fetch_audio_file_source()
        self._mp3_to_text()

    def _fetch_audio_file_source(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

        button = self.driver.find_element(By.CSS_SELECTOR, ".o-btn--player-control")
        self.driver.execute_script("arguments[0].click();", button)

        sleep(2)
        self.audio_filepath = self.driver.find_element(By.ID, 'audio-streaming_html5').get_property('src')

    def _parse_with_selenium(self, key):
        print("Parsing with selenium")
        self.driver.get(self.url)
        article = self.driver.find_element(By.TAG_NAME, key)
        annotated_article = {
            "title": article.text[:article.text.find('.')],
            "text": article.text,
            "url": self.url,
            "summary": article.text[:article.text.find('.')],
        }
        return annotated_article

    def _parse_text_from_wav(self):
        with sr.AudioFile(self.output_filepath) as source:
            audio_text = self.r.listen(source)

        try:
            # using google speech recognition
            text = self.r.recognize_google(audio_text, language=self.lang_lookup[self.lang])
            print(text)

        except:
            print('audio file not processed')


class AudioParser:
    def __init__(self):
        SpeechRecognition