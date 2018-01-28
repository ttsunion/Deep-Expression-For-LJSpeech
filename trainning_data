#Training_data

#LJ Speech dataset was downloaded from below website:

* [LJ Speech](https://keithito.com/LJ-Speech-Dataset/) (Public Domain)

#processing LJSpeech-1.0 metadata.csv can be found in [keithito_tacotron](https://github.com/keithito/tacotron), after that,

we can get train.txt, then use a python script below to transcribe his results to mine.

with open(r'D:\tacotron-master\tacotron-master\LJSpeech-1.0\labels.txt','w') as file:
    with open(r'D:\tacotron-master\tacotron-master\LJSpeech-1.0\metadata.csv','r',encoding='utf-8') as file1:
        with open(r'D:\tacotron-master\tacotron-master\LJSpeech-1.0\train.txt','r',encoding='utf-8') as file2:
            line1 = file1.readlines()
            line2 = file2.readlines()
            for i in range(len(line1)):
                line = line1[i].split('|')[0]+'|'+line2[i].split('|')[1]
                file.write(line)
                file.write("\n")
                file.flush()
            
then, I revised some text manually

1.line 5936 replace “sponge” to "sponge"

2.line 5965 replace “crater”  to "crater"

3.line 5975 replace “bolting” to "bolting"

4.line 6040 replace hours’ to hours'

5.line 8822 replace [Marina] to Marina

6.line 4247 repace bric-à-brac to bric-a-brac

7.line 4671 repace d'être to d'etre

8.lines 4685, 4700, 4707, 4714, 5164, 5165, 5166, 5167, 5168, 5170, 5173, 5175, 5183, 5186 repace Müller to Muller

9.line 5535 repace célèbre to celebre
