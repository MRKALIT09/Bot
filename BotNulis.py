import requests
import shutil
import os
import json
url="https://tools.zone-xsec.com/api/nulis.php?q="
logo="""
Program Bot Nulis Bisa Via File Ya Anjink :v
Open Source Juga Bwang Mana Tau Butuh Ya Kan
=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×

Author Script = ./Mando × -Xploit
Cyber Me      = Medan-Xploiter
WhatsApp Me   = 0853-6152-4681
"""

def biasa():
    tulis=input("Masukan text Nya Bwang : ")
    req=requests.get(url+tulis)
    jeson=json.loads(req.text)
    link=jeson['image']
    image_url= link
    nama_file = image_url.split("/")[-1]
    r = requests.get(image_url, stream = True)
    if r.status_code == 200:
       r.raw.decode_content = True
       with open(nama_file, 'wb') as f:
           shutil.copyfileobj(r.raw, f)
           print('Succes Name File: ', nama_file)
    else:
        print("Maff Sistem Error")


if __name__=="__main__":
    os.system("clear")
    print(logo)
    print("[1]> Tulis Manual")
    print("[2]> Tulis Via File ")
    print("[3]> Exit/Out [> ")
    pil=input("Mau Yang Mana Bang ~> ")
    if pil == "1":
        biasa()
    if pil == "2":
        file
    else:
        print(pil,  "[!] Pilihan Tidak ada ")

