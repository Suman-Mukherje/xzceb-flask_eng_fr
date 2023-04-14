
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

#apikey = os.environ['apikey']
#url = os.environ['url']

authenticator = IAMAuthenticator('byK0Vzllvnlz46BjZt4mQqNVbeOr-HeRQvXx7QiuEGgk')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/a1de3843-3951-49e1-89bb-34850daaff61')

def EnglishToFrench(english_text):
    #write the code here
    french_text = language_translator.translate(text = english_text, model_id='en-fr').get_result()
    #french_text = translation['translation'][0]['translation']
    return french_text

def FrenchToEnglish(french_text):
    english_text = language_translator.translate(text = french_text, model_id='fr-en').get_result()
    #english_text = translation['translation'][0]['translation']
    return english_text