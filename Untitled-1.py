# ==============================================================================
# KLISTRA IN DIN KOD MELLAN CITATTECKNEN PÅ DE STEG DU VILL ANVÄNDA (1 TILL 10):
# ==============================================================================

steg_1  = """ print('Steg 1 körs...') """
steg_2  = """ import os
import subprocess
import time

# Vad filen ska heta på skrivbordet
filnamn = "Cooked.txt"

desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
if not os.path.exists(desktop):
    desktop = os.path.join(os.environ['USERPROFILE'], 'Skrivbord')

output_file = os.path.join(desktop, filnamn)

try:
    # 1. Hämta gateway-IP dolt via PowerShell
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = 0 
    
    cmd = ["powershell.exe", "-NoProfile", "-WindowStyle", "Hidden", "-Command", "(Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop"]
    result = subprocess.run(cmd, capture_output=True, text=True, startupinfo=startupinfo)
    
    gateway_ip = result.stdout.strip()
    if not gateway_ip:
        gateway_ip = "192.168.1.1"

    # 2. Skapa texten och spara Cooked.txt
    min_text = f"I know where you live, your gateway is {gateway_ip} and I am watching you..."

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(min_text) 

    # 3. Öppna Cooked.txt i Anteckningar och vänta tills användaren stänger fönstret
    subprocess.run(["notepad.exe", output_file])

    # 4. Radera textfilen permanent från skrivbordet
    if os.path.exists(output_file):
        os.remove(output_file)
    
    # Source - https://stackoverflow.com/q/37407255
# Posted by Chumbucket, modified by community. See post 'Timeline' for change history
# Retrieved 2026-11-10, License - CC BY-SA 4.0

import time
import pygame

screen=pygame.display.set_mode(size, pygame.FULLSCREEN)
nbPicturesToLoad=12
pictures=range(nbPicturesToLoad)
for i in range(nbPicturesToLoad):
    pictures[i]=pygame.image.load(pictureName).convert() //Here pictureName depends on the value of i

(...)

for i in range(nbPicturesToLoad):
    timer1=time.time()
    screen.blit(pictures[i], (0,0))
    pygame.display.flip()
    timer2=time.time()
    timer=timer2-timer1
    while(timer<0.03333):
        timer2=time.time()
        timer=timer2-timer1

except Exception:
    pass """
steg_3  = """  """
steg_4  = """  """
steg_5  = """  """
steg_6  = """  """
steg_7  = """  """
steg_8  = """  """
steg_9  = """  """
steg_10 = """ print('Steg 10 klart!') """

# ==============================================================================
# RÖR INTE KODEN NEDANFÖR - DEN KÖR DINA 10 STEG I ORDNING AUTOMATISKT
# ==============================================================================
import sys

def kor_steg(kod_text, nummer):
    rensa_kod = kod_text.strip()
    if rensa_kod: # Körs bara om du har klistrat in något på steget
        try:
            exec(rensa_kod, globals())
        except Exception as e:
            print(f"\n[FEL] Det blev fel i STEG {nummer}:\n{e}")
            return False
    return True

def starta():
    alla_steg = [steg_1, steg_2, steg_3, steg_4, steg_5, steg_6, steg_7, steg_8, steg_9, steg_10]
    
    for i, steg in enumerate(alla_steg, 1):
        if not kor_steg(steg, i):
            break # Avbryter om ett steg kraschar
            
    input("\nTryck på Enter för att avsluta programmet...")

if __name__ == "__main__":
    starta()
