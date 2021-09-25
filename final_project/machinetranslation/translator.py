"""DuyManh's code"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-09-25',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(txt):
    """En to Fr"""
    if not txt:
        return ""
    translation = language_translator.translate(text=txt, model_id='en-fr').get_result()
    result = str(translation['translations'][0]['translation'])
    return result


def frenchToEnglish(txt):
    """Fr to En"""
    if not txt:
        return ""
    translation = language_translator.translate(text=txt, model_id='fr-en').get_result()
    result = str(translation['translations'][0]['translation'])
    return result
