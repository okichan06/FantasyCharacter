from googletrans import Translator

def create_prompt(Input_Chara,Input_Job,Input_Do):
    base_prompt = "(((super realistic))), (((best quality))),((masterpiece)), ((ultra-detailed)), an anime style,"
    translator = Translator()
    character = Input_Chara
    job = Input_Job
    Do = Input_Do
    jp_words, en_words = [character, job, Do],[]
    
    for src in jp_words:
        dst = translator.translate(src, src='ja', dest='en')
        en_words.append(dst.text)
        en_txt = ', '.join(en_words)
    return base_prompt + en_txt
    
if __name__ == "__main__":
    new_prompt = create_prompt("テスト用の文字です")
    print(new_prompt)
