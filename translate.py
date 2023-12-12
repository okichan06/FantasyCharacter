from googletrans import Translator

def create_prompt(Input_prompt):
    base_prompt = "(((super realistic))), (((best quality))),((masterpiece)), ((ultra-detailed)), an anime style"
    translator = Translator()
    character = Input_prompt
    jp_words, en_words = [character],[]
    
    for src in jp_words:
        dst = translator.translate(src, src='ja', dest='en')
        en_words.append(dst.text)
        en_txt = ', '.join(en_words)
    return base_prompt + en_txt
    
if __name__ == "__main__":
    new_prompt = create_prompt("テスト用の文字です")
    print(prompt)
