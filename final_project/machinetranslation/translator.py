import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
from flask import Flask, render_template
import json

app = Flask("My First Flask Application")

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2023-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(englishText=''):
    if(englishText == ''):
        return ''
    frenchText = language_translator.translate(
                    text=englishText,
                    source='en',
                    target='fr').get_result()
    return frenchText['translations'][0]['translation']


def frenchToEnglish(frenchText=''):
    if(frenchText == ''):
        return ''
    englishText = language_translator.translate(
                    text=frenchText,
                    source='fr',
                    target='en').get_result()
    return englishText['translations'][0]['translation']