import os
os.system('cls')
#os.startfile('KeyVINA.exe')
from time import sleep
import playsound
from playsound import playsound
print('\033[1;32;40m')
import sys
import re

sys.stdout.write('\033[1A')








print('\033[1;37;40mPlease wait while ChatVINA_lite is loading ...')
import torch
device = 0 if torch.cuda.is_available() else -1


from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torch
import speech_recognition as sr
from pydub import AudioSegment
import io
import pyttsx3
import datetime
import random

import sys
def quit():
    sys.exit()
import os

import playsound
from playsound import playsound





device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# load model and tokenizer
Bach_processor = Wav2Vec2Processor.from_pretrained("assets/eng-model")
model = Wav2Vec2ForCTC.from_pretrained("assets/eng-model")#wav2vec2-bachptnk-model


PTNK_AI_assistant=pyttsx3.init()  # My name is Bach. I am learning in grade 10 in HIGH SCHOOL FOR THE GIFTED (PTNK)
voice=PTNK_AI_assistant.getProperty('voices')
assistant_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
PTNK_AI_assistant.setProperty('voice',assistant_voice_id)
Brate = 170
PTNK_AI_assistant.setProperty('rate',Brate)
def speak(audio):
    #print('PTNK_AI_assistant: ' + audio)
    PTNK_AI_assistant.say(audio)
    PTNK_AI_assistant.runAndWait()



def time():
    Time=datetime.datetime.now().strftime('%I:%M: %p') #giải thích nè ^^: %I là giờ loại 12 tiếng, %M là phút, %p là AM hay PM
    speak('It is')
    speak(Time)
def date():
    today=datetime.datetime.now().strftime('Today is %d-%m-%Y')

    speak(today)
    
def welcome(): #đây là mình tạo một cái function chào hỏi dựa theo thời gian mỗi khi khởi động PTNK_AI_ASSISTANT
    hour=datetime.datetime.now().hour
    if hour >=3 and hour <12:
        speak('Good morning')
    elif hour >=12 and hour <18:
        speak('Good afternoon')
    elif hour >=18 and hour <21:
        speak('Good evening')
    elif hour >=21 and hour <24:
        speak('Good nice and have a nice dream')
    elif hour >=0 and hour <3:
        speak('It is late. Let us take a nap.')
    speak('What can I help you?')


from transformers import pipeline, BertTokenizer, BertForSequenceClassification
import torch
device_for_genertator = 0 if torch.cuda.is_available() else -1
import warnings
warnings.filterwarnings("ignore")

generator = pipeline('text-generation', model='assets/lite_bach_model', device=device_for_genertator)
tokenizerkk = BertTokenizer.from_pretrained('assets/sysmod')
modelkk = BertForSequenceClassification.from_pretrained('assets/sysmod')

################################################################
global context
context='"Hello, my name is Vina. How can I help you?"\n"Hi, can I ask you some questions?"\n"Yes, you can ask me anything."\n"what is ambition in life?"\n"I think ambition is a strong desire to achieve whatever goals you set for yourself."'
prompt=('')
string3=('')




rec_Bach = sr.Recognizer()
def command():
  with sr.Microphone(sample_rate=16000) as source:  
    rec_Bach.pause_threshold=1
    #rec_Bach.adjust_for_ambient_noise(source)
    #print('You can start speaking now!')
    audio = rec_Bach.listen(source, phrase_time_limit=4)
    data = io.BytesIO(audio.get_wav_data())
    clip = AudioSegment.from_file(data)
    x = torch.FloatTensor(clip.get_array_of_samples())
    inputs = Bach_processor(x, sampling_rate=16000, 
    return_tensors='pt', padding='longest').input_values
    logits = model(inputs).logits
    tokens = torch.argmax(logits, axis=-1)
    text = Bach_processor.batch_decode(tokens)
    print('You said: ', str(text))
    z=str(text)
    global prompt
    prompt = prompt+'\n'+string3+'\n'+'"'+z+'"'
    if context in prompt:
        context_length_1=int(len(context))
        prompt=prompt[context_length_1:]

    prompt_pure=prompt
    global initial_prompt
    initial_prompt = prompt
    prompt = context+prompt
    return text


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
    speak(string4)














playsound('assets/PTNK-on.mp3')
def main_function():
  while True:
    textaBach=command() #textaBach is a list, not a string
    text=''
    for x in textaBach:
      text += ' '+x #convert list to string
    if ("PUT YOUR WORDS HERE" in text.lower()):
      #YOUR UNIQUE FUNCTION HERE                This is QuangBach sample code. Please give me credit if you use it.
      pass

    else:
      process()
    
        
main_function()