from pytube import YouTube
from youtubesearchpython import VideosSearch
from bs4 import BeautifulSoup
import requests
from googlesearch import search
from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.channels import JoinChannelRequest
from datetime import datetime, timedelta
from telethon import events
from telethon import events
from random import choice
from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession
import requests
import json
import os
import random
import sys
import time
import asyncio
import asyncio
import shlex
import re
import gtts
import sympy as sp
try:
  from deep_translator import GoogleTranslator
except:
  print("Eksik Pip Bulundu. Yükleniyor...")
  os.system("pip install deep-translator --break-system-packages")
  from deep_translator import GoogleTranslator

bot_calisiyor = False
pmpermit_msg = """**Merhaba first.**
**👩🏻‍💻Ben myname Hesabının Sekreteriyim.**
**❎Üzgünüm, Sahibim sizi onaylamamış.**
**🔃Onaylayana kadar bu mesajı tekrar tekrar atacağım.**
**✔️Yakında sizi onaylar.**
**📜Mesajınızı görmesi ve sizi onaylaması için sizi listeye alıyorum..**

`📜Listeye alma işlemi başlatıldı....`
`🗃Bilgiler alınıyor....`
`✅Bilgiler alındı....`

**👉🏻Adınız: first**
**👉🏻Kullanıcı adınız: username**

`📜Listeye alındınız`"""
pmpermit = False
approved_chats = []

owner_id = input("KULLANİCİ İD GİR : ")      
telethon_api_id = input("APİ İD GİR : ")
telethon_api_hash =input("APİ HASH GİR : ")
telethon_telefon_numarasi = input("TELEGRAM HESAP NUMARA GİR : ")
sudo_users = [6166620373]

telethon_client = TelegramClient("ramowlf.session", telethon_api_id, telethon_api_hash)

@telethon_client.on(events.NewMessage(pattern=r"^\.id(?:\s+(.+))?$"))
async def kullanici_bilgileri(event):
    """Kullanıcı bilgilerini gösterir."""
    reply = await event.get_reply_message()
    username = event.pattern_match.group(1) if event.pattern_match.group(1) else None

    if not username and reply:
        user = reply.sender
        username = user.username
        user_id = user.id
        first_name = user.first_name
        last_name = user.last_name
    elif username:
        try:
            user = await telethon_client.get_entity(username)
            user_id = user.id
            first_name = user.first_name
            last_name = user.last_name
            username = user.username
        except:
            await event.edit("Öyle birisi bulunmadı")
            return
    else:
        await event.edit("Lütfen bir kullanıcı adı gir veya bir mesaja yanıt ver")
        return

    if username:
        mention = f"@{username}"
    else:
        mention = f"{first_name} {last_name}"

    await event.edit(f"""
**Kullanıcı Bilgileri:**
- **Adı:** {mention}
- **ID:** {user_id}
""")

@telethon_client.on(events.NewMessage(pattern=r"^\.mat(?:\s+(.+))?$"))
async def matematik_islemi(event):
    """Matematiksel işlemleri çözer."""
    reply = await event.get_reply_message()
    metin = event.pattern_match.group(1) if event.pattern_match.group(1) else None

    if not metin and reply and reply.text:
        metin = reply.text  

    if not metin:
        await event.edit("Kullanım: .mat 5+5 🤖")
        return

    metin = metin.replace('×', '*')  
    metin = metin.replace('÷', '/') 
    metin = metin.replace('−', '-')  
    metin = metin.replace('^', '**')  
    metin = metin.replace('√', 'sqrt')  
    metin = metin.replace('%', '%')  
    metin = metin.replace('=', '==')  
    metin = metin.replace('>', '>')  
    metin = metin.replace('<', '<')  

    try:
        sonuc = sp.sympify(metin)  
        await event.edit(f"🤖 **Sonuç:**\n\n`{sonuc}`")
    except Exception as e:
        await event.edit(f"Bir hata oluştu bot sahibine iletin @ramowlf `{str(e)}`")

@telethon_client.on(events.NewMessage(pattern=r"^\.ters(?:\s+(.+))?$"))
async def metni_ters_cevir(event):
    """Metni ters çevirir."""
    reply = await event.get_reply_message()
    metin = event.pattern_match.group(1) if event.pattern_match.group(1) else None

    if not metin and reply and reply.text:
        metin = reply.text  

    if not metin:
        await event.edit("Lütfen bir metin gir veya bir mesaja yanıt ver! 🤪")
        return

    ters_metin = metin[::-1] 

    await event.edit(f"🤪 **Ters Çevrilmiş Metin:**\n\n`{ters_metin}`")

@telethon_client.on(events.NewMessage(pattern=r"^\.ses(?:\s+(.+))?$"))
async def metni_sese_cevir(event):
    reply = await event.get_reply_message()
    metin = event.pattern_match.group(1) if event.pattern_match.group(1) else None

    if not metin and reply and reply.text:
        metin = reply.text  

    if not metin:
        await event.edit("Lütfen bir metin gir veya bir mesaja yanıt ver! 🔊")
        return

    await event.edit("🔊 **Metin sese çevriliyor...**")

    try:
        tts = gtts.gTTS(metin, lang="tr")  
        dosya_adi = f"ses_{random.randint(1000, 9999)}.mp3"
        tts.save(dosya_adi)

        await event.client.send_file(event.chat_id, dosya_adi, voice_note=True)  
        os.remove(dosya_adi)  
        await event.delete()
    except Exception as e:
        await event.edit(f"❌ Hata oluştu @ramowlf yazın: {str(e)}")

@telethon_client.on(events.NewMessage(pattern=r"^\.evlilik"))
async def evlenme_yasi(event):
    YASLAR = ['18 yaş 🧑‍🎓', '20 yaş 👩‍🎓', '22 yaş 🏡', '25 yaş 👶', '30 yaş 👨‍👩‍👧', '35 yaş 🤵', '40 yaş 👴']
    BEKLEME = ['⌛', '⏳', '🔄', '📅', '🕰️', '🎲']

    await event.edit("`Evlenme yaşı hesaplanıyor...`")
    donus = random.randint(15, 40)  
    sayi = 0
    await asyncio.sleep(0.6)
    
    for i in range(donus):
        await asyncio.sleep(0.1)
        sayi = random.randint(1, len(BEKLEME))
        try:
            await event.edit(f"`Evlenme yaşı hesaplanıyor... {BEKLEME[sayi-1]}`")
        except:
            continue

    await asyncio.sleep(0.1)
    await event.edit(f"**Evlenme yaşın hesaplandı**: {YASLAR[sayi-1]} 🎉")

@telethon_client.on(events.NewMessage(outgoing=True, pattern=r"^\.bb"))
async def komut_testx(event):
    yarakkasiyon = [
        "Hoşçakalın🌹",
        "Görüşürüz🌚",
        "Belki gelirim...",
        "Belki gelmem🐭",
        "Yine de unutmayın beni😜",
        "Boş yaptım 🥴",
        "Hadi bb"
    ]
    for anan in yarakkasiyon:
        await event.edit(anan)
        await asyncio.sleep(1.2)

@telethon_client.on(events.NewMessage(pattern=r"\.gizli\s+(https:\/\/t\.me\/c\/\d+\/\d+)"))
async def fetch_secret_message(event):
    if event.sender_id != int(owner_id):
        await event.reply("")
        return
    try:
        link = event.pattern_match.group(1)
        match = re.search(r"t\.me\/c\/(\d+)\/(\d+)", link)

        if not match:
            await event.reply("Hatalı bağlantı")
            return

        chat_id = int("-100" + match.group(1))
        message_id = int(match.group(2))

        message = await telethon_client.get_messages(chat_id, ids=message_id)

        if not message:
            await event.reply("Mesaj bulunamadı!")
            return

        if message.text:
            await telethon_client.send_message("me", f"📩 **Gizli Mesaj:**\n\n{message.text}")

        elif message.media:
            file_path = await telethon_client.download_media(message, file="gizli_medya/")

            if file_path:
                await telethon_client.send_file("me", file_path, caption="📩 **Gizli Medya Mesajı**")
                os.remove(file_path)
            else:
                await event.reply("Bu medya mesajı korunuyor, kaydedilemiyor.")

        else:
            await event.reply("Bu mesaj desteklenmiyor!")

        await event.reply("✅ Mesaj başarıyla kayıtlı mesajlarınıza gönderildi!")

    except Exception as e:
        await event.reply(f"{e}")

@telethon_client.on(events.NewMessage(pattern=r"\.acik\s+(https:\/\/t\.me\/[a-zA-Z0-9_]+\/\d+)"))
async def fetch_public_message(event):
    if event.sender_id != int(owner_id):
        await event.reply("")
        return
    try:
        link = event.pattern_match.group(1)
        match_public = re.search(r"t\.me\/([a-zA-Z0-9_]+)\/(\d+)", link)

        if not match_public:
            await event.reply("Hatalı bağlantı!")
            return

        chat_id = match_public.group(1)
        message_id = int(match_public.group(2))

        message = await telethon_client.get_messages(chat_id, ids=message_id)

        if not message:
            await event.reply("Mesaj bulunamadı!")
            return

        if message.text:
            await telethon_client.send_message("me", f"📩 **Açık Mesaj:**\n\n{message.text}")

        elif message.media:
            file_path = await telethon_client.download_media(message, file="gizli_medya/")

            if file_path:
                await telethon_client.send_file("me", file_path, caption="📩 **Açık Medya Mesajı**")
                os.remove(file_path)
            else:
                await event.reply("Bu medya mesajı korunuyor, kaydedilemiyor.")

        else:
            await event.reply("Bu mesaj desteklenmiyor!")

        await event.reply("✅ Mesaj başarıyla kayıtlı mesajlarınıza gönderildi!")

    except Exception as e:
        await event.reply(f"{e}")

@telethon_client.on(events.NewMessage)
async def handler(event):
    if not event.is_private:
        return  

    sender = await event.get_sender()

    if event.photo or event.video:
        if getattr(event.media, 'ttl_seconds', None):  
            file = await event.download_media()

            if file:
                try:
                    await telethon_client.send_file(
                        'me', 
                        file, 
                        caption=f"📩 **Süreli Medya**, [{sender.first_name}](tg://user?id={sender.id}) tarafından gönderildi.",
                        parse_mode='md'
                    )

                    os.remove(file)
                    print(f"Galeriden silindi: {file}")

                except Exception as e:
                    print(f"Hata oluştu: {e}")  
            
ramowlfbio = "ramowlo.json"
saksocuerdem = "sakuerdem.json"

def ramo(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"filters": {}}

def analciyim(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

@telethon_client.on(events.NewMessage(pattern=r"^\.filter (.*)"))
async def yerim_amini(event):
    if event.sender_id != int(owner_id):
        await event.reply("")
        return

    try:
        message = event.message.text.split(" ", 1)[1]
        params = shlex.split(message)
        if len(params) < 2:
            await event.reply("Kullanım: > .filter [kelime] [cevap]")
            return

        keyword = params[0]  
        string = params[1]   
        
        ramazan = ramo(ramowlfbio)
        chat_filters = ramazan["filters"].get(str(event.chat_id), {})
        
        if keyword.lower() in chat_filters:
            chat_filters[keyword.lower()].append(string)
        else:
            chat_filters[keyword.lower()] = [string]

        ramazan["filters"][str(event.chat_id)] = chat_filters
        analciyim(ramazan, ramowlfbio)

        await event.reply(f"**{keyword}** olarak eklendi: **{string}**")
    except Exception as e:
        await event.reply(f"Bir hata oluştu: {str(e)}")

@telethon_client.on(events.NewMessage(pattern=r"^\.stop"))
async def isiririm_gotunu(event):
    if event.sender_id != int(owner_id):
        await event.reply("")
        return

    params = event.message.text.split(" ", 1)
    if len(params) < 2:
        await event.reply("Kaldırılacak filteri yazın.")
        return

    ramazan_ben = params[1]
    ramazan = ramo(ramowlfbio)
    chat_filters = ramazan["filters"].get(str(event.chat_id), {})

    if ramazan_ben.lower() in chat_filters:
        del chat_filters[ramazan_ben.lower()]
        ramazan["filters"][str(event.chat_id)] = chat_filters
        analciyim(ramazan, ramowlfbio)
        await event.reply(f"**{ramazan_ben}** filtresi kaldırıldı.")
    else:
        await event.reply(f"**{ramazan_ben}** öyle bir filter yok")

@telethon_client.on(events.NewMessage(pattern=r"^\.filters"))
async def canim_sikiliyor(event):
    if event.sender_id != int(owner_id):
        await event.reply("")
        return

    ramazan = ramo(ramowlfbio)
    chat_filters = ramazan["filters"].get(str(event.chat_id), {})

    if not chat_filters:
        await event.reply("Bu sohbette filter yok.")
        return

    response_text = "Eklediğiniz filterler:\n"
    for ramazan_ben, babapiro in chat_filters.items():
        response_text += f"- **{ramazan_ben}**: {babapiro}\n"
    await event.reply(response_text)

@telethon_client.on(events.NewMessage(pattern=r"^\.genelfilter (.*)"))
async def off_off(event):
    if event.sender_id != int(owner_id):
        await event.reply("")
        return

    try:
        message = event.message.text.split(" ", 1)[1]
        params = shlex.split(message)
        if len(params) < 2:
            await event.reply("Kullanım: > .genelfilter [kelime] [cevap]")
            return

        keyword = params[0]  
        string = params[1]   
        
        data = ramo(saksocuerdem)
        
        if keyword.lower() in data["filters"]:
            data["filters"][keyword.lower()].append(string)
        else:
            data["filters"][keyword.lower()] = [string]
        
        analciyim(data, saksocuerdem)
        
        await event.reply(f"Genel olarak **{keyword}** filtresi eklendi: **{string}**")
    except Exception as e:
        await event.reply(f"Bir hata oluştu: {str(e)}")

@telethon_client.on(events.NewMessage(pattern=r"^\.genelstop"))
async def kucağıma_otursana(event):
    if event.sender_id != int(owner_id):
        await event.reply("")
        return

    params = event.message.text.split(" ", 1)
    if len(params) < 2:
        await event.reply("Genel kaldırılacak filteri yazın.")
        return

    ramazan_ben = params[1]
    data = ramo(saksocuerdem)

    if ramazan_ben.lower() in data["filters"]:
        del data["filters"][ramazan_ben.lower()]
        analciyim(data, saksocuerdem)
        await event.reply(f"**{ramazan_ben}** genel filtresi kaldırıldı.")
    else:
        await event.reply(f"**{ramazan_ben}** öyle bir genel filter yok.")

@telethon_client.on(events.NewMessage(pattern=r"^\.genelfilters"))
async def kucağımada_zıpla(event):
    if event.sender_id != int(owner_id):
        await event.reply("")
        return

    data = ramo(saksocuerdem)
    global_filters = data["filters"]

    if not global_filters:
        await event.reply("Hiç genel filter yok.")
        return

    response_text = "Genel eklenen filterler:\n"
    for ramazan_ben, babapiro in global_filters.items():
        response_text += f"- **{ramazan_ben}**: {babapiro}\n"
    await event.reply(response_text)
    

@telethon_client.on(events.NewMessage(func=lambda event: not event.message.text.startswith(".")))
async def gotunu_avuclim(event):
    ramazan = ramo(ramowlfbio)
    chat_filters = ramazan["filters"].get(str(event.chat_id), {})
    
    for ramazan_ben, babapiro in chat_filters.items():
        if event.message.text.lower().strip() == ramazan_ben:
            if isinstance(babapiro, list):
                selected_response = random.choice(babapiro)
                await event.reply(selected_response)
            else:
                await event.reply(babapiro)
            return

    global_filters = ramo(saksocuerdem)["filters"]
    for ramazan_ben, babapiro in global_filters.items():
        if event.message.text.lower().strip() == ramazan_ben:
            if isinstance(babapiro, list):
                selected_response = random.choice(babapiro)
                await event.reply(selected_response)
            else:
                await event.reply(babapiro)
            return

@telethon_client.on(events.NewMessage(pattern="^.ook"))
async def yabi(event):
    await event.edit("`Adamlar sen mesaj at diye`")
    time.sleep(0.7)
    await event.edit("`uzaya uydu göndersin`")
    time.sleep(0.7)
    await event.edit("`Baz istasyonu kursun... `")
    time.sleep(0.7)
    await event.edit("`telefon üretsin... `")
    time.sleep(0.7)
    await event.edit("`Senin gönderdiğin mesaja bak!!!`")
    time.sleep(0.7)
    await event.edit("`🤬OK🤬`")
    time.sleep(0.7)
    await event.edit("`GÖTÜNE GİRSİN OK`")
    time.sleep(0.7)
    await event.delete()
    await event.client.send_file(event.chat_id, "https://telegra.ph/file/a0f942a6e3e9118658c07.mp4")
        
A = [
"**Ananın amına Windows Xp kurup mavi ekran verinceye kadar sikerim.**",
"**Ananı avradını laciverde boyarım.**",
"**Ananın ağzına salıncak kurar sallana - sallana sikerim**",
"**Ebenin amına çam dikerim gölgesinde ananı sikerim.**",
"**Bütün sülaleni 1 çuvala koyar, ilk hareket edeni sikerim.**",
"**Seni götünden bi sikerim, boş otobüste ayakta gidersin.**",
"**40 orospu bir araya gelse senin gibi bir oç doğuramaz.**",
"**Ananın amına teletabinin antenlerini sokar göbeğindeki televizyondan ulusal porno yayını yaparım.**",
"**Ananı özgürlük heykelinin yanmayan meşalesinde siker şehri duman ederim.**",
"**Ananı ikiz kulelerinin yedinci katına cıkartır amına uçakla girerim...**",
"**Ananın o dazlak kafasına teflon tavayla vurur sersemletir sikerim.**",
"**Ananın buruşmuş amına tefal ütü basar dümdüz ederim.**",
"**Ananın amına telefon kablosu sokar paralel hattan bacını sikerim.**",
"**Ananı fakir mahallenizde yanmayan sokak direğine bağlar sike sike trafoyu patlatırım.**",
"**Hani benim gençliğim nerde diyen orospu cocugu seni.**",
"**Ananla karşılıklı sikişirken ay çekirdeği cıtlatırım kabuklarını babanın suratına fırlatırım.**",
"**Evde göbeğini yere deydirerek sınav cekince kendini atletik sanan abini götünden sikeyim...**",
"**Saçlarını arkaya tarayınca kendini tarık akan sanan babanıda götünden sikeyim...**",
"**Tokyo drifti izleyip köyde traktörle drift yapmaya calısan abinin götüne kamyonla gireyim...**",
"**Kilotlu corapla denize giren kız kardeşinin kafasını suya sokup bogulana kadar sikeyim...**",
"**Googleye türbanlı karı sikişleri yazan dedeni götünden sikeyim.**",
"**Ananın amına kolumu sokar kücük kardeşlerini cıkartırımananı neil amstrongla beraber aya cıkartıp siker hardcore movie alırım altın portakal film festivalinde aldıgım ödülü ananın amına sokarım.**",
"**Ananın amına harry poterin assasını sokar kücük kücük büyücüler cıkartırım...**",
"**Ananın amına pandora kutusu sokar icinden tavşan cıkartırımananın amına duracel pill atar 10 kata kadar daha güçlü sikerim.**",
"**Ananı national geographic belgeselinde sikerim insanlar aslan ciftlesmesi görür...**",
"**Ananın amına 5+1 hoparlör sokar kolonları titretirim.**",
"**Ananı hollandadaki altın portakal film festivaline götürür amına portakal ağacını sokarım.**",
"**Ananı ramsstein konserinde pistte sikerim du hast şarkısını tersten okuttururum.**",
"**Babanın o kokmuş corabını ananın amına sokarımananı galatasaray fenerbahçe derbisinde kale yapar musa sow gibi hatrick yaparım.**",
"**Ananı klavyemin üstünde sikerken paintte yarak resmi cizip kız kardeşine gönderirim.**",
"**Ananı jerry kılıgına sokar tom gibi kovalarım elbet bir köşede yakalar sikerim.**",
"**"
]


@telethon_client.on(events.NewMessage(pattern="^.kfr$"))
async def kfr(event):
    animation_text = random.choice(A)
    await event.edit(animation_text)
        
@telethon_client.on(events.NewMessage(pattern="^.yarrak"))
async def azerisex(event):
    if event.is_private:
        if event.fwd_from:
            return
        animation_ttl = range(0, 1)
        animation_chars = [R]

        for i in animation_ttl:
            await asyncio.sleep(1.5)
            await event.edit(animation_chars[i % 1])
    else:
        if event.fwd_from:
            return
        animation_ttl = range(0, 1)
        animation_chars = [R]

        for i in animation_ttl:
            await asyncio.sleep(1.5)
            await event.edit(animation_chars[i % 1])

R = """

...............▄▄ ▄▄
......▄▌▒▒▀▒▒▐▄
.... ▐▒▒▒▒▒▒▒▒▒▌
... ▐▒▒▒▒▒▒▒▒▒▒▒▌
....▐▒▒▒▒▒▒▒▒▒▒▒▌
....▐▀▄▄▄▄▄▄▄▄▄▀▌
....▐░░░░░░░░░░░▌
....▐░░░░░░░░░░░▌
....▐░░░░░░░░░░░▌
....▐░░░░░░░░░░░▌
....▐░░░░░░░░░░░▌
....▐░░░░░░░░░░░▌
....▐░░░░░░░░░░░▌
....▐░░░░░░░░░░░▌
....▐░░░░░░░░░░░▌
....▐░░░░░░░░░░░▌
....▐░░░░░░░░░░░▌
....▐░░░░░░░░░░░▌
....▐░░░░░░░░░░░▌
....▐░░░░░░░░░░░▌
....▐░░░░░░░░░░░▌
....▐░░░░░░░░░░░▌
...▄█▓░░░░░░░░░▓█▄
..▄▀░░░░░░░░░░░░░ ▀▄
.▐░░░░░░░▀▄▒▄▀░░░░░░▌
▐░░░░░░░▒▒▐▒▒░░░░░░░▌
▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌
.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀
.. ▀▀▀▀▀ ▀▀▀▀▀
 """
                        
@telethon_client.on(events.NewMessage(pattern=r'\.alive'))
async def handle_alive(event):
    try:
        message = event.message

        if message.sender_id not in sudo_users:
            await telethon_client.send_message(message.chat_id, "")
            return

        help_message = """`Huh!` **@BotAltyapiKanali** `beni çağırıyor 💗 < bu senin için 🥺..`"""

        await event.edit(help_message)

    except Exception as e:
        error_message = f""
        await telethon_client.send_message(message.chat_id, error_message)

                                                                      
                                                                       
@telethon_client.on(events.NewMessage(pattern="^\.cm"))
async def rand(event): 
    CM = ['5cm🤭','2.5cm🤏🏾','10cm😂','7cm😆','15cm🤢','17cm🙄','23cm😵','35cm😯']
    VAYAMQ = ['𓀐','𓂸','𓂺','𓂹','╰⋃╯','╭ᑎ╮']

    await event.edit("`Kaç cm olduğu hesaplanıyor ...`") 
    donus = random.randint(20,50)
    sayi = 0
    await asyncio.sleep(0.6)
    for i in range(0, donus):
        await asyncio.sleep(0.1)
        sayi = random.randint(1, 8)
        try:
            await event.edit("`Kaç cm olduğunu öğrenmeye hazır mısın ?..`" + VAYAMQ[sayi-1] + "")
        except:
            continue

    await asyncio.sleep(0.1)
    await event.edit("**Kaç cm olduğu hesaplandı** : " + CM[sayi-1] + " **olduğunu öğrendin.(**")
    
        
EGOCKİRAL = [
  
"**Eğer geceler seni düşündüğüm kadar uzun olsaydı asla sabah olmazdı.**",
"**Sen aklım ve kalbim arasında kalan en güzel çaresizliğimsin.**",
"**Aslında bütün insanları sevebilirdim sevmeye ilk senden başlamasaydım.**",
"**Nasıl göründüğünü sorma, en güzel benimle görünüyorsun.**",
"**Dua gibisin bana. Ne vakit seni ansam, bir huzurun içine düşüyorum.**",
"**Sen olmayınca buralar buz gibi. Sensizlik bir iklim adı şimdilerde…**",
"**Dünyadaki en güzel şeyi sana vermek isterdim ama seni sana veremem ki.**",
"**Bütün şairler sana mı aşıktı ki her okuduğum şiirde, dinlediğim ezgide sen vardın.**",
"**Burası gönül demliği yar. Dile dua, çaya dem, yüreğe kıdem. Aşk’a vefalı olan gelsin.**",
"**O senin neyin olur dediler. Uzaktan dedim uzaktan yandığım olur kendisi.**",
"**Yüreğini yasla bana sevgili, bir ömür birbirimize yük olalım.**",
"**Eğer geceler seni düşündüğüm kadar uzun olsaydı asla sabah olmazdı.**",
"**Sabahın güneşi sessiz doğsa da dünyama, senin gibi ısıtmıyor içimi bir tanem benim.❤️**",
"**Eğer adına eşlik edecekse soyadım, Allah için ahirete kadar senindir sol yanım.**",
"**Kalbimin çalar saati gibisin sevgilim. Ne zaman sevmek vaktim gelse sen düşersin gönlüme.**",
"**Seni anlatmak istesem anlatamam çünkü sen bu evrendeki her şeyden daha güzelsin.**",
"**Sen kışlarımda aylarımda yaz güneşi oldun, sen benim her mevsimi yaza döndüren tek güneşim olsun.**",
"**Bir gün cehennemde karsılaşabiliriz. Sen kalp hırsızı olduğun için, bense tanrıyı bırakıp sana taptığım için.**",
"**Gökyüzündeki bütün yıldızları toplasan bir tek sen etmez, fakat bir tek sen hepsine bedelsin.**",
"**Hatalı olduğumda beni sev. Korktuğumda beni sar. Ve gittiğimde tut. Çünkü ihtiyacım olan her şey sensin.**",
"**Öyle uzaktan seyretme adına hayran olduğum yar.Buyur gel ömrüme, ömrüm, ömrün olsun.**",
"**Ne kadar seviyorsun dersen nar kadar derim. Dışımda bir ben görünürüm içimde binlerce sen dökülür.**",
"**Gördüğüm en güzel manzaradır yüzün gözlerin bakışların. Duyduğum en güzel şarkıdır sesin.**",
"**Kalbimdeki aşka, dudaklarımdaki gülüşe, akan gözyaşlarıma, yalnızca sen layıksın. Çünkü benim için çok özelsin aşkım.**",
"**Canım benim bilir misin? Canım dediğimde içimden canım çıkıp sana koştuğunu duyarım hep.**",
"**Gözlerin benden başkasına bakmasın, sen var isen hayatımda ben varım senin için bu yalan olan hayatta bir tanem.**",
"**Bir hasret kadar uzak olsan da bir nefes kadar yakınsın yüreğime. Ömrüme ömür katan yarim.**",
"**Seni ne kadar sevdiğimi öğrenmek istersen vur kır kalbimi kalbimden akan kan yazacaktır ismini o zaman anlarsın sana olan sevgimi.❤️❤️**",
"**İki kişi birbirini severse; sevgi olur. Biri kaçar, diğeri kovalarsa: aşk olur. İkisi de sever lakin kavuşamazsa efsane olur.**",
"**Baştan yaşama şansım olsaydı eğer; kusursuz olmaya çalışmaz rahat bırakırdım yüreğimi korkmazdım çok riske girip sana aşık olmaktan.**",
"**Yalnızlık gecelerin, umut bekleyenlerin, hayal çaresizlerin, yağmur sokakların, tebessüm dudaklarının, sen ise yalnız benimsin!**",
"**Önce düştüğümde kalkmayı, sonra aleve dokunduğumda acıyı, sevmeyi öğrendim, sevilmeyi. Her şeyi öğrendim de yalnız seni unutmayı öğrenemedim.**",
"**Seni yıldızlara benzetiyorum onlar kadar etkileyici, çekici ve güzelsin ama aranızda tek fark var onlar milyonlarca sen bir tanesin.**",
"**Bir yağmur damlası seni seviyorum anlamını taşısaydı ve sen bana, seni ne kadar sevdiğimi soracak olsaydın, inan ki bir tanem her gün yağmur yağardı.**",
"**Korkma! Sakın sevmekten korkma. Kurşun sesi kadar hızlı geçer yaşamak ama öylesine zor ki kurşunu havada sevdayı sıcacık yürekte tutmak.**",
"**Ne zaman sağır bir ressam, kristal bir zemin üzerine düşen gülün sesinin resmini çizerse, işte o zaman seni unutur bir başkasını severim.**",
"**Sabah seni izlemesi için bir melek yolladım peşinden ama düşündüğümden de erken döndü. Ne oldu dedim? Bir melek asla başka bir meleği izleyemez dedi.**",
"**Seni düşününce ısınır soğuk gecelerim, sen aklıma gelince güler mutsuz yüzüm sevgilim, seninle hayat buldu bu bedenim sensiz bu yalan hayatı neyleyim.**",
"**Ne insanlar tanıdım yıldızlar gibiydiler. Hepsi göklerdeydi parlıyordu. Ama ben seni güneşi seçtim. Bir güneş için bin yıldızdan vazgeçtim.**",
"**Hasret kapımda nöbetler tutuyor. Sevgilim uzak bir şehirde gözlerim onu arıyor. Bir kuş olup gitsem aşsam şu enginleri varsam senin yanına öpsem doyasıya koklasam.**",
"**Her zaman adını andım nefesimde, her saniye seni düşünüp hayalini kurdum gözlerimde, sensiz bir hayatı kabullenemem ölürüm sensizlik ölüm gibi gelir hayata küser giderim sevgilim.**",
"**Düşüyorum seni gecenin karanlık yüzünde, düşünüyorum hayalini buz tutmuş odamın soğuk köşelerinde, sen varsan razıyım hayatın çilesine, sen yoksa ölürüm yalnızlığımın nöbetinde.**",
"**Yalanların içinde tek gerçeksin benim gözümde, sahte gülüşlerin içinde tek doğrusun sevdim seni bir kere, dünya dönse de inadına çevremde, ben sensiz nefes alamıyorum dünya kimin umurunda banane.**",
"**Bir gülüşünle hayata dönerim yeniden, sensiz buz tutan için alev alev olur gülüşünle, sensiz bir yalan olurum yalan hayatın içinde, seninle gerçekleri yaşarım gerçek olan aşkımın içinde.**",
"**Gülüşünle yalnızlığıma bir son veriyorum her gece, seni hayal edince mutlu oluyorum yalnızlığımın gölgesinde, seninle ölüme bile giderim düşünmem bir an bile, sensin benim tek sevdiğim bu can sana feda olsun her nefesimde.**",
"**Aşk bir su damlası olsaydı okyanusları, bir yaprak olsaydı bütün ormanları, bir yıldız olsaydı tüm kainatı sana vermek isterdim. Ama sadece seni seven kalbimi verebiliyorum.**",
"**Ne zaman batan güneşe baksam hüzünlenirim yanımda yoksun diye, ne zaman yıldızlara baksam üşürüm hayalinle ısınırım, ne zaman yanımda olsan işte bunların hepsini unuturum bir tanem benim.**",
"**Hayatta üç şeyi sevdim. Seni, kalbimi, ümit etmeyi. Seni sevdim, sensin diye. Kalbimi sevdim, seni sevdi diye. Ümit etmeyi sevdim, belki seversin diye.**",
  ]

@telethon_client.on(events.NewMessage(pattern=r"^\.yavsa"))
async def egockiral(event):
    await event.edit(f"{choice (EGOCKİRAL)}")
          
@telethon_client.on(events.NewMessage(pattern=r'\.ip'))
async def handle_ip(event):
  if str(event.sender_id) in owner_id:
    try:     
        message = event.message

        ip = message.text.split(' ')[1]     
    	
        api_url = f'http://ip-api.com/json/{ip}'
        response = requests.get(api_url)

        if response.status_code == 200:
               data = json.loads(response.text)
               if "country" in data:
                      response_message = f"\n" \
                              f"ÜLKE: {data['country']}\n" \
                              f"ÜLKE KODU: {data['countryCode']}\n" \
                              f"BÖLGE: {data['region']}\n" \
                              f"BÖLGE ADI: {data['regionName']}\n" \
                              f"ŞEHİR: {data['city']}\n" \
                              f"ZIP KOD: {data['zip']}\n" \
                              f"ENLEM: {data['lat']}\n" \
                              f"SAAT DİLİMİ: {data['timezone']}\n" \
                              f"İSP: {data['isp']}\n" \
                              f"ORG: {data['org']}\n" \
                              f""
                              
        await message.reply( response_message)

    except IndexError:
        await message.reply("Geçerli Bir IP Adresi  Girin.")
    except Exception as e:
        await message.reply(f"Data bulunamadı.")    
               
                                
class FlagContainer:
    is_active = False            
    

islami_sozler = [
    "Hayatta karşılaştığınız en büyük zorluk nedir?",
    "Bir günü nasıl daha verimli geçirebilirsiniz?",
    "En çok hangi şeyler sizi mutlu eder?",
    "Hangi kitap, hayatınızı değiştirdi?",
    "Bir hayaliniz varsa, ona ulaşmak için ne yapıyorsunuz?",
    "Herkesin öğrenmesi gereken bir yaşam dersi nedir?",
    "Sizce en değerli şey nedir?",
    "Günümüz dünyasında mutluluğun sırrı nedir?",
    "Birçok insan için en büyük korku nedir?",
    "Dünyada yaşayan en ilginç insan kimdir?",
    "İnsanlar arasındaki en büyük iletişim problemi nedir?",
    "Sizce başarıyı tanımlarken hangi ölçütleri kullanmak daha doğru olur?",
    "Hayatınızda karşılaştığınız en ilginç tesadüf nedir?",
    "Bir insanın en değerli özelliği sizce nedir?",
    "Yaşamın amacını nasıl tanımlarsınız?",
    "Kendi hayatınızda yaptığınız en büyük hatayı nasıl telafi ettiniz?",
    "İnsanların çoğu hangi konuda yanlış bir şekilde düşünür?",
    "Hiç unutamadığınız bir anınızı bizimle paylaşır mısınız?",
    "Hangi kültürel farklar sizce insanları daha da zenginleştiriyor?",
    "Teknolojinin hayatımıza kattığı en önemli şey nedir?",
    "Bir insanın güvenini kazanmak için ne yapmalıyız?",
    "Hangi değerler sizin için her şeyin önündedir?",
    "Sosyal medya kullanımı hakkında ne düşünüyorsunuz?",
    "İnsan ilişkilerinde empatiyi artırmak için neler yapılabilir?",
    "En çok hangi konu hakkında konuşmak istersiniz?",
    "Hayatta bir şey değiştirebilseydiniz, neyi değiştirirdiniz?",
    "Bir insanın potansiyelini gerçekleştirmesi için hangi adımları atması gerekir?",
    "Hangi duygusal durumlarla başa çıkmakta zorlanırsınız?",
    "Herkesin sahip olması gerektiğine inandığınız bir beceri var mı?",
    "Sizin için başarı nedir?",
    "Doğru bir liderin sahip olması gereken özellikler nelerdir?",
    "Hangi insanları daha çok seviyorsunuz: pozitif olanları mı yoksa negatif olanları mı?",
    "Hayatta kazandığınız en büyük ders neydi?",
    "Hangi filmin veya dizinin sizi derinden etkilediğini düşünüyorsunuz?",
    "Bir insanın kendini tanıması için hangi süreçlerden geçmesi gerekir?",
    "Kendinizi nasıl tanımlarsınız?",
    "Bir hedef belirlemek için en iyi yöntemler nelerdir?",
    "Ne tür insanlar sizi daha çok motive eder?",
    "Sağlıklı bir yaşam tarzı için hangi alışkanlıkları edinmek önemlidir?",
    "Bir konuda ne kadar bilgi sahibi olmanız gerektiğini nasıl belirlersiniz?",
    "Bir başarısızlık sonrası nasıl yeniden ayağa kalkabilirsiniz?",
    "Geleceğe yönelik en büyük hayaliniz nedir?",
    "Hayatınızda aldığınız en değerli tavsiye nedir?",
    "İnsanlar arasındaki anlayış farklılıkları nasıl aşılabilir?",
    "Hangi özelliklerinizi geliştirmek istersiniz?",
    "İyi bir arkadaş olmak için hangi değerler önemlidir?",
    "Duygusal zekânın rolü hakkında ne düşünüyorsunuz?",
    "Karar alma süreçlerinizde hangi faktörler en belirleyicidir?",
    "Başkalarına yardım etmek için hangi yolları tercih edersiniz?",
    "Dünyadaki en büyük sorunları çözmek için hangi adımlar atılmalıdır?",
    "Hayatınızda sizi en çok motive eden şey nedir?",
    "En çok hangi konuda yanlış anlaşıldığınızı düşünüyorsunuz?",
    "Bir insanın mutlu olabilmesi için neye ihtiyacı vardır?",
    "En çok hangi değerleri kendinize rehber edinirsiniz?",
    "Çevremizdeki insanlara nasıl daha iyi bir destek olabilirsiniz?",
    "Hayatta karşılaştığınız en ilginç insan kimdi?",
    "Hiç hayal kırıklığı yaşadınız mı? Eğer yaşadıysanız, nasıl başa çıktınız?",
    "İnsanların hayatta kalması için hangi temel becerilere sahip olmaları gerekir?",
    "Sizi daha çok mutlu eden şeyler arasında neler var?",
    "Yaşadığınız şehri tanımlamak için hangi kelimeleri kullanırsınız?",
    "Herkesin hayatında mutlaka gerçekleştirmesi gereken bir hedef var mı?",
    "Bir kişinin kendi değerini anlaması için hangi adımları atması gerekir?",
    "İnsanlar neden bazen kendilerine zarar verir?",
    "Toplumda adaletin sağlanması için hangi önlemler alınmalıdır?",
    "Herkesin öğrenmesi gereken bir beceri nedir?",
    "Geleceğe dair umutlu musunuz?",
    "Çocukların gelişiminde en önemli faktörler nelerdir?",
    "Yaşam amacını bulmak için hangi yoldan gitmek gerekir?",
    "Bir insanın hayatta doğru yolu bulması için ne yapması gerekir?",
    "İnsan ilişkilerinde en çok hangi değerlerin ön planda olması gerektiğini düşünüyorsunuz?",
    "Hangi durumlar insanları zor durumda bırakır ve bu durumlar nasıl aşılabilir?",
    "Toplumların gelişmesi için en önemli faktör nedir?",
    "İnsanların kendi potansiyellerini gerçekleştirmelerini nasıl sağlarız?",
    "Zorluklar karşısında insanların güçlerini nasıl keşfettiklerini düşünüyorsunuz?",
    "Hangi duyguların insanları daha güçlü kıldığını düşünüyorsunuz?",
    "Hiç umudunuzu kaybettiğiniz anlar oldu mu?",
    "Sizin için anlamlı olan bir müzik parçası var mı?",
    "Ne zaman kendinizi en huzurlu hissettiniz?",
    "Başkaları için örnek bir insan olmak isteseniz, hangi özellikleri taşırdınız?",
    "En çok hangi sorular sizi düşündürür?",
    "İnsanların kendilerini ifade etme biçimleri hakkında ne düşünüyorsunuz?",
    "Hayatınızdaki en değerli anı hangi anıdır?",
    "İnsanlar arasında daha fazla anlayış sağlamak için neler yapılabilir?",
    "Kendinizi gelecekte nasıl görmek istersiniz?",
    "Hangi beceriler hayatı kolaylaştırır?",
    "Hayatta aldığınız en önemli karar neydi?",
    "Zorluklarla başa çıkarken hangi stratejileri kullanıyorsunuz?",
    "Hangi konularda daha fazla bilgi sahibi olmak istersiniz?",
    "İnsanların kendilerini geliştirebilmesi için hangi kaynaklardan yararlanması gerektiğini düşünüyorsunuz?",
    "Hayatınızın bir film olsaydı, adı ne olurdu?",
    "İnsanların hayatlarında daha fazla anlam aramalarını nasıl sağlarsınız?",
    "Ne tür insanlar sizi etkiler?",
    "En ilginç maceranızı anlatır mısınız?",
    "Bir insanın mutluluğa ulaşması için hangi adımlar atılabilir?",
    "İnsanın toplumdaki rolünü nasıl tanımlarsınız?",
    "Sizin için bir başarı nedir?",
    "İnsanlar daha iyi nasıl anlaşabilir?",
    "Hayatınızdaki en önemli deneyimi paylaşır mısınız?",
    "Hangi konularda daha fazla araştırma yapılması gerektiğini düşünüyorsunuz?",
    "Bir insanı tanımak için en önemli şey nedir?",
]

emojiler = ["Orospu Çocuğu",
"Gavat",
"Kahpe",
"GeriZekalı",
"Aptal Orospu Evladı",
"Kafanı skm",
"Oç",
"mezar taşını siktiğim",
"ananın amına tankla girer bazukayla çıkarım,yarrrrrağımın kurma kolu",
"Puşt",
"Pezevenk",
"bütün sülaleni bir çuvala koyar ilk hareket edeni sikerim.",
"amın düdüğü",
"kromozomlarına verdiğiminin oğlu.",
"got lalesi",
"sana küçükken anan emzik yerine baban sikini vermiş maybaşın evladı",
"beyninin kıvrımlarına sokiiim.",
"sen babanın sol taşşaklarında iken, ben annenle langırt oynuyordum.",
"yeni dökülmüş betonun üstünde sikerim gelen geçen hatırana attırır."
"Senin ananın amına yoğurt döker eyfel kulesinin tepesinde bütün avrupaya izlete izlete sikerek yoğurt yapayım",
"Yavaş ol orospu çocuğu ananı kerhaneyemi yetiştiriyon",
"Seni babana müjdeleyen doktorun ses tellerini sikeyim",
"Sana oksijen üreten ağacın yaprağını sikeyim",
"İzzet-ül ikramına bandırılmış karûcatını sikeyim",
"Anneni Alır Boğazın Tepesine Oturturur Hem Avrupaya Hem Asyaya Karşı Sikerim",
"ananı tavana asarım amına smaç basarım",
"kırk orospu bi araya gelse senin gibisini doğuramaz",
"ananın karnında amca yarragımı yedin orospu cocuuu",
"ananın amına çam diker gölgesinde bacını sikerim dogmamış yigenlerinin tohumuna katkıda bulunurum",
"kes ağlamayı sokarım bağlamayı",
"senin anayin amini burgulu matkap ilen oyarim",
"ananin amindan kan çekim kizilaya bagiğliim",
"seni bayir aşagi yatirir kaymayasin diye agzina takoz sokar manzarayi seyrederken gotunden sikerim",
"Veledi amın feryadı(yapanın sözüdür çalanı sikio)",
"amına chevrolet ile girip dört kapısını açayım",
"o götünü bi sikerim, boş minibüste bile ayakta gidersin!",
"ana rahminde ters dönmüş orospu çocuğu",
"götüne filli boya dökerim pompaladıkça ağzınla duvara paintbrush olarak milli takım yazarsın",
"anani telefon diregine asar,paralelden bacina basarim.",
"anasinin amindayken kafasina tam randimanli ermeni yarragi degmis suzme pic",
"amında fındık kırar kabukları götünden sikimle toplarım ",
"ananın amına kızgın demirin soguk tarafıını sokayimde kızgın yerini tutup çıkaramasın orospu",
"babanın şarap çanağına boşalır, anana sütlaç diye yediririm.",
"anneni ikinci abdülhamit ‘in saz ekibi siksin.",
"seni ciltleyip sikerim, dünya klasikleri serisine girersin.",
"senin ananın amına beton dökerim, baban bile sikemez",    
"ananın amına trojan atar uzaktan bağlanır bağlanır sikerim.",
"seni bir sikerim bir daha ne zaman sikecek diye gözlerimin içine bakarsın",
"seni öyle bir sikerim ki bütün tüyün kılın dökülür; hasta kuşlar misali cıscıbıldak kalırsın.",
"ebenin ammına ağaç dikeyim, gölgesinde serinliyeyim.",
"seni bir sikerim, sülalen direnişe geçer.",
"Ananın amına Windows Xp kurup mavi ekran verinceye kadar sikerim.",
"Ananı avradını laciverde boyarım.",
"Ananın ağzına salıncak kurar sallana - sallana sikerim",
"Ebenin amına çam dikerim gölgesinde ananı sikerim.",
"Bütün sülaleni 1 çuvala koyar, ilk hareket edeni sikerim.",
"Seni götünden bi sikerim, boş otobüste ayakta gidersin.",
"40 orospu bir araya gelse senin gibi bir oç doğuramaz.",
"Ananın amına teletabinin antenlerini sokar göbeğindeki televizyondan ulusal porno yayını yaparım.",
"Ananı özgürlük heykelinin yanmayan meşalesinde siker şehri duman ederim.",
"Ananı ikiz kulelerinin yedinci katına cıkartır amına uçakla girerim...",
"Ananın o dazlak kafasına teflon tavayla vurur sersemletir sikerim.",
"Ananın buruşmuş amına tefal ütü basar dümdüz ederim.",
"Ananın amına telefon kablosu sokar paralel hattan bacını sikerim.",
"Ananı fakir mahallenizde yanmayan sokak direğine bağlar sike sike trafoyu patlatırım.",
"Hani benim gençliğim nerde diyen orospu cocugu seni.",
"Ananla karşılıklı sikişirken ay çekirdeği cıtlatırım kabuklarını babanın suratına fırlatırım.",
"Evde göbeğini yere deydirerek sınav cekince kendini atletik sanan abini götünden sikeyim...",
"Saçlarını arkaya tarayınca kendini tarık akan sanan babanıda götünden sikeyim...",
"Tokyo drifti izleyip köyde traktörle drift yapmaya calısan abinin götüne kamyonla gireyim...",
"Kilotlu corapla denize giren kız kardeşinin kafasını suya sokup bogulana kadar sikeyim...",
"Googleye türbanlı karı sikişleri yazan dedeni götünden sikeyim.",
"Ananın amına kolumu sokar kücük kardeşlerini cıkartırımananı neil amstrongla beraber aya cıkartıp siker hardcore movie alırım altın portakal film festivalinde aldıgım ödülü ananın amına sokarım.",
"Ananın amına harry poterin assasını sokar kücük kücük büyücüler cıkartırım...",
"Ananın amına pandora kutusu sokar icinden tavşan cıkartırımananın amına duracel pill atar 10 kata kadar daha güçlü sikerim.",
"Ananı national geographic belgeselinde sikerim insanlar aslan ciftlesmesi görür...",
"Ananın amına 5+1 hoparlör sokar kolonları titretirim.",
"Ananı hollandadaki altın portakal film festivaline götürür amına portakal ağacını sokarım.",
"Ananı ramsstein konserinde pistte sikerim du hast şarkısını tersten okuttururum.",
"Babanın o kokmuş corabını ananın amına sokarımananı galatasaray fenerbahçe derbisinde kale yapar musa sow gibi hatrick yaparım.",
"Ananı klavyemin üstünde sikerken paintte yarak resmi cizip kız kardeşine gönderirim.",
"Ananı jerry kılıgına sokar tom gibi kovalarım elbet bir köşede yakalar sikerim."]

bot_calisiyor = False

@telethon_client.on(events.NewMessage)
async def handle_message(event):
    global bot_calisiyor

    if event.text == ".baslat" and not bot_calisiyor:
        if str(event.sender_id) == owner_id:
            bot_calisiyor = True
            await event.respond("✅ Bot Başlatıldı..\nBot çalışıyor.")
        return
    elif event.text == ".durdur" and bot_calisiyor and str(event.sender_id) == owner_id:
        bot_calisiyor = False
        await event.respond("Bot Durdurma İşlemi Tamamlandı. Bot durduruldu.")
        return 
    elif bot_calisiyor and str(event.sender_id) == owner_id:
        if event.text.startswith(".kfrtag"):
            await emoji_tag(event)
        elif event.text.startswith(".soztag"):
            await soz_tag(event)

async def emoji_tag(event):
    global bot_calisiyor

    if not bot_calisiyor:
        await event.respond("")
        return

    if event.fwd_from:
        return

    chat = await event.get_input_chat()
    async for i in telethon_client.iter_participants(chat):
        if not bot_calisiyor:
            break
        try:
            emoji = random.choice(emojiler)
            if i.username:
                mention = f"@{i.username}"
            else:
                mention = f"[{i.first_name}](tg://user?id={i.id})"
                
            await telethon_client.send_message(chat, f"{mention} {emoji}", parse_mode="md")
            await asyncio.sleep(2)
        except Exception as e:
            print("❌ Hata:", e)

async def soz_tag(event):
    global bot_calisiyor

    if not bot_calisiyor:
        await event.respond("")
        return

    if event.fwd_from:
        return

    chat = await event.get_input_chat()
    async for i in telethon_client.iter_participants(chat):
        if not bot_calisiyor:
            break
        try:
            islami_soz = random.choice(islami_sozler)
            if i.username:
                mention = f"@{i.username}"
            else:
                mention = f"[{i.first_name}](tg://user?id={i.id})"
                
            await telethon_client.send_message(chat, f"{islami_soz} - {mention}", parse_mode="md")
            await asyncio.sleep(4)
        except Exception as e:
            print("❌ Hata:", e)
            
                                
@telethon_client.on(events.NewMessage(pattern=r"^.evlenme ?(.*)"))
async def _(event):
    oran = event.pattern_match.group(1)
    evlilik = random.randint(0, 100)
    if not oran:
       await event.edit("`Evlenmek istediğiniz kişiyi yazın`")
    if oran:
       await event.edit(f"**Senin evleneceğin kişi ➪ __{oran}__ 💍 **\n\n🔑 **Gerçekleşme oranı:** `{evlilik}%`")
       
@telethon_client.on(events.NewMessage(pattern=r'\.spam (\d+) (.+)', outgoing=True))
async def spam_message(event):
    count = int(event.pattern_match.group(1))
    message = event.pattern_match.group(2)
    for _ in range(count):
        await event.respond(message)
        
@telethon_client.on(events.NewMessage(pattern=r"^\.kedicik"))
async def kedicik(event):
    if event.fwd_from:
        return
    animation_interval = 0.7
    animation_ttl = range(0, 11)

    #input_str = event.pattern_match.group(1)

    #if input_str == "kedicik":
    animation_chars = [       
            "`ᅠᅠᅠᅠᅠ🧶🏃🏼‍♂\n ᅠᅠ  ᅠ  ᅠ  -Yakala Kedicik\n           ᅠᅠ  \n     ᅠᅠᅠᅠ   \n  ᅠᅠᅠᅠᅠ  🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ 🧶ᅠ  \n           ᅠᅠ  \n     ᅠᅠᅠᅠ   \n  ᅠᅠᅠᅠᅠ  🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ  \n           🧶ᅠ  \n     ᅠᅠᅠᅠ   \n  ᅠᅠᅠᅠᅠ  🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ  \n             ᅠ  \n       🧶ᅠᅠᅠ   \n  ᅠᅠᅠᅠᅠ  🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ  \n             ᅠ  \n         ᅠᅠᅠ   \n  🧶ᅠᅠᅠᅠ  🐈`",    
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ  \n             ᅠ  \n         ᅠᅠᅠ   \n  🧶ᅠᅠᅠ 🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ  \n             ᅠ  \n         ᅠᅠᅠ   \n  🧶ᅠᅠᅠ🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ  \n             ᅠ  \n         ᅠᅠᅠ   \n  🧶ᅠᅠ🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ  \n             ᅠ  \n         ᅠᅠᅠ   \n  🧶ᅠ🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ  \n             ᅠ  \n        -Miyaav ᅠᅠᅠ \n  🧶🐈`",
            "`ᅠᅠᅠᅠᅠ  🏃🏼‍♂\n ᅠᅠ  ᅠ   ᅠ -Aferin Kedime\n             ᅠ  \n         ᅠᅠᅠ   \n  🧶🐈`"
        ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])
        
@telethon_client.on(events.NewMessage(pattern="^\.opucuk", outgoing=True))
async def opucuk(event):  
     await event.edit("**Şşştt**")
     time.sleep(2.00)     
     await event.edit("**Seni Öpe Bilir Miyim ?**")
     time.sleep(2.00)     
     await event.edit("**Bak Öpüyom Haa**")
     time.sleep(2.00)    
     await event.edit("**Muuaahh**")
     time.sleep(2.00)
                                                             
@telethon_client.on(events.NewMessage(outgoing=True, pattern="^.otuzbir"))
async def jokerpluginn(event):
    if event.fwd_from:
        return
    animation_interval = 0.8
    await asyncio.sleep(0.1)
    animation_ttl = range(0, 7)
    await event.edit("31 çekiom kiral")
    animation_chars = [
"...............▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n████████████████████\n▓▓▓▓▓▓█░░░░░░░░░░░░░███\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░█░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░██\n███████████████████\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n...▄█▓░░░░░░░░░▓█▄\n..▄▀░░░░░░░░░░░░░ ▀▄\n.▐░░░░░░░▀▄▒▄▀░░░░░░▌\n▐░░░░░░░▒▒▐▒▒░░░░░░░▌\n▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌\n.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀\n.. ▀▀▀▀▀▀▀▀▀▀▀▀",     
"...............▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n████████████████████\n▓▓▓▓▓▓█░░░░░░░░░░░░░███\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░█░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░██\n███████████████████\n...▄█▓░░░░░░░░░▓█▄\n..▄▀░░░░░░░░░░░░░ ▀▄\n.▐░░░░░░░▀▄▒▄▀░░░░░░▌\n▐░░░░░░░▒▒▐▒▒░░░░░░░▌\n▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌\n.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀\n.. ▀▀▀▀▀▀▀▀▀▀▀▀",
"...............▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n████████████████████\n▓▓▓▓▓▓█░░░░░░░░░░░░░███\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░█░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░██\n███████████████████\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n...▄█▓░░░░░░░░░▓█▄\n..▄▀░░░░░░░░░░░░░ ▀▄\n.▐░░░░░░░▀▄▒▄▀░░░░░░▌\n▐░░░░░░░▒▒▐▒▒░░░░░░░▌\n▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌\n.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀\n.. ▀▀▀▀▀▀▀▀▀▀▀▀",     
"...............▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n████████████████████\n▓▓▓▓▓▓█░░░░░░░░░░░░░███\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░█░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░██\n███████████████████\n...▄█▓░░░░░░░░░▓█▄\n..▄▀░░░░░░░░░░░░░ ▀▄\n.▐░░░░░░░▀▄▒▄▀░░░░░░▌\n▐░░░░░░░▒▒▐▒▒░░░░░░░▌\n▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌\n.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀\n.. ▀▀▀▀▀▀▀▀▀▀▀▀",
"...............▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n███████████████████\n▓▓▓▓▓▓█░░░░░░░░░░░░░███\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░█░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░██\n███████████████████\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n...▄█▓░░░░░░░░░▓█▄\n..▄▀░░░░░░░░░░░░░ ▀▄\n.▐░░░░░░░▀▄▒▄▀░░░░░░▌\n▐░░░░░░░▒▒▐▒▒░░░░░░░▌\n▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌\n.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀\n.. ▀▀▀▀▀▀▀▀▀▀▀▀",     
"...............▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n████████████████████\n▓▓▓▓▓▓█░░░░░░░░░░░░░███\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░█░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░██\n███████████████████\n...▄█▓░░░░░░░░░▓█▄\n..▄▀░░░░░░░░░░░░░ ▀▄\n.▐░░░░░░░▀▄▒▄▀░░░░░░▌\n▐░░░░░░░▒▒▐▒▒░░░░░░░▌\n▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌\n.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀\n.. ▀▀▀▀▀▀▀▀▀▀▀▀",
"...............▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n████████████████████\n▓▓▓▓▓▓█░░░░░░░░░░░░░███\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░█░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░██\n███████████████████\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n...▄█▓░░░░░░░░░▓█▄\n..▄▀░░░░░░░░░░░░░ ▀▄\n.▐░░░░░░░▀▄▒▄▀░░░░░░▌\n▐░░░░░░░▒▒▐▒▒░░░░░░░▌\n▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌\n.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀\n.. ▀▀▀▀▀▀▀▀▀▀▀▀",     
"...............▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n████████████████████\n▓▓▓▓▓▓█░░░░░░░░░░░░░███\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░█░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░██\n███████████████████\n...▄█▓░░░░░░░░░▓█▄\n..▄▀░░░░░░░░░░░░░ ▀▄\n.▐░░░░░░░▀▄▒▄▀░░░░░░▌\n▐░░░░░░░▒▒▐▒▒░░░░░░░▌\n▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌\n.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀\n.. ▀▀▀▀▀▀▀▀▀▀▀▀",

]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i %9 ])

"""TÜM ERMENİLERİ GÖTTEN 

@slmbenjok | @jokerpluginn
"""

S = """
..................▄▄▄▄▄
..............▄▌░░░░▐▄
............▐░░░░░░░▌
....... ▄█▓░░░░░░▓█▄
....▄▀░░   ▐░░░░░░▌░▒▌
.▐░░░░   ▐░░░░░░▌░░░▌
▐ ░░░░   ▐░░░░░░▌░░░▐
▐ ▒░░░   ▐░░░░░░▌░▒▒▐
▐ ▒░░░   ░░░░░░░▌░▒▐
..▀▄▒▒▒  ▐░░░░░░▌▄▀
........ ▀▀▀▐░░░░░░▌
.................▐░░░░░░▌
.................▐░░░░░░▌
.................▐░░░░░░▌
.................▐░░░░░░▌
................▐▄▀▀▀▀▀▄▌
...............▐▒▒▒▒▒▒▒▒▌
...............▐▒▒▒▒▒▒▒▒▌
................▐▒▒▒▒▒▒▒▌
..................▀▌▒▀▒▐▀
                       💧💧💧
                         💧 💧
                            💧
🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲🇦🇲
 """

@telethon_client.on(events.NewMessage(pattern="^\.erm"))
async def ramoseks(event):
    if event.fwd_from:
        return
    animation_ttl = range(0, 1)
    animation_chars = [S]
    for i in animation_ttl:
        await asyncio.sleep(2.5)
        await event.edit(animation_chars[i %1 ])
        
         
@telethon_client.on(events.NewMessage(pattern=r"^\.tavlama"))
async def tavlama(event):  
    time.sleep(0.8)
    await event.edit("❤️**Ben**❤️")
    time.sleep(0.7)
    await event.edit("❤️__Sana__❤️")
    time.sleep(0.7)
    await event.edit("❤️__Yürümek__🖤")
    time.sleep(0.7)
    await event.edit("🖤__İstiyorum__❤️")
    time.sleep(0.8)
    await event.edit("❤️__Aç Kalbinin Kapısını__🖤")
    time.sleep(1)
    await event.edit("🖤__Lütfen__❤️")
    time.sleep(1.7)
    await event.edit("**Kapı Açıldı Saldır Komutu Bekleniyor** 🐅 🐆")
    time.sleep(1.5)
    await event.edit("__Komut Geldi Bombalar Hazırlanıyor__ 🏹 🏹")
    time.sleep(1.5)
    await event.edit("**Saldırı Başlatıldı** 🏰 💣")
    time.sleep(3)
    await event.edit("__Bombaya Gerek yok, Gözlerindeki Derinlik İçimi Yıkmaya Yeter〽️__ (*˘︶˘*).｡*♡ ")
    time.sleep(3)
    await event.edit("`Bana şair diyorlar da senin şiir olduğunu göremiyorlar.`✍🏻")
    time.sleep(2)
    await event.edit("`Düşürme Tamamlandı...`")
    time.sleep(2)
    await event.edit("`Sosyal Medya Hesabı İsteniyor...`")
    time.sleep(1.8)
    await event.edit("`Özele Bekleniyorsunuz...`")
             
 
@telethon_client.on(events.NewMessage(pattern=r"\.cevir"))
async def cevir_command_handler(event):   
  args = event.message.text.split()
  if event.message.text == ".cevir":
    return await event.edit("`Bir metin belirtmelisin.`")
  metin = " ".join(args[1:])   
  çevrilmiş = GoogleTranslator(source='auto', target='tr').translate(metin)
  return await event.edit(f"**AUTO→TR**\n\n`{çevrilmiş}`")
           
@telethon_client.on(events.NewMessage)
async def pmpermit_handler(event):
  sender = await event.get_sender()
  if event.is_private and pmpermit:    
    if event.sender_id not in approved_chats:
      me = await telethon_client.get_me()
      if sender.id != me.id:
        return await event.respond(pmpermit_msg.replace("first", sender.first_name).replace("username", "@"+sender.username).replace("myname", me.first_name))    
           
@telethon_client.on(events.NewMessage(pattern=r"\.pm"))
async def pmpermit_command_handler(event):
  global pmpermit
  cmd = event.message.text.split()
  if len(cmd) > 1 and len(cmd) < 3:
    if cmd[1] == "on":
      pmpermit = True
      return await event.edit("Aktif")
    elif cmd[1] == "off":
      pmpermit = False
      return await event.edit("Aktif değil")
  else:
    return await event.edit("on/off belirtilmeli.")
    
@telethon_client.on(events.NewMessage(pattern=r"\.edit"))
async def edit_command_handler(event):
  global pmpermit_msg
  cmd = event.message.text.split()
  if len(cmd) > 1:  
    pmpermit_msg = " ".join(cmd[1:])
    return await event.edit("`Mesaj güncellendi!`")
  else:
    return await event.edit("`Geçersiz kullanım!`")
    
@telethon_client.on(events.NewMessage(pattern=r"\.approve"))
async def approve_command_handler(event):
  global approved_chats
  me = await telethon_client.get_me()
  sender = event.sender_id
  if sender == me.id:
    splt = event.message.text.split()
    if len(splt) > 1 and splt[1].isdigit():
      chat_id = int(splt[1])
      if chat_id not in approved_chats:
        approved_chats.append(chat_id)
        await event.edit("Onaylandı")
      else:
        await event.edit("Zaten onaylandı")
    else:
      await event.edit("`Geçersiz komut formatı. Kullanım:` `.approve <user_id>`")

@telethon_client.on(events.NewMessage(pattern=r"\.disapprove"))
async def disapprove_command_handler(event):
    global approved_chats
    me = await telethon_client.get_me()
    sender = event.sender_id
    if sender == me.id:
        splt = event.message.text.split()
        if len(splt) > 1 and splt[1].isdigit():
            chat_id = int(splt[1])
            if chat_id in approved_chats:
                approved_chats.remove(chat_id)
                await event.edit("Onay kaldırıldı")
            else:
                await event.edit("`Bu chat ID'si zaten onaylı değil`.")
        else:
            await event.edit("Geçersiz komut formatı. Kullanım: .disapprove <user_id>") 
                                   
@telethon_client.on(events.NewMessage(pattern=r'^\.kurulum'))
async def my_event_handler(event):
    if event.raw_text.startswith('.kurulum'):
        if str(event.sender_id) != owner_id:
            await event.respond('Bu Komutu Sadece Sahibi Kullanabilir.')
            return

        try:
            idd = int(event.raw_text.split(' ')[1])
            data_Pyro = '{"telegramId":' + str(idd) + '}'
            PyroRobots = requests.post('https://restore-access.indream.app/regdate', headers=headers, data=data_Pyro)

            Pyro = json.loads(PyroRobots.text)
            date = Pyro['data']['date']

            if date:
                await event.respond(f'• Hesabın Telegram Üzerindeki Kuruluş Tarihi {date}')
            else:
                await event.respond('Hata oluştu Lütfen ID\'nizi Doğru Şekilde Gönderdiğinizden Emin Olun.')
        except:
            await event.respond('• Lütfen Hesap ID\'nizi Doğru Şekilde Gönderin.')
            
headers = {
    'Host': 'restore-access.indream.app',
    'Connection': 'keep-alive',
    'x-api-key': 'e758fb28-79be-4d1c-af6b-066633ded128',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7', 
    'Content-Length': '25',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}        
  
@telethon_client.on(events.NewMessage(pattern="^.cikolata"))
async def cikolata(event):
    ANIMASYON = ["""
{\__/} 
( • - • ) 
/>🍫 Al sana çikolata""",
"""
{\__/} 
( • - • ) 
🍫 < \  Yada alma sende vardı
""","""
{\__/} 
( • - • ) 
/>🍫 Yada al kıyamadım
""","""
{\__/} 
( • - • ) 
/>☕ Al bu da yanında olsun
""","""
{\__/} 
( • - • ) 
/>❤️ Bunu da al ama kırma lütfen
""","""
{\__/} 
( • - • ) 
/>💔 Kırma demiştim
""","""
{\__/} 
( • - • ) 
💔<\ Kırdığın için üzgün olmalısın
""","""
{\__/} 
( • - • ) 
/> ❤️ Yada al birtane daha""","""
{\__/} 
( • - • ) 
/>💔 MAL !!!
""","""
{\__/} 
( • - • ) 
/>❤️ Bunu da al ama kırma lütfen yoksa sikerim elini ayağını eline yarrağimi verir mahalle aralarında kafana yırtık don koyar köpek gibi dolaştırırım seni muck askim
"""]
    for anim in ANIMASYON:
        await event.edit(anim)
        await asyncio.sleep(1.4)
                            
@telethon_client.on(events.NewMessage(outgoing=True, pattern="^\.hack"))
async def merkurkedis(event):
    if event.fwd_from:
        return
    animation_interval = 0.4
    animation_ttl = range(0, 22)
    await event.edit("`Kurulum Hazırlanıyor...`")

    animation_chars = [
      "`İşlem başlatılıyor \n(0%) ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
   "`Sistem özellikleri alınıyor. \n(5%) █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
   "`Sistem özellikleri alınıyor.. \n(10%) ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
   "`Sistem özellikleri alınıyor... \n(15%) ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`Betik yürütülüyor. \n(20%) ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`Betik yürütülüyor.. \n(25%) █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`Betik yürütülüyor... \n(30%) ██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`IP adresi alınıyor. \n(35%) ███████▒▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`IP adresi alınıyor.. \n(40%) ████████▒▒▒▒▒▒▒▒▒▒▒▒`",
            "`IP adresi alınıyor... \n(45%) █████████▒▒▒▒▒▒▒▒▒▒▒`",
            "`MAC adresi alınıyor. \n(50%) ██████████▒▒▒▒▒▒▒▒▒▒`",
            "`MAC adresi alınıyor.. \n(55%) ███████████▒▒▒▒▒▒▒▒▒`",
            "`MAC adresi alınıyor... \n(60%) ████████████▒▒▒▒▒▒▒▒`",
            "`Dosyalar yükleniyor. \n(65%) █████████████▒▒▒▒▒▒▒`",
            "`Dosyalar yükleniyor.. \n(70%) ██████████████▒▒▒▒▒▒`",
            "`Dosyalar yükleniyor... \n(75%) ███████████████▒▒▒▒▒`",
            "`Dosyalar yükleniyor. \n(80%) ████████████████▒▒▒▒`",
            "`Dosyalar yükleniyor.. \n(85%) █████████████████▒▒▒`",
            "`Dosyalar yükleniyor... \n(90%) ██████████████████▒▒`",
            "`Dosyalar yükleniyor. \n(95%) ███████████████████▒`",
            "`Temizleniyor.. \n(100%) ███████████████████`",
            "`İşlem Tamam... \n(100%) ███████████████████\n\nCihazınız tarafımızca hacklendi.\nHack'i kaldırmak için 100$ ödeyin `",
            "`Cihazınız tarafımızca hacklendi.\nHack'i kaldırmak için 100$ ödeyin`"
    ]

    for i in animation_ttl:
        await asyncio.sleep(0.1)
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 22])        
        

SAGOPA = [
'`5 IQ`', '`3 IQ`', '`10 IQ`', '`15 IQ`', '`30 IQ`', '`25 IQ`', '`54 IQ`', '`20 IQ`', '`1 IQ`', '`55 IQ`', '`85 IQ`', '`120 IQ`', '`60 IQ`', '` 45 IQ`', '`75 ÏQ`'
  ]

@telethon_client.on(events.NewMessage(pattern=r"^.iqtest (.*)"))
async def sokus(event):
    if event.fwd_from:
        return
    ani_first_interval = 2.5
    ani_sec = range(0, 7)
    u_name = event.pattern_match.group(1)
   
    ani_first = [
            f"**{u_name}** IQ'Nu Öğrenmeye Hazır Mısın❓❓",
            f"**🧠 IQ TESTİ 🧠**" ,
            f"**🧠 IQ TESTİ 🧠**\n\n**⭕** Test yapılıyor.",    
            f"**🧠 IQ TESTİ 🧠**\n\n**⭕** Test yapılıyor..\n**⁉️** Test kontrol ediliyor..",
            f"**🧠 IQ TESTİ 🧠**\n\n**⭕** Test yapılıyor...\n**⁉️** Test kontrol ediliyor..\n**💻** Test kontrol edildi..",
            f"**🧠 IQ TESTİ 🧠**\n\n**⭕** Test Yapılıyor.. \n**⁉️** Test kontrol ediliyor...\n**💻** Test kontrol edildi..\n**👨‍💻** Sonuç bekleniliyor...",
            f"**🧠 IQ TESTİ 🧠**\n\n**⭕** Test Yapılıyor.. \n**⁉️** Test kontrol ediliyor...\n**💻** Test kontrol edildi..\n**😰** Sonuç bekleniliyor...\n\n**💾SONUÇ:** {random.choice(SAGOPA)}"
        ]
        
    for j in ani_sec:
        await asyncio.sleep(ani_first_interval)
        await event.edit(ani_first[j % 7])         

@telethon_client.on(events.NewMessage(pattern=r'^\.aç(?: |$)(.*)'))
async def open_file(event):
    if event.sender_id != int(owner_id):
        await event.reply("")
        return

    reply_message = await event.get_reply_message()
    
    if reply_message and reply_message.media:
        file_path = await telethon_client.download_media(reply_message)
        
        try:
            with open(file_path, "r") as file:
                content = file.read()
                
                if len(content) > 4095:
                    await event.reply("Üzgünüm, dosya çok büyük.")
                else:
                    await event.reply(f"`{content}````")
        except Exception as e:
            await event.reply(f"Dosya okuma hatası: {str(e)}")
        finally:
            os.remove(file_path)

@telethon_client.on(events.NewMessage(pattern="^.ttf(?: |$)(.*)"))
async def get_file(event):
    if event.sender_id != int(owner_id):
        await event.reply("")
        return

    file_name = event.text[5:]
    reply_message = await event.get_reply_message()

    if reply_message:
        file_content = reply_message.message
        with open(file_name, "w") as file:
            file.write(file_content)
        await event.delete()

        await telethon_client.send_file(event.chat_id, file_name, force_document=True)

        await telethon_client(JoinChannelRequest("@ramowlf"))
        await telethon_client(JoinChannelRequest("@BotAltyapiKanali"))

@telethon_client.on(events.NewMessage(pattern=r"^.hayal ?(.*)"))
async def _(event):
    hayal = event.pattern_match.group(1)
    sayı = random.randint(0, 100)
    if not hayal:
       await event.edit("`Hayalinizı söyleyin`")
    if hayal:
       await event.edit(f"**Senin hayalin ➪ __{hayal}__ ✨  **\n\n💠 **Gerçekleşme oranı:** `{sayı}%`") 

@telethon_client.on(events.NewMessage(pattern=r"^[Nn][Aa][Pp][İi][Mm]$"))
async def benimol(event):
  
     await event.edit("**N**")
     time.sleep(0.25)
     
     await event.edit("**Na**")
     time.sleep(0.25)
     
     await event.edit("**Nap**")
     time.sleep(0.25)
     
     await event.edit("**Napi**")
     time.sleep(0.31)
     
     await event.edit("**Napim**")
     time.sleep(0.31)
     
     await event.edit("**ㅤㅤ ㅤ**")
     time.sleep(0.31)
     
     await event.edit("**Napim**")
     time.sleep(0.31)
     
     await event.edit("**ㅤㅤ ㅤ**")
     time.sleep(0.31)
     
     await event.edit("**Napim**")
     time.sleep(0.20)
     
     await event.edit("**ㅤ ㅤㅤ**")
     time.sleep(0.20)
     
     await event.edit("**Napim**")
     time.sleep(0.20)
     
     await event.edit("NApim")
     time.sleep(0.25)
     
     await event.edit("NAPim")
     time.sleep(0.25)
     
     await event.edit("NAPİm")
     time.sleep(0.25)
     
     await event.edit("NAPİM")
     time.sleep(0.25)
     
     await event.edit("N")
     time.sleep(0.25)
     
     await event.edit("ㅤA")
     time.sleep(0.25)
     
     await event.edit("ㅤㅤP")
     time.sleep(0.25)
     
     await event.edit("ㅤㅤㅤİ")
     time.sleep(0.25)
     
     await event.edit("ㅤㅤㅤㅤM")
     time.sleep(0.25)
     
     await event.edit("N A P İ M")
     time.sleep(0.25)             

@telethon_client.on(events.NewMessage(pattern=r"^\.gay ?(.*)"))
async def rand(event): 
    u_name = event.pattern_match.group(1)
    GAY = ['1%','2%','3%','4%','5%','6%','7%','8%','9%','10%','11%','12%','13%','14%','15%','16%','17%','18%','19%','20%','21%','22%','23%','24%','25%','26%','27%','28%','29%','30%','31%','32%','33%','34%','35%','36%','37%','38%','39%','40%','41%','42%','43%','44%','45%','46%','47%','48%','49%','50%','51%','52%','53%','54%','55%','56%','57%','58%','59%','60%','61%','62%','63%','64%','65%','66%','67%','68%','69%','70%','71%','72%','73%','74%','75%','76%','77%','78%','79%','80%','81%','82%','83%','84%','85%','86%','87%','88%','89%','90%','91%','92%','93%','94%','95%','96%','97%','98%','99%','100%']
    await event.edit(f"{u_name} `Adlı Kişinin Ne Kadar` **Gay** `Olduğu Araştırılıyor...`") 
    donus = random.randint(15,40)
    sayi = 0
    await asyncio.sleep(0.3)
    for i in range(0, donus):
    	await asyncio.sleep(0.1)
    	sayi = random.randint(1, 100)

    await asyncio.sleep(0.1)
    await event.edit(f"{u_name} Adlı Kişinin Şu Kadar Gay Olduğu Tespit Edildi: `"+GAY[sayi-1]+"`")        
                                             
@telethon_client.on(events.NewMessage(outgoing=True, pattern="^\.as$"))
async def merkurkedissa(event):

    if event.fwd_from:
        return

    animation_interval = 0.4
    animation_ttl = range(0, 11)
    await event.edit("Aleyküm selam..💧")

    animation_chars = [
        "**Aleyküm Selam 🌟**",
        "📌As",
        "❗A ve S",
        "🔱 Ase",
        "🔰 Hoşgeldin",
        "🎄As",
        "⛱ Sonunda geldin 📡",
        "🍁 Sanada Selammm",
        "💥 Nabre",
        "**🔴 Ase 🔴**"
    ]

    for i in animation_ttl:
        await asyncio.sleep(0.1)
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])
        
@telethon_client.on(events.NewMessage(outgoing=True, pattern="^\.sa"))
async def sa(event):
    animation_interval = 0.4
    animation_ttl = range(0, 12)
    await event.edit("Selamün Aleyküm..🚀🔱")

    animation_chars = [
        "S",
        "SA",
        "SEA",
        "**Selam Almayanı Döverim*",
        "🎄Sea",
        "🔴Selam",
        "⭕Sa",
        "📡Selammm",
        "💉Naber",
        "🌟Ben Geldim",
        "**Hoşgeldim**",
        "**🔥☄Sea**"
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])
        await asyncio.sleep(0.1)
        

@telethon_client.on(events.NewMessage(pattern=r"^.kurt"))
async def kurt(event):
  args = event.message.text.split()
  if len(args) == 1:
    return await event.edit("**Bir isim belirtin**: `.kurt «isim»`")
  await event.edit("`Kürtlük seviyesi kontrol ediliyor...`")
  time.sleep(1)
  await event.edit("`%10`")
  time.sleep(1)
  sayi = random.randint(50, 95)
  await event.edit(f"`%{sayi}`")
  time.sleep(2.5)
  kürtlük = random.randint(0, 100)
  return await event.edit(f"**{' '.join(args[1:])} adlı kişinin k*rtlük seviyesi:** `%{kürtlük}` 💀")
  
@telethon_client.on(events.NewMessage(pattern=r"^.beyin"))
async def husu(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0, 21)
    await event.edit("`Beyin aranıyor🧠🔬...`")
    time.sleep(0.9)
    await event.edit("`Beyin bulundu✅...`")
    time.sleep(0.9)

    animation_chars = [    

        "Senin beynin ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
        "Senin beynin ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
        "Senin beynin ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
        "Senin beynin ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
        "Senin beynin ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
        "Senin beynin ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
        "Senin beynin ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "Senin beynin ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "Senin beynin ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "Senin beynin ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "Senin beynin ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "Senin beynin ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "Senin beynin ➡️ 🧠\n\n            (> ^_^)>🗑",
        "Senin beynin ➡️ 🧠\n\n            <(^_^ <)🗑",
        "Senin beynin ➡️ 🧠\n\n           <(^_^ <) 🗑",
        "Senin beynin ➡️ 🧠\n\n         <(^_^ <)   🗑",
        "Senin beynin ➡️ 🧠\n\n       <(^_^ <)     🗑",
        "Senin beynin ➡️ 🧠\n\n     <(^_^ <)       🗑",
        "Senin beynin ➡️ 🧠\n\n   <(^_^ <)         🗑",
        "Senin beynin ➡️ 🧠\n\n <(^_^ <)           🗑",
        "Senin beynin ➡️ 🧠\n\n             ➡️🗑⬅️",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 21])        
        
@telethon_client.on(events.NewMessage(pattern=r"^\.ölüm"))
async def rand(event): 
    EMOJILER = ['️28','36','48','115','53','️54' , '63' ,'88','77' , '70' , '33' , '44' , '29' ,'30','100','92','67','33','47','51','61','84','97','112','49','38']
    TR = ['','☠','❄️','🏹','⚔','🤭','😝','🥺','😊']
    await event.edit("`Ölüm Yaşın Hesaplanıyor ...`") 
    donus = random.randint(18,120)
    sayi = 0
    await asyncio.sleep(0.6)
    for i in range(0, donus):
    	await asyncio.sleep(0.1)
    	sayi = random.randint(1, 6)
    	try:
    		await event.edit("`Ölüceğin Yaşı Ögrenmeye Hazırmısın ?..`"+TR[sayi-1]+"")
    	except:
        	continue

    await asyncio.sleep(0.1)
    await event.edit("**Öleceğin yaş Hesaplandı** : 😔 "+EMOJILER[sayi-1]+" **Yaşında Ölüceksin.(**")
        
        
@telethon_client.on(events.NewMessage(pattern="^[Nn][Aa][Bb][Ee][Rr]$", outgoing=True))
async def benimol(event):
  
     await event.edit("**N😊**")
     time.sleep(0.25)
     
     await event.edit("**Na😘**")
     time.sleep(0.25)
     
     await event.edit("**Nab🤗**")
     time.sleep(0.25)
     
     await event.edit("**Nabe🔥**")
     time.sleep(0.31)
     
     await event.edit("**Naber👻**")
     time.sleep(0.31)
     
     await event.edit("**ㅤㅤ ㅤ**")
     time.sleep(0.31)
     
     await event.edit("**Naber☘️😇**")
     time.sleep(0.31)
     
     await event.edit("**ㅤㅤ ㅤ**")
     time.sleep(0.31)
     
     await event.edit("**Naber💀**")
     time.sleep(0.20)
     
     await event.edit("**ㅤ ㅤㅤ**")
     time.sleep(0.20)
     
     await event.edit("**Naber💝**")
     time.sleep(0.20)
     
     await event.edit("**Naber💥**")
     time.sleep(0.25)
     
     await event.edit("**NAber‼️**")
     time.sleep(0.25)
     
     await event.edit("**NABer⭕**")
     time.sleep(0.25)
     
     await event.edit("**NABEr☠️**")
     time.sleep(0.25)
     
     await event.edit("**NABER💯**")
     time.sleep(0.25)
     
     await event.edit("**N**")
     time.sleep(0.25)
     
     await event.edit("**ㅤA**")
     time.sleep(0.25)
     
     await event.edit("**ㅤㅤB**")
     time.sleep(0.25)
     
     await event.edit("**ㅤㅤㅤE**")
     time.sleep(0.25)
     
     await event.edit("**ㅤㅤㅤㅤR**")
     time.sleep(0.25)
     
     await event.edit("**☠️N A B E R☠️**")
     time.sleep(0.25)
     
@telethon_client.on(events.NewMessage(pattern="^[Hh][Oo][Ss][Gg][Ee][Ll][Dd][İi][Nn]$", outgoing=True))
async def benimol(event):
  
     await event.edit("**HO😊**")
     time.sleep(0.25)
     
     await event.edit("**HOŞ😘**")
     time.sleep(0.25)
     
     await event.edit("**HOŞ GE🤗**")
     time.sleep(0.25)
     
     await event.edit("**HOŞ GELDİN🔥**")
     time.sleep(0.31)
     
     await event.edit("**Hoş Geldin👻**")
     time.sleep(0.31)
     
     await event.edit("**ㅤㅤ ㅤ**")
     time.sleep(0.31)
     
     await event.edit("**Hoş Geldin☘️😇**")
     time.sleep(0.31)
     
     await event.edit("**ㅤㅤ ㅤ**")
     time.sleep(0.31)
     
     await event.edit("**Hoş Geldin💀**")
     time.sleep(0.20)
     
     await event.edit("**ㅤ ㅤㅤ**")
     time.sleep(0.20)
     
     await event.edit("**Hoş Geldin💝**")
     time.sleep(0.20)
     
     await event.edit("**Hoş Geldin💥**")
     time.sleep(0.25)
     
     await event.edit("**HOŞ Geldin‼️**")
     time.sleep(0.25)
     
     await event.edit("**HOŞ GEldin⭕**")
     time.sleep(0.25)
     
     await event.edit("**HOŞ GELdin☠️**")
     time.sleep(0.25)
     
     await event.edit("**HOŞ GELDİN💯**")
     time.sleep(0.25)
     
     await event.edit("**HO**")
     time.sleep(0.25)
     
     await event.edit("**ㅤŞ**")
     time.sleep(0.25)
     
     await event.edit("**ㅤㅤGE**")
     time.sleep(0.25)
     
     await event.edit("**ㅤㅤㅤL**")
     time.sleep(0.25)
     
     await event.edit("**ㅤㅤㅤㅤDİN**")
     time.sleep(0.25)
     
     await event.edit("**💯H O Ş  G E L D İ N💯**")
     time.sleep(0.25)
     
@telethon_client.on(events.NewMessage(pattern="^[Tt][Aa][Mm][Aa][Mm]$", outgoing=True))
async def sikiskenbalik(event):
  
     await event.edit("**T😊**")
     time.sleep(0.25)
     
     await event.edit("**Ta😘**")
     time.sleep(0.25)
     
     await event.edit("**Tam🤗**")
     time.sleep(0.25)
     
     await event.edit("**Tama🔥**")
     time.sleep(0.31)
     
     await event.edit("**Tamam👻**")
     time.sleep(0.31)
     
     await event.edit("**ㅤㅤ ㅤ**")
     time.sleep(0.31)
     
     await event.edit("**Tamam☘️😇**")
     time.sleep(0.31)
     
     await event.edit("**ㅤㅤ ㅤ**")
     time.sleep(0.31)
     
     await event.edit("**Tamam💀**")
     time.sleep(0.20)
     
     await event.edit("**ㅤ ㅤㅤ**")
     time.sleep(0.20)
     
     await event.edit("**Tamam💝**")
     time.sleep(0.20)
     
     await event.edit("**Tamam💥**")
     time.sleep(0.25)
     
     await event.edit("**TAmam‼️**")
     time.sleep(0.25)
     
     await event.edit("**TAMam⭕**")
     time.sleep(0.25)
     
     await event.edit("**TAMAm☠️**")
     time.sleep(0.25)
     
     await event.edit("**TAMAM💯**")
     time.sleep(0.25)
     
     await event.edit("**T**")
     time.sleep(0.25)
     
     await event.edit("**ㅤA**")
     time.sleep(0.25)
     
     await event.edit("**ㅤㅤM**")
     time.sleep(0.25)
     
     await event.edit("**ㅤㅤㅤA**")
     time.sleep(0.25)
     
     await event.edit("**ㅤㅤㅤㅤM**")
     time.sleep(0.25)
     
     await event.edit("**☘️T A M A M☘️**")
     time.sleep(0.25)    
        
@telethon_client.on(events.NewMessage(pattern='^.sex', outgoing=True))
async def send_sex(event):
    if event.fwd_from:
        return
    sende_sex = 1
    animation_ttl = range(0, 12)
 
    selam = [
        """**ㅤ😐              😕 
  /👕\          <👗\ 
    👖              /|**""",
        """**ㅤ😉          😳
  /👕\       /👗\ 
    👖           /|**""",
        """**ㅤ😚             😒 
  /👕\         <👗> 
    👖             /|**""",
        """**ㅤ 😍         ☺️ 
   /👕\      /👗\ 
     👖          /|**""",
        """**ㅤ😍          😍 
  /👕\       /👗\ 
    👖           /|**""",
        """**ㅤ😘   😊 
  /👕\/👗\ 
    👖   /|**""",
        """**ㅤ😳  😁 
    /|\ /👙\ 
    /     / |**""",
        """**ㅤ😈    /😰\ 
   <|\      👙 
   /🍆    / |**""",
        """**ㅤ😅 
   /() ✊😮 __
   /\         _|   ı |**""",
        """**ㅤ😎 
    /\_,__😫__ 
    //    //   |   ı \**""",
        """**ㅤ😖 
    /\_,💦😋___  
    //         //    ı \**""",
        """**ㅤ😭      ☺️ 
    /|\   /(👶)\ 
    /!\      / \**"""
    ]

    for i in animation_ttl:
        await asyncio.sleep(sende_sex)
        await event.edit(selam[i % 12])

async def main():
    
    await client.start()

    @client.on(events.NewMessage(pattern='^.sex', outgoing=True))
    async def handler(event):
        await send_sex(event)
    
    await client.run_until_disconnected()

        

GÜNAYDIN = ["Sen uyandıysan", "Gün aydı demektir🙃", "Günaydın canım❤️", "Nasılsın?", "Umarım iyisindir 😊", "Hep iyi ol inşallah", "Seviliyorsun❤️❤️❤️❤️"]

@telethon_client.on(events.NewMessage(pattern="^\.gn"))
async def edit_and_send_günaydın(event):
    
    if str(event.sender_id) == owner_id:
        
        for message in GÜNAYDIN:
            await event.edit(message)
            await asyncio.sleep(2)  
            
                    
İYİGECELER = [
    "`Geceleri uzaklara çığlık olur sesim, Denizden çıkan yosun kokusundan keskin sana olan özlemim, Bu gece sırf senin için kapanıyor gözlerim. İyi geceler Herşeyim...`❤️", 
    "`♥ Gece olup güzel gözlerin yenik düştüğünde uykusuzluğa, seni gökyüzünden alıp düşlerime emanet ediyorum, gözlerimden uzaksın belki ama daima yüreğimdesin unutma. İyi geceler.` 💐", 
    "`Rüyaların en güzelini görürken Allah'ın seni koruması için gönderdiği meleğin kanatları öyle büyük olsun ki en masum anında sana kimseler zarar veremesin. İyi geceler meleğim.` 💋",
    "`♥ Bu gönül sana tutkun. Sözlerin yine suskun ne olursa olsun artık, sensizlikten korkuyorum. Bir aradayken ayrıyız. Her şeye rağmen dayanmalıyız. Kayıp gitme ellerimden, korkuyorum sensizlikten, gecelerden. İyi geceler aşkım.` 🌻", 
    "`İnanıyorum hayatta her iyiliğe karşılık verecek olan güzel olan kişiler de var. Saygı herkese olsa bile sevgi hak eden kişiye karşıdır, iyi geceler! 😙`🥰",  
    "`İyi uykular sevgilim, rüyanda buluşmak üzere...🌹`", 
    "`İyi geceler dileme, iyi geceler ol bana yeter sevgilim.😙`", 
    "`Gün bitiyor, sen başlıyorsun. İyi geceler sevgilim.✨`",
    "`En güzel gecelerin en güzel rüyalarını gör sevgilim. Tatlı uykular!`😍",
    "💘`Gökyüzüne bakarım geceleri tatlı rüyalar görmeni isterim tatlı hayaller içinde uyurken gülümsemeni isterim gül yüzlüm iyi geceler...🤗`",
    "😘`Sen görüp görebileceğim en güzel rüyasın, bu rüyadan hiç uyanmak istemiyorum. İyi geceler canım, cananım.💘`",
    "😋`Yeni doğacak güneşin yeni umutlar, yarınlar getirmesi dileğiyle iyi uykular.☀️`",
    "`En güzel rüyaların senin olması, meleklerin uyurken seni koruması dileğiyle… Hayırlı geceler…💝`",
    "😚`Yatsam uzun uzun ve kalkmasam ve sonra bir uyansam her şey yoluna girmiş olsa…💖`",
    "`Yarın sabah uyandığınızda gönlünüzden geçen her güzel şeyin hayalden çıkıp gerçeğe dönüşmesi dileğiyle, hayırlı geceler...`💋",
    "🤗`Tüm yürekler sevinç dolsun, umutlar gerçek olsun, acılar unutulsun, dualarınız kabul ve geceniz hayırlı olsun.❣️`",
    "`Bazen unutmak için uyumak gerek, rüyalar hesaba katmadan. İyi Geceler.`✨",
    "`En güzel gecelerin en güzel rüyalarını gör bir tanem tatlı uykular.`❤️",
    "`Gökyüzüne bakarım geceleri tatlı rüyalar görmeni isterim tatlı hayaller içinde uyurken gülümsemeni isterim gül yüzlüm iyi geceler…`🥀",
]


@telethon_client.on(events.NewMessage(pattern="^\.ig"))
async def edit_and_send_günaydın(event):
    
    if str(event.sender_id) == owner_id:
        
        for message in İYİGECELER:
            await event.edit(message)
            await asyncio.sleep(2)


        
AZERBAYCAN = [
    "`Keçən dəfə anovu nətər sikdimsə anavın qarnındaki 10 il əvvəl tikilmiş tikişlər cırıldı`", 
    "`Səni elə sikərəm ki paralel dünyadaki dədəndə gəlsə sikimi götündən unfollow eləyə bilməz`", 
    "`Bacın o qədər bomba şeydiki hər görəndən 20 günün hərgünü gecə onu fikirləşib sxoy vururam`",
    "`Anavı elə sikdimki oğlu qeyrətə gəlib 'nolar bəsdidə' dedi`", 
    "`Bu saniyə götündə deşiy açıb mamana protiv çaldırajam`",  
    "`Səni elə sikərəm ki meymunlar cəhənnəmindən dədən gəlib üzüvə tüpürər`", 
    "`Götündən qan gələnə kimi, ağzında babasil olana qədər səni amcığından sikərəm`", 
    "`Beynində tromp yaranana qədər ağzından elə sikərəm ki götündən ay başı olarsan`",
    "`Səni dombaldıb götündə oyun oynayaram özdə takımlı`",
    "`Bacıvın döşlərini əncir edib sənə yedizdirərəm`",
    "`Anavn südlü döşünü elə sıxaramki içindəki süd nənəvin amcığına girər şəp şüp`",
    "`Səni elə sikərəmki götündə 10 dənə deşiy yaranar`",
    "`Səni dombaldıb götüvə dildo soxub gül iyi verən ağzıva şlankdan işiyərəm`",
    "`Ağzıva o qədər verərəmki dilivi hiss eləmərsən`",
    "`Sikim o qədər uzundurki götüvə soxsam gözüvə qədər çatıb, gözüvü sikərəm`",
    "`Anavın götünə elə boşaldaramki cəmi 5 ay əkiz içində doğar`",
    "`Sikimdən səni qaydasız döyüşdəki kimi döyərəm`",
    "`Boynuvun qalınlığı Everest dağını keçir uje`",
    "`məmə ucunu kəsib 5 aylıq qardaşıva sosqa kimi verərəm`",
]


@telethon_client.on(events.NewMessage(pattern="^\.azekfr"))
async def edit_and_send_azerbaycan(event):
    
    if str(event.sender_id) == owner_id:
        
        for message in AZERBAYCAN:
            await event.edit(message)
            await asyncio.sleep(4)  

        
        
AMINE = [
    "https://telegra.ph/file/3d7d710ca6b9f087c2939.jpg",
"https://telegra.ph/file/2ae3e359ad350d9025cce.jpg",
"https://telegra.ph/file/ee7f281fbe790fba2cabd.jpg",
"https://telegra.ph/file/62cca4ee6b182eba260fe.jpg",
"https://telegra.ph/file/b51410a7a3f02b233e699.jpg",
"https://telegra.ph/file/b51410a7a3f02b233e699.jpg",
"https://telegra.ph/file/37a03ee79cb510743461d.jpg",
"https://telegra.ph/file/6a015c917e980b0618240.jpg",
"https://telegra.ph/file/081e5ca613d8174ecbcf8.jpg",
"https://telegra.ph/file/081e5ca613d8174ecbcf8.jpg",
"https://telegra.ph/file/641ce4d03bb2ba124782f.jpg",
"https://telegra.ph/file/0fb6ee856d31731b23256.jpg",
"https://telegra.ph/file/c8a45d8d942845ec1e79b.jpg",
"https://telegra.ph/file/ecd22a6a80bd2d22e0432.jpg",
"https://telegra.ph/file/f2a09dd737ebc349978d9.jpg",
"https://telegra.ph/file/7dc8db507acc6c089510d.jpg",
"https://telegra.ph/file/d8e68b72db590df0f95aa.jpg",
"https://telegra.ph/file/265fda43d121c6f5d9530.jpg",
"https://telegra.ph/file/ecd22a6a80bd2d22e0432.jpg",
"https://telegra.ph/file/f2a09dd737ebc349978d9.jpg",
"https://telegra.ph/file/7dc8db507acc6c089510d.jpg",
"https://telegra.ph/file/7dc8db507acc6c089510d.jpg",
"https://telegra.ph/file/d8e68b72db590df0f95aa.jpg",
"https://telegra.ph/file/265fda43d121c6f5d9530.jpg",
"https://telegra.ph/file/704777fd833595fafa154.jpg",
"https://telegra.ph/file/f53a18a1612684cca2e75.jpg",
"https://telegra.ph/file/f53a18a1612684cca2e75.jpg",
"https://telegra.ph/file/a02863f086bb93e7b09b3.jpg",
"https://telegra.ph/file/a02863f086bb93e7b09b3.jpg",
"https://telegra.ph/file/c2c7f5f8bd420b9afe875.jpg",
"https://telegra.ph/file/af64f67bb80a75b91fc81.jpg",
"https://telegra.ph/file/704777fd833595fafa154.jpg",
"https://telegra.ph/file/f53a18a1612684cca2e75.jpg",
"https://telegra.ph/file/a02863f086bb93e7b09b3.jpg",
"https://telegra.ph/file/c2c7f5f8bd420b9afe875.jpg",
"https://telegra.ph/file/d6cf9422b50e8329a04fe.jpg",
"https://telegra.ph/file/d6cf9422b50e8329a04fe.jpg",
"https://telegra.ph/file/f68be6b800f9affc23906.jpg",
"https://telegra.ph/file/a35a8bd3f9f29c8fd83f7.jpg",
"https://telegra.ph/file/54a0154f9e48e0a1a698b.jpg",
"https://telegra.ph/file/e1a49941edb62de55a1cd.jpg",
"https://telegra.ph/file/7bac01cef8f5e517f0023.jpg",
"https://telegra.ph/file/8aafdb214e01c348efb5a.jpg",
"https://telegra.ph/file/e04911504aaf8d4427655.jpg",
"https://telegra.ph/file/6aef40b7109abf794065e.jpg",
"https://telegra.ph/file/c4e76fa47ea029651ba85.jpg",
"https://telegra.ph/file/57069cac7c3002e7823da.jpg",
"https://telegra.ph/file/3d7d710ca6b9f087c2939.jpg"
]

GOT = [
    "https://telegra.ph/file/c69daf6d119d90d7c1d8f.jpg",
"https://telegra.ph/file/d7eafb14a3294a49c9ed0.jpg",
"https://telegra.ph/file/8104aa15fe751af206c14.jpg",
"https://telegra.ph/file/ca478de4b507f44f9ec54.jpg",
"https://telegra.ph/file/03aa11fdd46f96c410f5d.jpg",
"https://telegra.ph/file/70deaa6256cd9d6d86e89.jpg",
"https://telegra.ph/file/b19d6daa4a616f788f45d.jpg",
"https://telegra.ph/file/0cfcc2206616995bada81.jpg",
"https://telegra.ph/file/0cfcc2206616995bada81.jpg",
"https://telegra.ph/file/65a290bf8e6df370762a8.jpg",
"https://telegra.ph/file/78951fe3c499cc7433961.jpg",
"https://telegra.ph/file/889781c7d2fb5bd1d3f2c.jpg",
"https://telegra.ph/file/ad59bcf4bc0840909ce0c.jpg",
"https://telegra.ph/file/8a2366094ee43e18c873b.jpg",
"https://telegra.ph/file/97d00a1bea9094b9cd0c6.jpg",
"https://telegra.ph/file/df1408d0293d55ddc867b.jpg",
"https://telegra.ph/file/86a3020627709ee3b79b8.jpg",
"https://telegra.ph/file/dc01b73c7b8c5b84c0ceb.jpg",
"https://telegra.ph/file/ff705236e826b044ebf17.jpg",
"https://telegra.ph/file/6be0b213071b3c8232525.jpg",
"https://telegra.ph/file/4ea9cd132700b24df7df9.jpg",
"https://telegra.ph/file/f5af27cf39ef6888bac9a.jpg",
"https://telegra.ph/file/cee6e5040b29e559021f4.jpg",
"https://telegra.ph/file/6d1da2075369a8ad02063.jpg",
"https://telegra.ph/file/4ea9cd132700b24df7df9.jpg",
"https://telegra.ph/file/9562c20ed72ca5e77113b.jpg",
"https://telegra.ph/file/67ffced03b627745e3221.jpg",
"https://telegra.ph/file/79777e181dd362fd70051.jpg",
"https://telegra.ph/file/142507a822c77174d9957.jpg",
"https://telegra.ph/file/758ffea16a5be46650e57.jpg",
"https://telegra.ph/file/758ffea16a5be46650e57.jpg",
"https://telegra.ph/file/e80f5811ab497a3fff473.jpg",
"https://telegra.ph/file/54eb04bccbf483578ed4a.jpg",
"https://telegra.ph/file/1e6303accd0feb59a5ca3.jpg",
"https://telegra.ph/file/cb7fd1ce2207407866757.jpg",
"https://telegra.ph/file/0a84616f2b6bbacb8a6f2.jpg",
"https://telegra.ph/file/a86095e5561a50cd8b9b5.jpg",
"https://telegra.ph/file/52185c19c2204d0dbd356.jpg",
"https://telegra.ph/file/f3c64f1b7ef9a6dc6bfac.jpg",
"https://telegra.ph/file/57ea2a5e74d9b04476608.jpg",
"https://telegra.ph/telethon-04-24-3",
]

@telethon_client.on(events.NewMessage(pattern='^\.anime'))
async def anime(event): 
    if str(event.sender_id) in owner_id:
        if AMINE:  
            file = choice(AMINE) 
            await event.reply(file=file)
        else:
            await event.reply("AMINE listesi boş. Lütfen uygun resim URL'lerini ekleyin.")
    else:
        await event.reply("")

@telethon_client.on(events.NewMessage(pattern='^\.got'))
async def got(event): 
    if str(event.sender_id) in owner_id:
        if GOT:  
            file = choice(GOT) 
            await event.reply(file=file)
        else:
            await event.reply("GOT listesi boş. Lütfen uygun resim URL'lerini ekleyin.")
    else:
        await event.reply("")

async def main():
    await telethon_client.start(phone_number)
    print("Telethon giriş başarılı.")

    
    await telethon_client.run_until_disconnected()

@telethon_client.on(events.NewMessage(pattern="^\.aptallik"))
async def rand(event): 
    APTALLİK = ['%40','%83','%100','%93','%10','%20','%31','%50']

    await event.edit("`Aptallığın 100'de Kaç Olduğu Hesaplanıyor...`") 
    donus = random.randint(20,50)
    sayi = 0
    await asyncio.sleep(0.6)
    for i in range(0, donus):
        await asyncio.sleep(0.1)
        sayi = random.randint(1, 8)
        try:
            await event.edit("`Aptallığın Kaç Olduğunu Öğrenmeye Hazır Mısın...?`")
        except:
            continue

    await asyncio.sleep(0.1)
    await event.edit("**Aptallığın Kaç Olduğu Hesaplandı** :"+APTALLİK[sayi-1]+" **Aptallığının Kaç Olduğunu Öğrendin.(**")
 
@telethon_client.on(events.NewMessage(pattern="^[Ss][Ee][Nn][İi] [Ss][Ee][Vv][İi][Yy][Oo][Rr][Uu][Mm]$", outgoing=True))
async def benimol(event):
  
     await event.edit("**S😊**")
     time.sleep(0.30)
     
     await event.edit("**Se😘**")
     time.sleep(0.30)
     
     await event.edit("**Sen🤗**")
     time.sleep(0.30)
     
     await event.edit("**Seni🔥**")
     time.sleep(0.41)
     
     await event.edit("**Seviyorum👻**")
     time.sleep(0.41)
     
     await event.edit("**ㅤㅤ ㅤ**")
     time.sleep(0.41)
     
     await event.edit("**Seni Seviyorum☘️😇**")
     time.sleep(0.41)
     
     await event.edit("**ㅤㅤ ㅤ**")
     time.sleep(0.41)
     
     await event.edit("**Seni Seviyorum💀**")
     time.sleep(0.30)
     
     await event.edit("**ㅤ ㅤㅤ**")
     time.sleep(0.30)
     
     await event.edit("**Seni Seviyorum💝**")
     time.sleep(0.30)
     
     await event.edit("**Seni Seviyorum💥**")
     time.sleep(0.30)
     
     await event.edit("**SEni‼️**")
     time.sleep(0.30)
     
     await event.edit("**SENi⭕**")
     time.sleep(0.30)
     
     await event.edit("**SENİ☠️**")
     time.sleep(0.30)
     
     await event.edit("**SEVİYORUM💯**")
     time.sleep(0.30)
     
     await event.edit("**S**")
     time.sleep(0.30)
     
     await event.edit("**ㅤE**")
     time.sleep(0.30)
     
     await event.edit("**ㅤㅤN**")
     time.sleep(0.30)
     
     await event.edit("**ㅤㅤㅤİ**")
     time.sleep(0.30)
     
     await event.edit("**ㅤㅤㅤㅤS**")
     time.sleep(0.30)
     await event.edit("**                 E**")
     time.sleep(0.30)
     
     await event.edit("**ㅤ                 V**")
     time.sleep(0.30)
     
     await event.edit("**ㅤㅤ                İ**")
     time.sleep(0.30)
     
     await event.edit("**ㅤㅤㅤ              YO**")
     time.sleep(0.30)
     
     await event.edit("**ㅤㅤㅤㅤ              RUM**")
     time.sleep(0.30)
     
     await event.edit("**💝S E N İ  S E V İ Y O R U M💝**")
     time.sleep(0.30)      
     
@telethon_client.on(events.NewMessage(pattern="^\.ym"))
async def rand(event): 
    YALANMAKİNE = ['Doğru','Yalan','Doğru','Yalan','Doğru','Yalan','Doğru','Yalan']

    await event.edit("`Doğru Mu Yoksa Yalan Mı Söylediği Kontrol Ediliyor...`") 
    donus = random.randint(20,50)
    sayi = 0
    await asyncio.sleep(0.6)
    for i in range(0, donus):
        await asyncio.sleep(0.1)
        sayi = random.randint(1, 8)
        try:
            await event.edit("`Sonucu Öğrenmeye Hazır Mısın...?`")
        except:
            continue

    await asyncio.sleep(0.1)
    await event.edit("**Doğru Veya Yalan Söylediği Açıklandı Kullanıcı**: `"+YALANMAKİNE[sayi-1]+"` **Söylüyor.**")  
   
                                                                      
@telethon_client.on(events.NewMessage)
async def handle_message(event):
    global bot_calisiyor
    if event.text == ".baslat" and not bot_calisiyor:
        if str(event.sender_id) == owner_id:
            bot_calisiyor = True
            await event.respond("Bot başlatılıyor...")
            return
        else:
            await event.respond("")
            return
    elif event.text == ".durdur" and bot_calisiyor:
        if str(event.sender_id) == owner_id:
            bot_calisiyor = False
            await event.respond("Bot durduruluyor...")
            return

@telethon_client.on(events.NewMessage(pattern="^\.all(?: |$)(.*)"))
async def tag_all(event):
    global bot_calisiyor

    if bot_calisiyor:
        if event.fwd_from:
            return
            
    if str(event.sender_id) == owner_id:
        if event.pattern_match.group(1):
            seasons = event.pattern_match.group(1)
        else:
            seasons = ""

        chat = await event.get_input_chat()
        a_ = 0
        async for i in telethon_client.iter_participants(chat):
            if not bot_calisiyor:
                break
            if a_ == 5000:
                break
            a_ += 1
            try:
                await event.respond("[{}](tg://user?id={}) {}".format(i.first_name, i.id, seasons))
                time.sleep(4)
            except Exception as e:
                print("Hata:", e)
    else:
        await event.respond("")


async def telethon_main():
    await telethon_client.connect()

    if not await telethon_client.is_user_authorized():
        await telethon_client.send_code_request(telethon_telefon_numarasi)
        code = input("Doğrulama kodunu girin: ")

        try:
            await telethon_client.sign_in(telethon_telefon_numarasi, code)
        except Exception as e:
            print(f"Giriş sırasında hata oluştu: {e}")
            return

    print(f'\033[2;35mBot başarılı Bir şekilde giriş yaptı')

    
    await telethon_client.run_until_disconnected()

@telethon_client.on(events.NewMessage(pattern="^\.menu(?: |$)"))
async def show_menu(event):
    menu_text = """
╭──❰ 🎭 𝙆𝙊𝙈𝙐𝙏 𝙈𝙀𝙍𝙆𝙀𝙕𝙄 🎭 ❱───➤  
│  
├ 🎯 **Genel Komutlar**  
│   ├ 💫 `.baslat` - Etiketlemeyi başlat  
│   ├ 🛑 `.durdur` - Etiketlemeyi durdur  
│   ├ ⚡ `.sex` - Sex animasyonu  
│   ├ ⚜️ `.all` - Tüm kullanıcıları etiketle  
│   ├ 👁 `.gn` - Günaydın mesajı  
│   ├ ✨ `.ig` - İyi geceler mesajı  
│   ├ 👑 `.ym` - Yalan makinesi  
│   ├ 🎯 `.aptallik` - Aptallık testi  
│   ├ ⚡ `.azekfr` - Azerbaycanca küfür  
│   ├ 🌟 `.otuzbir` - 31 çekme komutu  
│   ├ 📡 `.cm` - Y#rr#k cm ölçme komutu  
│   ├ 🌌 `.anime` - Rasgele anime fotoları  
│   ├ 💫 `.got` - Rasgele karı fotoları  
│   ├ ⚜️ `naber` - Nokta olmadan naber  
│   ├ 🛑 `.pm` - On/Off - PM permit açma veya kapama  
│   ├ 💫 `.edit` - PM permit mesajını editler  
│   ├ ⚡ `.approve` - Kullanıcı onayı verir  
│   ├ 👑 `.disapprove` - Kullanıcı onayını kaldırır  
│   ├ 🌟 `seni seviyorum` - Nokta olmadan seni seviyorum  
│   ├ ⚡ `.ip` - IP sorgulama  
│  
├ 🎭 **Filtreleme & Komutlar**  
│   ├ `.filter` - Chat veya DM mesajları için filtre  
│   ├ `.stop` - Ayarladığınız filtreyi siler  
│   ├ `.filters` - Ayarladığınız filtreleri gösterir  
│   ├ `.genelfilter` - Tüm yerler için filtre ayarlar  
│   ├ `.genelstop` - Genel filtreyi siler  
│   ├ `.genelfilters` - Genel filtreleri gösterir  
│  
├ 🤖 **Eğlence Komutları**  
│   ├ 🌌 `.soztag` - Rasgele sorularla etiket atar  
│   ├ 💫 `.kfrtag` - Rasgele küfürlü etiket atar  
│   ├ ⚜️ `.yavsa` - Sevdiğinize yavşayın  
│   ├ 🌟 `.erm` - Ermenistan bayrağına boşalır  
│   ├ 📡 `.evlenme` - Evlenme oranını gösterir  
│   ├ 💫 `.kedicik` - Eğlence modu başlatır  
│   ├ ⚡ `.opucuk` - Öpücük gönderir  
│   ├ 🌟 `.yarrak` - 35cm yarrak atar  
│   ├ ⚜️ `.ook` - Ok diye mesaj gönderir  
│   ├ 💫 `.kfr` - Rasgele küfürler atar  
│   ├ ⚡ `.sa` - Selam mesajı atar  
│   ├ ⭐ `.ters` - metini terse çevirir  
│   ├
├ 🌍 **Bilgi & Araçlar**  
│   ├ 🌌 `.kurulum` - Hesap kurulum tarihi  
│   ├ ⚜️ `.aç` - Dosyadaki kodu atar  
│   ├ 💫 `.ttf` - Metni dosyaya dönüştürür  
│   ├ 📡 `.cevir` - Metin çevirisi yapar  
│   ├ 🌟 `.as` - Aleyküm selam mesajı atar  
│   ├ ⚡ `.kurt` - Kürtlük seviyesini ölçer  
│   ├ 🌌 `.aptallik` - Kişinin aptallık seviyesini gösterir  
│   ├ 🎯 `napim` - Napim mesajı atar  
│   ├ ⚜️ `Tamam` - Tamam mesajı atar  
│   ├ 🌟 `hosgeldin` - Hoşgeldin mesajı atar  
│   ├ 💫 `.beyin` - Beyinle ilgili test yapar  
│   ├ ⚡ `.hayal` - Hayal ettiğiniz şeyi yazar  
│   ├ 🌌 `.ölüm` - Ölüm yaşını söyler  
│   ├ ⚜️ `.hack` - Troll amaçlı hack komutu  
│   ├ 🌟 `.iqtest` - Kişinin IQ seviyesini ölçer  
│   ├ 💫 `.gay` - Kişinin gaylik oranını söyler  
│   ├ ⚡ `.tavlama` - Instagram profilini alır  
│   ├ 💫 `.id` - Kullanıcı id alır
│   ├ ✨ `.ses` - metini sese çevirir
│   ├ 💛 `.mat` - matematiksel soruları çözer
│   ├
├ 🫣 ** Ekstra komutlar**
│   ├ 🌞 `gizli` - iletisi kapalı olan gizli kanaldan içerik çeker 
│   ├ 🌝 `acik` - public yani bağlantısı açık olup iletisi kapalı olan
│   ├ 🤤 `süreli fotoğrafı veya videoyu kayıtlı mesajlara atar komutu yok`
│  
╰───❰ 👾 @BotAltyapiKanali ❱──➤  
"""

    await event.edit(menu_text)
    
        
    
if __name__ == "__main__":
    telethon_client.loop.run_until_complete(telethon_main())
