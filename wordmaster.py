from textblob import TextBlob
from datetime import datetime
from nltk.corpus import wordnet
import ety
import nltk
nltk.download('wordnet')
from langcodes import langcodes

print(
	f"""Hey there! I am the Word Master.
I can tell you everything you want to know about the word that is bugging your mind.
So, welcome to my v1.0 on this fine day in {datetime.now().strftime('%B.')}
	"""
)

word = str(input("\nInput your word: ")).lower()

print(
	f"""\nYou can do the following things with your word:
1. Know the meaning
2. Translate it to another language

(The etymological tree will be displayed in any case)"""
)


choice = int(input("\nEnter your choice as a number: "))

def langCode_to_lang(list, langName):
	return [langCode for langCode, toLang in list.items() if toLang == langName]
	

toTB="" 
toTB=TextBlob(word)
toTB_lang=toTB.detect_language()

print(f"\nThe language of the entered word is: {langcodes[toTB_lang]}")

if choice == 1:  # Know the meaning
	if toTB_lang != 'en':
		syns = wordnet.synsets(toTB.translate(to = 'en')) 
	else:
		syns = wordnet.synsets(word)

	print(f"The most common meaning of '{word}' in English is:")
	print(syns[0].definition()) 

elif choice == 2:  # Translate it
	toLang = str(input("Which language do you want the word to be translated in? ")).lower().capitalize()
	langCode = langCode_to_lang(langcodes, toLang) 

	print(f"'{word}' translated into {toLang} is:")
	print(toTB.translate(to = langCode[0])) 



toTB2 = TextBlob(word) 
toTB2_lang = toTB.detect_language()

print(f"\nThe etymological root of '{word}' is as below: \n")

if toTB2_lang != 'en':
	print(ety.tree(str(toTB2.translate(to = 'en'))))
else:
	print (ety.tree(word))
