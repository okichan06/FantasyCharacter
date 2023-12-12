from googletrans import Translator

def create_prompt(Input_prompt):
    print("start translating")
    prompt = "(((super realistic))), (((best quality))),((masterpiece)), ((ultra-detailed)), an anime style"
    translator = Translator()
    character = Input_prompt
    jp_words = [character]
    en_words = []
    print("I'm ready!")
    
    for src in jp_words:
        dst = translator.translate(src, src='ja', dest='en')
        en_words.append(dst.text)
        prompt = prompt + ', '.join(en_words)
    
    if __name__ == "__main__":
        create_prompt()
        print(prompt)
