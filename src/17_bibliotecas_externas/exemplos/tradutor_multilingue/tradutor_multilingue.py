# Importa a classe Translator do módulo googletrans
from googletrans import Translator

# Define uma função para criar um dicionário de traduções multilíngue para uma palavra específica
def multi_language_dictionary(word):
    # Cria uma instância da classe Translator
    translator = Translator()

    # Traduz a palavra para o inglês
    translations = translator.translate(word, dest='en', src='pt')
    english_translation = translations.text

    # Traduz a palavra para o francês
    translations = translator.translate(word, dest='fr', src='pt')
    french_translation = translations.text

    # Traduz a palavra para o espanhol
    translations = translator.translate(word, dest='es', src='pt')
    spanish_translation = translations.text

    # Retorna um dicionário com as traduções para cada idioma especificado
    return {
        'Português': word,
        'Inglês': english_translation,
        'Francês': french_translation,
        'Espanhol': spanish_translation
    }

# Exemplo de uso da função
word = 'bonita'
translations = multi_language_dictionary(word)

# Itera sobre as traduções e imprime cada uma delas com o idioma correspondente
for lang, translation in translations.items():
    print(f'{lang}: {translation}')


