# ```py
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

# apikey = os.environ['iuXXelXUFt-7ICyoxq434BrneQuVLtx_Z2p0ObLULLjs']
# url = os.environ['https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/63fe1554-b07f-4d73-86d3-5a10970e13f6']
# ```
apikey='iuXXelXUFt-7ICyoxq434BrneQuVLtx_Z2p0ObLULLjs'
url='https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/63fe1554-b07f-4d73-86d3-5a10970e13f6'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
def englishToFrench(englishText):
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    englishText = translation['translations'][0]['translation']
    return englishText
