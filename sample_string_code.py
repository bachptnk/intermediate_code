# Quang_Bach_sample code
# If you use it, remember to give me credit

import os
os.system('cls')
#os.startfile('KeyVINA.exe')
from time import sleep
import playsound
from playsound import playsound
import sys
playsound('assets/PTNK-on.mp3')
print('\033[1;37;40mPlease wait while ChatVINA_lite is loading ...')
import torch
device = 0 if torch.cuda.is_available() else -1
from transformers import pipeline, BertTokenizer, BertForSequenceClassification
import random
import re
import warnings
warnings.filterwarnings("ignore")


################################################################
generator = pipeline('text-generation', model='assets/lite_bach_model', device=device)
tokenizer = BertTokenizer.from_pretrained('assets/sysmod')
model = BertForSequenceClassification.from_pretrained('assets/sysmod')

################################################################
global context
context='"Hello, my name is Vina. How can I help you?"\n"Hi, can I ask you some questions?"\n"Yes, you can ask me anything."\n"what is ambition in life?"\n"I think ambition is a strong desire to achieve whatever goals you set for yourself."'
prompt=('')
string3=('')


################################################################


def promptt():
    print('')
    print('\033[1;31;40mUser:\033[1;37;40m', end = ' \033[1;33;40m')
    global prompt
    global prompt_pure
    global string3
    z=input()
    prompt = prompt+'\n'+string3+'\n'+'"'+z+'"'
    #print(prompt)
    if context in prompt:
        context_length_1=int(len(context))
        prompt=prompt[context_length_1:]
    #print(prompt)
    prompt_pure=prompt
    global initial_prompt
    initial_prompt = prompt
    prompt = context+prompt
    
################################################################

global final_answer
final_answer = ""

################################################################

def process():
    print('\033[1;36;40mChatVINA \033[1;37;40mis typing. . . . .\033[1;37;40m', end='\r')
    t1=random.randint(8,9)
    t2=random.randint(1,8)
    t3=random.randint(1,9)
    p=float("0."+ str(t1)+ str(t2)+str(t3))
    k=random.randint(38,60)
    res = generator(prompt,max_new_tokens=30, do_sample=True, top_k=k, top_p=p, pad_token_id = 50256)
    #os.system('cls')
    #print('User: ')
    #global z
    #print(z)

        

    list=re.split(r'[.!?]+', res[0]['generated_text'])
    real_initial_length = int(len(res[0]['generated_text']))
    list=re.split(r'[.!?]+', res[0]['generated_text'])
    no_need_part_length = int(len(list[-1]))
    remain_length = real_initial_length - no_need_part_length
    not_final_answer=res[0]['generated_text']
    final_answer = not_final_answer[:remain_length]
    context_length = int(len(context))
    prompt_length = int(len(initial_prompt))
    context_length_and_prompt_length = context_length + prompt_length
    final_answer = final_answer[context_length_and_prompt_length:]

    
    list2=re.split(r"\"", final_answer)
    if len(list2)==0: return process()
    
    global string3
    try:
        if (len(list2[0]))>3:
            string3='"'+(list2[0])+'"'
        if (len(list2[1]))>3:
            string3='"'+(list2[1])+'"'
    except:
        return process()
    playsound('assets/receive.mp3')
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    string4=string3.replace('"','')
    print('\033[1;36;40mChatVINA: \033[1;33;40m' + string4 +'\033[1;37;40m')
    #print('ChatVINA: ' + string3)

    

while True:
    promptt()
    process()