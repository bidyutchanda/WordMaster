from textblob import TextBlob
from datetime import datetime
from nltk.corpus import wordnet
import ety

langcodes = { #langcodes dict
	'ab': 'Abkhaz',
	'aa': 'Afar',
	'af': 'Afrikaans',
	'ak': 'Akan',
	'sq': 'Albanian',
	'am': 'Amharic',
	'ar': 'Arabic',
	'an': 'Aragonese',
	'hy': 'Armenian',
	'as': 'Assamese',
	'av': 'Avaric',
	'ae': 'Avestan',
	'ay': 'Aymara',
	'az': 'Azerbaijani',
	'bm': 'Bambara',
	'ba': 'Bashkir',
	'eu': 'Basque',
	'be': 'Belarusian',
	'bn': 'Bengali',
	'bh': 'Bihari',
	'bi': 'Bislama',
	'bs': 'Bosnian',
	'br': 'Breton',
	'bg': 'Bulgarian',
	'my': 'Burmese',
	'ca': 'Catalan; Valencian',
	'ch': 'Chamorro',
	'ce': 'Chechen',
	'ny': 'Chichewa; Chewa; Nyanja',
	'zh': 'Chinese',
	'cv': 'Chuvash',
	'kw': 'Cornish',
	'co': 'Corsican',
	'cr': 'Cree',
	'hr': 'Croatian',
	'cs': 'Czech',
	'da': 'Danish',
	'dv': 'Divehi; Maldivian;',
	'nl': 'Dutch',
	'dz': 'Dzongkha',
	'en': 'English',
	'eo': 'Esperanto',
	'et': 'Estonian',
	'ee': 'Ewe',
	'fo': 'Faroese',
	'fj': 'Fijian',
	'fi': 'Finnish',
	'fr': 'French',
	'ff': 'Fula',
	'gl': 'Galician',
	'ka': 'Georgian',
	'de': 'German',
	'el': 'Greek, Modern',
	'gu': 'Gujarati',
	'ht': 'Haitian',
	'ha': 'Hausa',
	'he': 'Hebrew (modern)',
	'hz': 'Herero',
	'hi': 'Hindi',
	'ho': 'Hiri Motu',
	'hu': 'Hungarian',
	'ia': 'Interlingua',
	'id': 'Indonesian',
	'ie': 'Interlingue',
	'ga': 'Irish',
	'ig': 'Igbo',
	'ik': 'Inupiaq',
	'io': 'Ido',
	'is': 'Icelandic',
	'it': 'Italian',
	'iu': 'Inuktitut',
	'ja': 'Japanese',
	'jv': 'Javanese',
	'kl': 'Kalaallisut',
	'kn': 'Kannada',
	'kr': 'Kanuri',
	'ks': 'Kashmiri',
	'kk': 'Kazakh',
	'km': 'Khmer',
	'ki': 'Kikuyu, Gikuyu',
	'rw': 'Kinyarwanda',
	'ky': 'Kirghiz, Kyrgyz',
	'kv': 'Komi',
	'kg': 'Kongo',
	'ko': 'Korean',
	'ku': 'Kurdish',
	'kj': 'Kwanyama, Kuanyama',
	'la': 'Latin',
	'lb': 'Luxembourgish',
	'lg': 'Luganda',
	'li': 'Limburgish',
	'ln': 'Lingala',
	'lo': 'Lao',
	'lt': 'Lithuanian',
	'lu': 'Luba-Katanga',
	'lv': 'Latvian',
	'gv': 'Manx',
	'mk': 'Macedonian',
	'mg': 'Malagasy',
	'ms': 'Malay',
	'ml': 'Malayalam',
	'mt': 'Maltese',
	'mr': 'Marathi',
	'mh': 'Marshallese',
	'mn': 'Mongolian',
	'na': 'Nauru',
	'nv': 'Navajo, Navaho',
	'nb': 'Norwegian',
	'nd': 'North Ndebele',
	'ne': 'Nepali',
	'ng': 'Ndonga',
	'nn': 'Norwegian Nynorsk',
	'no': 'Norwegian',
	'ii': 'Nuosu',
	'nr': 'South Ndebele',
	'oc': 'Occitan',
	'oj': 'Ojibwe, Ojibwa',
	'cu': 'Old Church Slavonic',
	'om': 'Oromo',
	'or': 'Oriya',
	'os': 'Ossetian, Ossetic',
	'pa': 'Panjabi, Punjabi',
	'fa': 'Persian',
	'pl': 'Polish',
	'ps': 'Pashto, Pushto',
	'pt': 'Portuguese',
	'qu': 'Quechua',
	'rm': 'Romansh',
	'rn': 'Kirundi',
	'ro': 'Romanian, Moldavan',
	'ru': 'Russian',
	'sa': 'Sanskrit',
	'sc': 'Sardinian',
	'sd': 'Sindhi',
	'se': 'Northern Sami',
	'sm': 'Samoan',
	'sg': 'Sango',
	'sr': 'Serbian',
	'gd': 'Scottish Gaelic',
	'sn': 'Shona',
	'si': 'Sinhala, Sinhalese',
	'sk': 'Slovak',
	'sl': 'Slovene',
	'so': 'Somali',
	'st': 'Southern Sotho',
	'es': 'Spanish',
	'su': 'Sundanese',
	'sw': 'Swahili',
	'ss': 'Swati',
	'sv': 'Swedish',
	'ta': 'Tamil',
	'te': 'Telugu',
	'tg': 'Tajik',
	'th': 'Thai',
	'ti': 'Tigrinya',
	'bo': 'Tibetan',
	'tk': 'Turkmen',
	'tl': 'Tagalog',
	'tn': 'Tswana',
	'to': 'Tonga',
	'tr': 'Turkish',
	'ts': 'Tsonga',
	'tt': 'Tatar',
	'tw': 'Twi',
	'ty': 'Tahitian',
	'ug': 'Uighur, Uyghur',
	'uk': 'Ukrainian',
	'ur': 'Urdu',
	'uz': 'Uzbek',
	've': 'Venda',
	'vi': 'Vietnamese',
	'wa': 'Walloon',
	'cy': 'Welsh',
	'wo': 'Wolof',
	'fy': 'Western Frisian',
	'xh': 'Xhosa',
	'yi': 'Yiddish',
	'yo': 'Yoruba',
	'za': 'Zhuang, Chuang',
	'zu': 'Zulu',
}

print("Hey there! I am the Word Master.\nI can tell you everything you want to know about the word that is bugging your mind.")
print("So, welcome to my v1.0 on this fine day in "+datetime.now().strftime('%B')+".")

word=raw_input("\nInput your word: ")

print("\nYou can do the following things with your word.\n1.Know the meaning.\n2.Translate it to another language.\nThe etymological tree will be displayed in any case. ")
choice=int(input("\nEnter your choice as a number:"))


def langCode_to_lang(list,langName):
	return [langCode for langCode,toLang in list.iteritems() if toLang == langName]
	

toTB="" 
toTB=TextBlob(word)
toTB_lang=toTB.detect_language()
print("\nThe language of the entered word is: "+langcodes[toTB_lang]) 

if choice==1: 
	if toTB_lang!='en':
		syns = wordnet.synsets(toTB.translate(to='en')) 
	else:
		syns = wordnet.synsets(word)
	print("\nThe most common meaning of '"+word+"' in English is:")
	print(syns[0].definition()) 

elif choice==2: 
	toLang=raw_input('Which language do you want the word to be translated in? ')
	langCode=langCode_to_lang(langcodes,toLang) 
	print("\n"+word+" translated into "+toLang+" is :")
	print(toTB.translate(to=langCode[0])) 



toTB2=TextBlob(word) 
toTB2_lang=toTB.detect_language()
print("\n\nThe etymological root of '"+word+"' is as below:\n")
if toTB2_lang!='en':
	print(ety.tree(str(toTB2.translate(to='en'))))
else:
	print (ety.tree(word))
