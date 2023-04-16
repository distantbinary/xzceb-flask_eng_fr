"""
This module translate from English to French and vice versa
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY='iuXXelXUFt-7ICyoxq434BrneQuVLtx_Z2p0ObLULLjs'
URL='https://api.au-syd.language-translator.watson.cloud.ibm.com/'\
    'instances/63fe1554-b07f-4d73-86d3-5a10970e13f6'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def english_to_french(english_text):
    """
    This function translates English to French
    """
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    This function translates French to English
    """
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
