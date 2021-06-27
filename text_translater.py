# pip install translate

from translate import Translator
translator = Translator(from_lang='Spanish', to_lang='English')
result = translator.translate('Suscríbete a mi canal')
print(result)