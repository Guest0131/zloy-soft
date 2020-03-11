import os
import codecs
import re
import time
import random

tasks_baza = []
def print_logo():
    logo = '''
    $$$$$$$$\ $$\                            $$$$$$\             $$$$$$\    $$\     
\____$$  |$$ |                          $$  __$$\           $$  __$$\   $$ |    
    $$  / $$ | $$$$$$\  $$\   $$\       $$ /  \__| $$$$$$\  $$ /  \__|$$$$$$\   
   $$  /  $$ |$$  __$$\ $$ |  $$ |      \$$$$$$\  $$  __$$\ $$$$\     \_$$  _|  
  $$  /   $$ |$$ /  $$ |$$ |  $$ |       \____$$\ $$ /  $$ |$$  _|      $$ |    
 $$  /    $$ |$$ |  $$ |$$ |  $$ |      $$\   $$ |$$ |  $$ |$$ |        $$ |$$\ 
$$$$$$$$\ $$ |\$$$$$$  |\$$$$$$$ |      \$$$$$$  |\$$$$$$  |$$ |        \$$$$  |
\________|\__| \______/  \____$$ |       \______/  \______/ \__|         \____/ 
                        $$\   $$ |                                              
                        \$$$$$$  |                                              
                         \______/                                               
                                      $$\       $$$$$$\                         
                                    $$$$ |     $$$ __$$\                        
 $$$$$$\   $$$$$$\ $$\    $$\       \_$$ |     $$$$\ $$ |                       
$$  __$$\ $$  __$$\\$$\  $$  |        $$ |     $$\$$\$$ |                       
$$ |  \__|$$$$$$$$ |\$$\$$  /         $$ |     $$ \$$$$ |                       
$$ |      $$   ____| \$$$  /          $$ |     $$ |\$$$ |                       
$$ |      \$$$$$$$\   \$  /         $$$$$$\ $$\\$$$$$$  /                       
\__|       \_______|   \_/          \______|\__|\______/                        
    '''

    print("\033[{}m {}" .format(random.randint(30, 37),logo))
    time.sleep(1)



def baza_load(type):
    tasks_type = os.walk('tasks\\' + str(type))
    print('Начата загрузка базы задач для ' + str(type))
    for address, dirs, files in tasks_type:
        for file in files:
            if ('ini' in file):
                tasks_baza.append(address + '\\' + file)
    print('База загружена')
    print('В базе найдено {} задач'.format(len(tasks_baza)))

def parse_solition(div):
    res = []
    for file in tasks_baza:
        f = codecs.open(file,'r','utf_8_sig').read()
        if (div in f):
            type = re.findall(r"Type = \"(.*)\"", f)[0]
            if('ulti' in type):
                res.append(re.findall(r"ulti\s?\[\]\s?=\s?\"(.*)\n", f))
            elif('ext' in type):
                res.append(re.findall(r"ext\s?\[\]\s?=\s?\"(.*)\n", f))
            else:
                res.append(re.findall(r"ingle\s?=\s?\"(.*)\n", f))
            if (len(res) > -1):
                print("Решение найдено в базе")
            else:
                print("Данная задача не найдена в базе")

            return res



if __name__ == '__main__':
    print_logo()
    print("Выберите конфигурацию PHP | CPP | DB | MP | SDB | shell")
    choise = str(input())
    baza_load(choise)
    print('\n')
    while(1 == 1):
        string = str(input())
        for i in parse_solition(string)[0]:
            print(i)
            print('\n')


