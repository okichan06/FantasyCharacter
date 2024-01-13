from googletrans import Translator
import random

def create_prompt(Input_Chara,Input_Job,Input_Do):
    base_prompt = "(((super realistic))), (((best quality))),((masterpiece)), ((ultra-detailed)), an anime style, fantasy"
    
    N = random.randint(1, 100)
    if N%2==0:
        Sex = "male, one man"
    else:
        Sex = "one girl"

    if N<=10:
        base_promptT = Sex +" with dradon horns, "+base_prompt
    elif N<=30:
        base_promptT = Sex +", elf, "+base_prompt+", in forest"
    elif N<= 55:
        base_promptT = Sex +" with cat ears, "+base_prompt
    elif N<=80:
        base_promptT = Sex +" with wolf ears, "+base_prompt
    elif N<=87:
        base_promptT = Sex +", fairy, "+base_prompt+", in forest"
    else:
        base_promptT = Sex + ", " +base_prompt

    translator = Translator()
    character = Input_Chara
    job = Input_Job
    Do = Input_Do
    jp_words, en_words = [character, job, Do],[]
    
    for src in jp_words:
        dst = translator.translate(src, src='ja', dest='en')
        en_words.append(dst.text)
        en_txt = ', '.join(en_words)
    return base_promptT + en_txt
    
if __name__ == "__main__":
    new_prompt = create_prompt("テスト用の文字です")
    print(new_prompt)
