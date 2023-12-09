from googletrans import Translator

def create_prompt(Input_prompt):
    prompt = "(((super realistic))), (((best quality))),((masterpiece)), ((ultra-detailed)), an anime style"
    translator = Translator()
    character = Input_prompt
    jp_words = [character]
    en_words = []
    
    for src in jp_words:
        dst = translator.translate(src, src='ja', dest='en')
        en_words.append(dst.text)
        prompt = prompt + ', '.join(en_words)
