# pip install pywhatkit

import pywhatkit as kit
text = "Welcome to my youtube Channel. Here I post videos on various short tutorials and projects related to Python and AI."
kit.text_to_handwriting(text, 'demo.png', rgb= [0,0,0])