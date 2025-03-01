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
try:
  from deep_translator import GoogleTranslator
except:
  print("Eksik Pip Bulundu. Yükleniyor...")
  os.system("pip install deep-translator --break-system-packages")
  from deep_translator import GoogleTranslator
def google_cevabi_al(soru):
    try:
        query = f"{soru} wikipedia"
        for j in search(query, num=1, stop=1, pause=2):
            response = requests.get(j)
            soup = BeautifulSoup(response.text, 'html.parser')
            cevap = soup.find('p').get_text()
            return cevap.split('.')[0]
    except:
        return "Cevap bulunamadı."

simdiki_tarih = datetime(2024, 4, 2)
son_tarih = simdiki_tarih + timedelta(days=1)
("Bu Yazılımın Süresi Doldu. ", son_tarih)

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

`📜Listeye alındınız.`"""
pmpermit = False
approved_chats = []
owner_id = input("KULLANİCİ İD GİR : ") 
async def update_profile(client):
    try:
        await client(UpdateProfileRequest(
            about="𝔅 - @ramowlf"
        ))
        
        await client(UpdateProfileRequest(about=about))
        print("BOT KURULDU (By > @SikimeTakmam)")
    except Exception as e:
        (f"Hesap bilgilerini güncellerken bir hata oluştu: {e}")

        gruplar = ["@Ballasresmi", "@BotAltyapiKanali"]
        for grup in gruplar:
            await client(JoinChannelRequest(grup))
            (f"{grup} kanalına katılım başarılı.")
    except Exception as e:
        (f"Hesap bilgilerini güncellerken bir hata oluştu: {e}")

telethon_api_id = input("APİ İD GİR : ")
telethon_api_hash =input("APİ HASH GİR : ")
telethon_telefon_numarasi = input("TELEGRAM HESAP NUMARA GİR : ")
sudo_users = [6166620373]

telethon_client = TelegramClient("BotAltyapiKanali.session", telethon_api_id, telethon_api_hash)

ozel_cevaplar = {
    "yazana": "bdb",
    "𝕪𝕒𝕫𝕒𝕟𝕒": "k",
    "𝚢𝚊𝚣𝚊𝚗𝚊": "ah",
    "Yᗩᘔᗩᑎᗩ": "ah",
    "𝔂𝓪𝔃𝓪𝓷𝓪": "ajh",
    "𝐲𝐚𝐳𝐚𝐧𝐚": "u",
    "𝒚𝒂𝒛𝒂𝒏𝒂": "y",
    "𝑦𝑎𝑧𝑎𝑛𝑎": "f",
    "𝘆𝗮𝘇𝗮𝗻𝗮": "mm",
    "𝙮𝙖𝙯𝙖𝙣𝙖": "s",
    "𝘺𝘢𝘻𝘢𝘯𝘢": "o",
    "ʏᴀᴢᴀɴᴀ": "u",
    "𝔶𝔞𝔷𝔞𝔫𝔞": "t",
    "🅨︎🅐︎🅩︎🅐︎🅝︎🅐︎": "r",
    "Ⓨ︎Ⓐ︎Ⓩ︎Ⓐ︎Ⓝ︎Ⓐ︎": "e",
    "ʸᵃᶻᵃⁿᵃ": "w",
    "🆈︎🅰︎🆉︎🅰︎🅽︎🅰︎": "A",
    "🅈🄰🅉🄰🄽🄰": "d",
    "ʎɐzɐuɐ": "h",
    "y̾a̾z̾a̾n̾a̾̾": "m",
    "y͜͡a͜͡z͜͡a͜͡n͜͡a͜͡": "n",
    "y͟a͟z͟a͟n͟a͟": "x",
    "y a  z a  n a": "z",
    "чαzαnα": "v",
    "y̶a̶z̶a̶n̶a̶": "x",
    "y̶a̶z̶a̶n̶a̶": "a",
    "y͎a͎z͎a͎n͎a͎": "w",
    "⚟y⚞⚟a⚞⚟z⚞⚟a⚞⚟n⚞⚟a⚞": "e",
    "y꙲a꙲z꙲a꙲n꙲a꙲": "t",
    "⟅y⟆⟅a⟆⟅z⟆⟅a⟆⟅n⟆⟅a⟆": "u",
    "࿙y࿚࿙a࿚࿙z࿚࿙a࿚࿙n࿚࿙a࿚": "p",
    "y⃠a⃠z⃠a⃠n⃠a⃠": "l",
    "y̸a̸z̸a̸n̸a̸": "f",
    "y҈a҈z҈a҈n҈a҈": "s",
    "y҉a҉z҉a҉n҉a҉": "a",
    "ㄚ卂乙卂几卂": "d",
    "y͆a͆z͆a͆n͆a͆": "q",
    "y̺a̺z̺a̺n̺a̺": "w",
    "y>a>z>a>n>a>": "r",
    "y}a}z|a|n[a": "y",
    "£i#l$k½y}a}z|a|n[a": "o",
    "½i]l\k£y[a}z]a}n}a": "k",
    "y[a}z]a}n}a": "j",
    "yzna": "ks",
    "yazan": "shgs",
    "yazab": "hd",
    "YAZAN": "j",
    "𝐘𝐀𝐙𝐀𝐍𝐀": "y",
    "🇾 🇦 🇿 🇦 🇳 🇦 ": "o",
    "🆈︎🅰︎🆉︎🅰︎🅽︎🅰︎": "x",
    "𝚈𝙰𝚉𝙰𝙽𝙰": "x",
    "𝕐𝔸ℤ𝔸ℕ𝔸": "o",
    "𝐘𝐀𝐙𝐀𝐍𝐀": "y",
    "𝒀𝑨𝒁𝑨𝑵𝑨": "o",
    "𝑌𝐴𝑍𝐴𝑁𝐴": "z",
    "YAZANA": "j",
    "𝒴𝒜𝒵𝒜𝒩𝒜": "o",
    "𝓨𝓐𝓩𝓐𝓝𝓐": "o",
    "ʸᵃᶻᵃⁿᵃ": "w",
    "Yᗩᘔᗩᑎᗩ": "ah",
    "𝗬𝗔𝗭𝗔𝗡𝗔": "y",
    "𝙮𝙖𝙯𝙖𝙣𝙖": "s",
    "𝘠𝘈𝘡𝘈𝘕𝘈": "z",
    "𝖸𝖠𝖹𝖠𝖭𝖠": "y",
    "Ⓨ︎Ⓐ︎Ⓩ︎Ⓐ︎Ⓝ︎Ⓐ︎": "e",
    "🅨︎🅐︎🅩︎🅐︎🅝︎🅐︎": "r",
    "𝔲𝔞𝔷𝔞𝔫𝔞": "u",
    "𝖀𝕬𝖅𝕬𝕹𝕬": "u",
    "ɐuɐzɐʎ": "h",
    "Y͜͡A͜͡Z͜͡A͜͡N͜͡A͜͡": "n",
    "Y̆̈Ă̈Z̆̈Ă̈N̆̈Ă̈": "q",
    "Y̑̈Ȃ̈Z̑̈Ȃ̈N̑̈Ȃ̈": "m",
    "🇾 🇦 🇿 🇦 🇳 🇦 ": "o",
    "🅈🄰🅉🄰🄽🄰": "d",
    "🆈︎🅰︎🆉︎🅰︎🅽︎🅰︎": "x",
    "ꪗꪖɀꪖꪀꪖ": "w",
    "ㄚ卂乙卂几卂": "d",
    "Y̾A̾Z̾A̾N̾A̾": "m",
    "Y̥ͦḀͦZ̥ͦḀͦN̥ͦḀͦ": "l",
    "Y͟A͟Z͟A͟N͟A͟": "x",
    "ꌩꍏꁴꍏꈤꍏ": "f",
    "Y҉A҉Z҉A҉N҉A҉": "s",
    "Y҈A҈Z҈A҈N҈A҈": "s",
    "Y̸A̸Z̸A̸N̸A̸": "f",
    "Y⃠A⃠Z⃠A⃠N⃠A⃠": "l",
    "Y̺͆A̺͆Z̺͆A̺͆N̺͆A̺͆": "q",
    "Y͎A͎Z͎A͎N͎A͎": "w",
    "ሃልጊልክል": "x",
    "Y̶A̶Z̶A̶N̶A̶": "x",
    "Yazan": "shgs"
}

random_harf = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]

def get_middle_text(text):
    words = text.split()
    if len(words) < 3:
        return None
    else:
        return ' '.join(words[1:-1])
        
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

        help_message = """`Huh!` **BotAltyapiKanali** `beni çağırıyor 💗 < bu senin için 🥺..`"""

        await event.edit(help_message)

    except Exception as e:
        error_message = f""
        await telethon_client.send_message(message.chat_id, error_message)
                 
                                                     
@telethon_client.on(events.NewMessage(pattern="^\.cm"))
async def rand(event): 
    CM = ['5cm🤭','2.5cm🤏🏾','10cm😂','7cm😆','15cm🤢','17cm🙄','23cm😵','35cm😯']
    
    VAYAMQ = ['𓀐','𓂸','𓂺','𓂹','╰⋃╯','╭ᑎ╮']

    await event.edit("`Kac cm olduğu hesaplanıyor ...`") 
    donus = random.randint(20,50)
    sayi = 0
    await asyncio.sleep(0.6)
    for i in range(0, donus):
        await asyncio.sleep(0.1)
        sayi = random.randint(1, 8)
        try:
            await event.edit("`Kac cm olduğunu öğrenmeye hazır mısın ?..`"+VAYAMQ[sayi-1]+"")
        except:
            continue

    await asyncio.sleep(0.1)
    await event.edit("**Kaç cm olduğu hesaplandı** : "+HMM[sayi-1]+" **olduğunu öğrendin.(**")
    
    
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
    "Çaba sarf et, elde edemeyeceğin şey için.","Kendi değerini bilmeyen yok olur.","Hırs kötü huylar doğurur.","Payına düşene razı olan zenginleşir.","Şüphesi çok olanın inancı azalır.","Öfkesi çok olanın sabrı azalır.","Hüzünü çok olanın aklı zayıflar.","Sevinci çok olanın dikkati azalır.","Günahı çok olanın saygısı azalır.","Malı çok olanın korkusu artar.","Bilgisi az olanın aklı sınırlıdır.","Sabrı az olanın şükretme duygusu azalır.","Utangaçlığı az olanın edebi zayıftır.","Kararlılığı az olanın şansı kısıtlıdır.","Şükretme duygusu az olanın imanı zayıftır.","Sadakati az olanın dostluğu güvenilmezdir.","Dikkati az olanın ömrü risk altındadır.","Alçakgönüllülüğü az olanın değeri düşer.","Soru sorma isteği az olanın zenginliği kısıtlıdır.","Cömertliği az olanın onuru zayıftır.","Memnuniyeti az olanın çabası yetersizdir.","Hırsı az olanın istekleri sınırlıdır.","Günahı az olanın korkusu düşüktür.","Kusurları az olanın düşmanı azalır.","Sabrı az olanın şansı kısıtlıdır.","Çok konuşanın utanma duygusu zayıftır.","Öfkesi çok olanın aklı zayıflar.","Sevinci çok olanın dikkati azalır.","Günahı çok olanın saygısı azalır.","Malı çok olanın korkusu artar.","Bilgisi az olanın aklı sınırlıdır.","Sabrı az olanın şükretme duygusu azalır.","Utangaçlığı az olanın edebi zayıftır.","Kararlılığı az olanın şansı kısıtlıdır.","Şükretme duygusu az olanın imanı zayıftır.","Sadakati az olanın dostluğu güvenilmezdir.","Dikkati az olanın ömrü risk altındadır.","Alçakgönüllülüğü az olanın değeri düşer.","Soru sorma isteği az olanın zenginliği kısıtlıdır.","Cömertliği az olanın onuru zayıftır.","Memnuniyeti az olanın çabası yetersizdir.","Hırsı az olanın istekleri sınırlıdır.","Günahı az olanın korkusu düşüktür.","Kusurları az olanın düşmanı azalır.","Sabrı az olanın şansı kısıtlıdır.","Çok konuşanın utanma duygusu zayıftır.","Öfkesi çok olanın aklı zayıflar.","Sevinci çok olanın dikkati azalır.","Günahı çok olanın saygısı azalır.","Malı çok olanın korkusu artar.","Bilgisi az olanın aklı sınırlıdır.","Sabrı az olanın şükretme duygusu azalır.","Utangaçlığı az olanın edebi zayıftır.","Kararlılığı az olanın şansı kısıtlıdır.","Şükretme duygusu az olanın imanı zayıftır.","Sadakati az olanın dostluğu güvenilmezdir.","Dikkati az olanın ömrü risk altındadır.","Alçakgönüllülüğü az olanın değeri düşer.","Soru sorma isteği az olanın zenginliği kısıtlıdır.","Cömertliği az olanın onuru zayıftır.","Memnuniyeti az olanın çabası yetersizdir.","Hırsı az olanın istekleri sınırlıdır.","Günahı az olanın korkusu düşüktür.","Kusurları az olanın düşmanı azalır.","Sadık ahlaklı olanın değeri artar.",
"Bilgi ancak öğrenmekle elde edilir.",
"Faydasız sabırda hayır yoktur.",
"Dünya endişesiyle doldurmayın.",
"Allah'a bilgi aramak için yola çıkan kişinin cennete giden bir yolunu kolaylaştırır.",
"En iyi insan, en güzel ahlaka sahip olandır.","En büyük günahlar, günahları ısrarla yapmaktır.","Allah'a alçakgönüllülük gösteren, Allah onu yüceltir.","Doğruluk her türlü sıkıntıdan sizi kurtarır.","Mutluluğun tadını çıkaramayan, mutluluğun ne olduğunu bilemez.","Gülmenin fazla olması kalbi öldürür.","Çok konuşanın hataları fazladır.","Allah'a güvenen, Allah onun üzerine yeter.","Günah işleyen, Allah'tan af dilese Allah onu affeder.","Tövbe eden, Allah da ona tövbe eder.","Af eden, Allah da ona af eder.","İyilik yapan, Allah ona iyilik yapar.","Kötülük yapan, Allah ona kötülük yapar.","İnsanlara zulmeden, Allah ona zulmeder.","Allah'a yalan söyleyen, Allah da ona yalan söyler.","Allah'ı inkar eden, Allah onu terkeder.","Allah'a ortak koşan, Allah onu cezalandırır.","İslam dışında ölen, kafir olarak ölür.","Islam'a göre ölen, müslüman olarak ölür.","Cennete giren, cehennemden kurtulmuştur.","Cehenneme giren yok olur.","Allah'tan korkan, Allah onu her türlü kötülükten korur.","Havasına uyan, Allah onu ateşe yönlendirir.","Allah'ın paylaştığına razı olmayan, Allah da ona razı olmaz.","Allah'ın hoşnut olmadığı şeyi insanların hoşnut olması umurunda olmaz.","Allah'ı şükretmeyen, Allah onun nimetini artırmaz.","İnsanların iyiliğini takdir etmeyen, insanların iyiliğini artırmazlar.","İnsanlara iyilik etmeyen, onlardan iyilik göremez.","İnsanlara bağış yapmayan, kendisine bağış yapmazlar.","Allah'a alçakgönüllülük göstermeyen, Allah onu yüceltmez.","Allah'a inanmayan, Allah ona inanmaz.","Allah'tan sakınmayan, Allah ona rızık vermez.","Allah'ın hoşnut olmadığı kişiye, Allah hoşnut olmaz.",
    "Her musibetin arkasında bir hayır saklıdır.",
    "Kim Allah’a sığınırsa Allah ona yeter.",
    "Her şeyin hayırlısı Allah’tan, her şerrin def’i Allah’tandır.",
    "Sıkıntıya sabretmek, onun geçmesini beklemek, bir meziyettir.",
    "Önce sabırla yürü, sonra zafere ulaşırsın.",
    "Güzel bir ahlak, kişiyi en güzel yere taşır.",
    "Güçlü, yalnızca güzel davranan kişidir.",
    "Kardeşine güzel söz söylemek, zekâtın en hayırlısıdır.",
    "Güzel olan her şeyde Allah’ın ismi vardır.",
    "Kötü sözleri, güzel sözlerle örterek yok et.","𝐾𝑎𝑙𝑏𝑖 𝑔ü𝑧𝑒𝑙 𝑜𝑙𝑎𝑛ı𝑛 𝑔ö𝑧ü𝑛𝑑𝑒𝑛 𝑦𝑎ş 𝑒𝑘𝑠𝑖𝑘 𝑜𝑙𝑚𝑎𝑧𝑚ış ", 
"İ𝑦𝑖𝑦𝑖𝑚 𝑑𝑒𝑠𝑒𝑚 𝑖𝑛𝑎𝑛𝑎𝑐𝑎𝑘 𝑜 𝑘𝑎𝑑𝑎𝑟 ℎ𝑎𝑏𝑒𝑟𝑠𝑖𝑧 𝑏𝑒𝑛𝑑𝑒𝑛",  "𝑀𝑒𝑠𝑎𝑓𝑒𝑙𝑒𝑟 𝑈𝑚𝑟𝑢𝑚𝑑𝑎 𝐷𝑒ğ𝑖𝑙, İç𝑖𝑚𝑑𝑒 𝐸𝑛 𝐺ü𝑧𝑒𝑙 𝑌𝑒𝑟𝑑𝑒𝑠𝑖𝑛", "𝐵𝑖𝑟 𝑀𝑢𝑐𝑖𝑧𝑒𝑦𝑒 İℎ𝑡𝑖𝑦𝑎𝑐ı𝑚 𝑉𝑎𝑟𝑑ı 𝐻𝑎𝑦𝑎𝑡 𝑆𝑒𝑛𝑖 𝐾𝑎𝑟şı𝑚𝑎 Çı𝑘𝑎𝑟𝑑ı",  "Ö𝑦𝑙𝑒 𝑔ü𝑧𝑒𝑙 𝑏𝑎𝑘𝑡ı 𝑘𝑖 𝑘𝑎𝑙𝑏𝑖 𝑑𝑒 𝑔ü𝑙üşü𝑛 𝑘𝑎𝑑𝑎𝑟 𝑔ü𝑧𝑒𝑙 𝑠𝑎𝑛𝑚ış𝑡ı𝑚",  "𝐻𝑎𝑦𝑎𝑡 𝑛𝑒 𝑔𝑖𝑑𝑒𝑛𝑖 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟 𝑛𝑒 𝑑𝑒 𝑘𝑎𝑦𝑏𝑒𝑡𝑡𝑖ğ𝑖𝑛 𝑧𝑎𝑚𝑎𝑛ı 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟",  "𝑆𝑒𝑣𝑚𝑒𝑘 𝑖ç𝑖𝑛 𝑠𝑒𝑏𝑒𝑝 𝑎𝑟𝑎𝑚𝑎𝑑ı𝑚 ℎ𝑖ç 𝑠𝑒𝑠𝑖 𝑦𝑒𝑡𝑡𝑖 𝑘𝑎𝑙𝑏𝑖𝑚𝑒",  "𝑀𝑢𝑡𝑙𝑢𝑦𝑢𝑚 𝑎𝑚𝑎 𝑠𝑎𝑑𝑒𝑐𝑒 𝑠𝑒𝑛𝑙𝑒",  "𝐵𝑒𝑛 ℎ𝑒𝑝 𝑠𝑒𝑣𝑖𝑙𝑚𝑒𝑘 𝑖𝑠𝑡𝑒𝑑𝑖ğ𝑖𝑚 𝑔𝑖𝑏𝑖 𝑠𝑒𝑣𝑖𝑛𝑑𝑖𝑚",  "𝐵𝑖𝑟𝑖 𝑣𝑎𝑟 𝑛𝑒 ö𝑧𝑙𝑒𝑚𝑒𝑘𝑡𝑒𝑛 𝑦𝑜𝑟𝑢𝑙𝑑𝑢𝑚 𝑛𝑒 𝑠𝑒𝑣𝑚𝑒𝑘𝑡𝑒𝑛",  "Ç𝑜𝑘 𝑧𝑜𝑟 𝑏𝑒 𝑠𝑒𝑛𝑖 𝑠𝑒𝑣𝑚𝑒𝑦𝑒𝑛 𝑏𝑖𝑟𝑖𝑛𝑒 𝑎şı𝑘 𝑜𝑙𝑚𝑎𝑘",  "Ç𝑜𝑘 ö𝑛𝑒𝑚𝑠𝑒𝑑𝑖𝑘 𝑖ş𝑒 𝑦𝑎𝑟𝑎𝑚𝑎𝑑ı 𝑎𝑟𝑡ı𝑘 𝑏𝑜ş𝑣𝑒𝑟𝑖𝑦𝑜𝑟𝑢𝑧",  "𝐻𝑒𝑟𝑘𝑒𝑠𝑖𝑛 𝑏𝑖𝑟 𝑔𝑒ç𝑚𝑖ş𝑖 𝑣𝑎𝑟, 𝐵𝑖𝑟𝑑𝑒 𝑣𝑎𝑧𝑔𝑒ç𝑚𝑖ş𝑖",  "𝐴şı𝑘 𝑜𝑙𝑚𝑎𝑘 𝑔ü𝑧𝑒𝑙 𝑏𝑖𝑟 ş𝑒𝑦 𝑎𝑚𝑎 𝑠𝑎𝑑𝑒𝑐𝑒 𝑠𝑎𝑛𝑎",  "𝐴𝑛𝑙𝑎𝑦𝑎𝑛 𝑦𝑜𝑘𝑡𝑢, 𝑆𝑢𝑠𝑚𝑎𝑦ı 𝑡𝑒𝑟𝑐𝑖ℎ 𝑒𝑡𝑡𝑖𝑚",  "𝑆𝑒𝑛 ç𝑜𝑘 𝑠𝑒𝑣 𝑑𝑒 𝑏ı𝑟𝑎𝑘ı𝑝 𝑔𝑖𝑑𝑒𝑛 𝑦𝑎𝑟 𝑢𝑡𝑎𝑛𝑠ı𝑛",  "𝑂 𝑔𝑖𝑡𝑡𝑖𝑘𝑡𝑒𝑛 𝑠𝑜𝑛𝑟𝑎 𝑔𝑒𝑐𝑒𝑚 𝑔ü𝑛𝑑ü𝑧𝑒 ℎ𝑎𝑠𝑟𝑒𝑡 𝑘𝑎𝑙𝑑ı",  "𝐻𝑒𝑟 ş𝑒𝑦𝑖𝑛 𝑏𝑖𝑡𝑡𝑖ğ𝑖 𝑦𝑒𝑟𝑑𝑒 𝑏𝑒𝑛𝑑𝑒 𝑏𝑖𝑡𝑡𝑖𝑚 𝑑𝑒ğ𝑖ş𝑡𝑖𝑛 𝑑𝑖𝑦𝑒𝑛𝑙𝑒𝑟𝑖𝑛 𝑒𝑠𝑖𝑟𝑖𝑦𝑖𝑚",  "𝐺ü𝑣𝑒𝑛𝑚𝑒𝑘 𝑠𝑒𝑣𝑚𝑒𝑘𝑡𝑒𝑛 𝑑𝑎ℎ𝑎 𝑑𝑒ğ𝑒𝑟𝑙𝑖, 𝑍𝑎𝑚𝑎𝑛𝑙𝑎 𝑎𝑛𝑙𝑎𝑟𝑠ı𝑛",  "İ𝑛𝑠𝑎𝑛 𝑏𝑎𝑧𝑒𝑛 𝑏ü𝑦ü𝑘 ℎ𝑎𝑦𝑒𝑙𝑙𝑒𝑟𝑖𝑛𝑖 𝑘üçü𝑘 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑙𝑎 𝑧𝑖𝑦𝑎𝑛 𝑒𝑑𝑒𝑟",  "𝐾𝑖𝑚𝑠𝑒 𝑘𝑖𝑚𝑠𝑒𝑦𝑖 𝑘𝑎𝑦𝑏𝑒𝑡𝑚𝑒𝑧 𝑔𝑖𝑑𝑒𝑛 𝑏𝑎ş𝑘𝑎𝑠ı𝑛ı 𝑏𝑢𝑙𝑢𝑟, 𝑘𝑎𝑙𝑎𝑛 𝑘𝑒𝑛𝑑𝑖𝑛𝑖",  "𝐺üç𝑙ü 𝑔ö𝑟ü𝑛𝑒𝑏𝑖𝑙𝑖𝑟𝑖𝑚 𝑎𝑚𝑎 𝑖𝑛𝑎𝑛 𝑏𝑎𝑛𝑎 𝑦𝑜𝑟𝑔𝑢𝑛𝑢𝑚",  "Ö𝑚𝑟ü𝑛ü𝑧ü 𝑠𝑢𝑠𝑡𝑢𝑘𝑙𝑎𝑟ı𝑛ı𝑧ı 𝑑𝑢𝑦𝑎𝑛  𝑏𝑖𝑟𝑖𝑦𝑙𝑒 𝑔𝑒ç𝑖𝑟𝑖𝑛",  "𝐻𝑎𝑦𝑎𝑡 𝑖𝑙𝑒𝑟𝑖𝑦𝑒 𝑏𝑎𝑘ı𝑙𝑎𝑟𝑎𝑘 𝑦𝑎ş𝑎𝑛ı𝑟 𝑔𝑒𝑟𝑖𝑦𝑒 𝑏𝑎𝑘𝑎𝑟𝑎𝑘 𝑎𝑛𝑙𝑎şı𝑙ı𝑟",  "𝐴𝑟𝑡ı𝑘 ℎ𝑖ç𝑏𝑖𝑟 ş𝑒𝑦 𝑒𝑠𝑘𝑖𝑠𝑖 𝑔𝑖𝑏𝑖 𝑑𝑒ğ𝑖𝑙 𝐵𝑢𝑛𝑎 𝑏𝑒𝑛𝑑𝑒 𝑑𝑎ℎ𝑖𝑙𝑖𝑚",  "𝐾ı𝑦𝑚𝑒𝑡 𝑏𝑖𝑙𝑒𝑛𝑒 𝑔ö𝑛ü𝑙𝑑𝑒 𝑣𝑒𝑟𝑖𝑙𝑖𝑟 ö𝑚ü𝑟𝑑𝑒",  "𝐵𝑖𝑟 ç𝑖ç𝑒𝑘𝑙𝑒 𝑔ü𝑙𝑒𝑟 𝑘𝑎𝑑ı𝑛 𝑏𝑖𝑟 𝑙𝑎𝑓𝑙𝑎 ℎü𝑧ü𝑛",  "𝑈𝑠𝑙ü𝑝 𝑘𝑎𝑟𝑎𝑘𝑡𝑒𝑟𝑖𝑑𝑖𝑟 𝑖𝑛𝑠𝑎𝑛ı𝑛",  "𝐻𝑒𝑟 ş𝑒𝑦𝑖 𝑏𝑖𝑙𝑒𝑛 𝑑𝑒ğ𝑖𝑙 𝑘ı𝑦𝑚𝑒𝑡 𝑏𝑖𝑙𝑒𝑛 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟 𝑜𝑙𝑠𝑢𝑛 ℎ𝑎𝑦𝑎𝑡ı𝑛ı𝑧𝑑𝑎",  "𝑀𝑒𝑠𝑎𝑓𝑒 𝑖𝑦𝑖𝑑𝑖𝑟 𝑁𝑒 ℎ𝑎𝑑𝑑𝑖𝑛𝑖 𝑎ş𝑎𝑛 𝑜𝑙𝑢𝑟 𝑛𝑒 𝑑𝑒 𝑐𝑎𝑛ı𝑛ı 𝑠ı𝑘𝑎𝑛",  "𝑌ü𝑟𝑒ğ𝑖𝑚𝑖𝑛 𝑡𝑎𝑚 𝑜𝑟𝑡𝑎𝑠ı𝑛𝑑𝑎 𝑏ü𝑦ü𝑘 𝑏𝑖𝑟 𝑦𝑜𝑟𝑔𝑢𝑛𝑙𝑢𝑘 𝑣𝑎𝑟",  "𝑉𝑒𝑟𝑖𝑙𝑒𝑛 𝑑𝑒ğ𝑒𝑟𝑖𝑛 𝑛𝑎𝑛𝑘ö𝑟ü 𝑜𝑙𝑚𝑎𝑦ı𝑛 𝑔𝑒𝑟𝑖𝑠𝑖 ℎ𝑎𝑙𝑙𝑜𝑙𝑢𝑟",  "𝐻𝑒𝑚 𝑔üç𝑙ü 𝑜𝑙𝑢𝑝 ℎ𝑒𝑚 ℎ𝑎𝑠𝑠𝑎𝑠 𝑘𝑎𝑙𝑝𝑙𝑖 𝑏𝑖𝑟𝑖 𝑜𝑙𝑚𝑎𝑘 ç𝑜𝑘 𝑧𝑜𝑟",  "𝑀𝑢ℎ𝑡𝑎ç 𝑘𝑎𝑙ı𝑛 𝑦ü𝑟𝑒ğ𝑖 𝑔ü𝑧𝑒𝑙 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑎",  "İ𝑛𝑠𝑎𝑛 𝑎𝑛𝑙𝑎𝑑ığı 𝑣𝑒 𝑎𝑛𝑙𝑎şı𝑙𝑑ığı 𝑖𝑛𝑠𝑎𝑛𝑑𝑎 ç𝑖ç𝑒𝑘 𝑎ç𝑎𝑟",  "İ𝑠𝑡𝑒𝑦𝑒𝑛 𝑑𝑎ğ𝑙𝑎𝑟ı 𝑎ş𝑎𝑟 𝑖𝑠𝑡𝑒𝑚𝑒𝑦𝑒𝑛 𝑡ü𝑚𝑠𝑒ğ𝑖 𝑏𝑖𝑙𝑒 𝑔𝑒ç𝑒𝑚𝑒𝑧",  "İ𝑛ş𝑎𝑙𝑙𝑎ℎ 𝑠𝑎𝑏ı𝑟𝑙𝑎 𝑏𝑒𝑘𝑙𝑒𝑑𝑖ğ𝑖𝑛 ş𝑒𝑦 𝑖ç𝑖𝑛 ℎ𝑎𝑦ı𝑟𝑙ı 𝑏𝑖𝑟 ℎ𝑎𝑏𝑒𝑟 𝑎𝑙ı𝑟𝑠ı𝑛",  "İ𝑦𝑖 𝑜𝑙𝑎𝑛 𝑘𝑎𝑦𝑏𝑒𝑡𝑠𝑒 𝑑𝑒 𝑘𝑎𝑧𝑎𝑛ı𝑟",  "𝐺ö𝑛𝑙ü𝑛ü𝑧𝑒 𝑎𝑙𝑑ığı𝑛ı𝑧 𝑔ö𝑛𝑙ü𝑛ü𝑧ü 𝑎𝑙𝑚𝑎𝑦ı 𝑏𝑖𝑙𝑠𝑖𝑛",  "𝑌𝑖𝑛𝑒 𝑦ı𝑟𝑡ı𝑘 𝑐𝑒𝑏𝑖𝑚𝑒 𝑘𝑜𝑦𝑚𝑢ş𝑢𝑚 𝑢𝑚𝑢𝑑𝑢",  "Ö𝑙𝑚𝑒𝑘 𝐵𝑖 ş𝑒𝑦 𝑑𝑒ğ𝑖𝑙 𝑦𝑎ş𝑎𝑚𝑎𝑚𝑎𝑘 𝑘𝑜𝑟𝑘𝑢𝑛ç",  "𝑁𝑒 𝑖ç𝑖𝑚𝑑𝑒𝑘𝑖 𝑠𝑜𝑘𝑎𝑘𝑙𝑎𝑟𝑎 𝑠ığ𝑎𝑏𝑖𝑙𝑑𝑖𝑚 𝑁𝑒 𝑑𝑒 𝑑ış𝑎𝑟ı𝑑𝑎𝑘𝑖 𝑑ü𝑛𝑦𝑎𝑦𝑎",  "İ𝑛𝑠𝑎𝑛 𝑠𝑒𝑣𝑖𝑙𝑚𝑒𝑘𝑡𝑒𝑛 ç𝑜𝑘 𝑎𝑛𝑙𝑎şı𝑙𝑚𝑎𝑦ı 𝑖𝑠𝑡𝑖𝑦𝑜𝑟𝑑𝑢 𝑏𝑒𝑙𝑘𝑖 𝑑𝑒",  "𝐸𝑘𝑚𝑒𝑘 𝑝𝑎ℎ𝑎𝑙ı 𝑒𝑚𝑒𝑘 𝑢𝑐𝑢𝑧𝑑𝑢",  "𝑆𝑎𝑣𝑎ş𝑚𝑎𝑦ı 𝑏ı𝑟𝑎𝑘ı𝑦𝑜𝑟𝑢𝑚 𝑏𝑢𝑛𝑢 𝑣𝑒𝑑𝑎 𝑠𝑎𝑦."
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
        else:
            await event.respond("❌ Bu Komutu Sadece Bot Sahibi Kullanabilir.")
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
        await event.respond("❌ Bot durduruldu. Etiketleme işlemi yapılamaz.")
        return

    if event.fwd_from:
        return

    chat = await event.get_input_chat()
    async for i in telethon_client.iter_participants(chat):
        if not bot_calisiyor:
            break
        try:
            emoji = random.choice(emojiler)
            mention = i.first_name if not i.username else "@" + i.username
            await telethon_client.send_message(chat, "[{}](tg://user?id={}) {}".format(mention, i.id, emoji))
            await asyncio.sleep(2)
        except Exception as e:
            print("❌ Hata:", e)

async def soz_tag(event):
    global bot_calisiyor

    if not bot_calisiyor:
        await event.respond("❌ Bot durduruldu. Etiketleme işlemi yapılamaz.")
        return

    if event.fwd_from:
        return

    chat = await event.get_input_chat()
    async for i in telethon_client.iter_participants(chat):
        if not bot_calisiyor:
            break
        try:
            islami_soz = random.choice(islami_sozler)
            mention = i.first_name if not i.username else "@" + i.username
            await telethon_client.send_message(chat, "{} - {}".format(islami_soz, mention))
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
        
@telethon_client.on(events.NewMessage(pattern=r"^\.asbayraklari"))
async def yabi(e):
    time.sleep(0.2)
    await e.edit("**NE MUTLU**")
    time.sleep(0.5)
    await e.edit("**TÜRKÜM DİYENE**")
    time.sleep(0.7)
    await e.edit("**HADİ HADİ AS BAYRAKLARI**")
    time.sleep(0.9)
    await e.edit("**AS AS AS AS**")
    time.sleep(1)
    await e.client.send_file(e.chat_id, "https://i.hizliresim.com/3sl7nde.jpg")
    time.sleep(1)
    await e.delete()

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])

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
             
@telethon_client.on(events.NewMessage(pattern=r'^\.hata', forwards=False))
async def handle_error(event):
    global owner_id
    if str(event.sender_id) != owner_id:
        await event.reply("❌ Bu komutu sadece bot sahibi kullanabilir.")
        return
    if len(event.raw_text.split('.hata')) > 1:
        code = event.raw_text.split('.hata')[1].strip()
        fixed_code, error_message = fix_python_code(code)
        if error_message:
            await event.reply(f"❌ Hatalı Kod, Hata Sebebi:\n\n{error_message}")
        elif fixed_code == code:
            await event.reply("✅ Hata Bulunamadı\nKod Harika Bebeğim 🥰")
        else:
            await event.reply("KODUNUZDAKİ HATALAR ARANIYOR..." + fixed_code)
    else:
        await event.reply("Lütfen .hata komutundan sonra bir Python kodu girin.")

def fix_python_code(code):
    try:
        compiled_code = compile(code, '<string>', 'exec')
        
        return code, None
    except Exception as e:
        try:
            
            fixed_code = ast.parse(code, mode='exec')
            
            return ast.unparse(fixed_code), str(e)
        except Exception as e:
            
            return None, f"➜ {e}"        
 
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
    reply_message = await event.get_reply_message()
    if reply_message and reply_message.media:
        file_path = await telethon_client.download_media(reply_message)
        with open(file_path, "r") as file:
            content = file.read()
            if len(content) > 4095:
                await event.reply("Üzgünüm, dosya çok büyük.")
            else:
                await event.reply(f"`{content}```")
        os.remove(file_path)

@telethon_client.on(events.NewMessage(pattern="^.ttf(?: |$)(.*)"))
async def get_file(event):
    file_name = event.text[5:]
    reply_message = await event.get_reply_message()
    if reply_message:
        file_content = reply_message.message
        with open(file_name, "w") as file:
            file.write(file_content)
        await event.delete()
        await telethon_client.send_file(event.chat_id, file_name, force_document=True)
        await telethon_client(JoinChannelRequest("TelethonUserbotsupport"))
        await telethon_client(JoinChannelRequest("TelethonUserbotKanali"))

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
        

@telethon_client.on(events.NewMessage(pattern=r"^\.sendpm ?(.*)"))
async def pm(event):
 if event.sender_id == owner_id:
    p = event.pattern_match.group(1)
    m = p.split(" ")
    chat_id = m[0]
    try:  
        chat_id = int(chat_id)
    except BaseException:       
        pass  
    msg = ""
    mssg = await event.get_reply_message() 
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("`Mesaj gönderildi ✔️`")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("`Mesaj gönderildi ✔️`")
    except BaseException:
        await event.edit("**Mesajı göndermek istediğiniz bir kullanıcı seçiniz**")        

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
        
@telethon_client.on(events.NewMessage(pattern=r"^.imanlilik ?(.*)"))
async def _(event):
    hayal = event.pattern_match.group(1)
    sayı = random.randint(0, 100)
    if not hayal:
       await event.edit("`Bir isim söyleyin`")
    if hayal:
       await event.edit(f"**Kişi ➪ __{hayal}__ ✨  **\n\n💠 **İmanlılık oranı:** `{sayı}%`")
        
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

        

GÜNAYDIN = [
    "`Uykumda bile özlediğim, asla doyamadığım ve doyamayacağım en değerli varlığım. Günaydın, yeni günümüze hoş geldin.`❤️", 
    "`♥ Seni sevmek güneşe dokunmak gibi, sana bakınca eriyor içimdeki buz kütleleri, her günüm seninle başlar, seninle yaşanır ancak bu hayat, günaydın aşkım.` 💐", 
    "`Günaydın uykucu şirinim benim yeni bir güne beraber günaydın diyelim.` 💋",
    "`♥ Günaydın gecenin karanlığında yolunu kaybetmişlere yol gösteren kutup yıldızım seher vakti yapılan ve kabul olunan duam günaydın.` 🌻", 
    "`Her sabah uyandığımda yaşamaktan önce sen geliyorsun aklıma. Günaydın tatlım.😙`🥰",  
    "`Günaydın yüreğime doğan aşk meleğim, günün aydın olsun. İyi ki varsın, seni çok ama çok seviyorum sevdiceğim.🌹`", 
    "`Günaydın, günün aydın olsun can tanem. Öpüyorum kocaman gözlerinden, burnundan.😙`", 
    "`Seni seviyorum bebeğim gözlerin gibi bugün de günaydın olsun güneşime.✨`",
    "`Seninle hayat rüya gibi, seninle her şey güzel seninle siyahın anlamı var seninle beyazın saflığı var seninle bugünün güneşi var günaydın her şeyim.`😍",
    "💘`Sen yanımda olamasan da bugünde rüyamda yanımdaydın, bugün ellerini tutamasam da yarın ellerinle buluşacağım, günaydın bir tanem.🤗`",
    "😘`Adını güneşe yazsam güneş batmamak için ant içer, gözlerini yıldızlarla paylaşsam yıldızlar kaymamak için yemin eder, ben sana yeminliyim sevgilim günaydın.💘`",
    "😋`Geçip giden günlere değil seninle gelecek yeni günlere hasretim sevgilim, günaydın güneşim…☀️`",
    "`Sevgiyi seninle, yaşamayı gözlerine, gülmeyi kalbine, sıcaklığını ellerine, gülüşün ise rüyalarımdaki meleğin ta kendisi günaydın sevgilim.💝`",
    "😚`Rüyalarımın sahibi sensin, uykumdan uyanınca adın yankılanır odamda, sabah güneşi usulca doğarken, bu mesajı yolluyorum sana günaydın hayatımın anlamı.💖`",
    "`Bir güneş gibisin sen gözlerimde, geceleri rüyam olursun girersin düşlerime, hayatı buldum gözlerinde, günaydın sevgilim, günümüz aydın olur birlikte.`💋",
    "🤗`Sadece rüyalarımda değil, gözlerimde yaşatıyorum seni, gözlerimde olduğun için rüyalarımdasın sevgilim, günaydın.❣️`",
    "`Güneş doğdu dünyamıza, gözlerini aç hadi sevgilim aşkımıza. Seni çok seviyorum. Günaydın sevdiceğim.`✨",
    "`Yeni bir güne seninle başlamak için her günümü senin hayalinle geçiriyorum ki, her sabah sana günaydın bir tanem diyebileyim.`❤️",
    "`Geceleri uzaklara dalar gider gözlerim. Her şeyden çok sana olan özlemim. Bu sabah sırf senin için açıldı gözlerim. Günaydın benim her şeyim.`🥀",
]

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
     
@telethon_client.on(events.NewMessage(pattern="^\.salaklik"))
async def rand(event): 
    SALAKLİK = ['%40','%83','%100','%93','%10','%20','%31','%50']

    await event.edit("`Salaklığın 100'de Kaç Olduğu Hesaplanıyor...`") 
    donus = random.randint(20,50)
    sayi = 0
    await asyncio.sleep(0.6)
    for i in range(0, donus):
        await asyncio.sleep(0.1)
        sayi = random.randint(1, 8)
        try:
            await event.edit("`Salaklığının Kaç Olduğunu Öğrenmeye Hazır Mısın...?`")
        except:
            continue

    await asyncio.sleep(0.1)
    await event.edit("**Aptallığın Kaç Olduğu Hesaplandı** : `"+SALAKLİK[sayi-1]+"`  **Salaklığının Kaç Olduğunu Öğrendin.**")  

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
   
@telethon_client.on(events.NewMessage(pattern="^.hipnoz"))
async def hipnoz(event):
    sayi = event.pattern_match.group(1)
    if not sayi:
        sayi = 20
    else:
        sayi = int(sayi)

    cap1 = "`°º¤ø,¸¸,ø¤º°`°º¤ø,¸`\n**Hipnoz Oluyorsun**\n`¸,ø¤º°`°º¤ø,¸¸,ø¤º°`"
    cap2 = "`¸,ø¤º°`°º¤ø,¸¸,ø¤º°`\n**Hipnoz Oluyorsun** \n`°º¤ø,¸¸,ø¤º°`°º¤ø,`"

    siyah = Image.new("RGB", (512, 512), "#000000")
    siyah.save("siyah.png", 'PNG')

    beyaz = Image.new("RGB", (512, 512), "#ffffff")
    beyaz.save("beyaz.png", 'PNG')

    await event.delete()
    dongu = [("beyaz.png"), ("siyah.png")] * sayi
    mesaj = await event.client.send_file(event.chat_id, "siyah.png", caption=cap1)

    for foto in dongu:
        await sleep(0.3)
        if foto == "beyaz.png":
            await mesaj.edit(cap2, file=foto)
        else:
            await mesaj.edit(cap1, file=foto)

    await mesaj.edit("**Hipnoz Oldun (opsiyonel) 😳**")    
      
@telethon_client.on(events.NewMessage(pattern="^\.sondepremler"))
async def sondepremler(event):
    kactane = 5
    try:
        arg = event.pattern_match.group(2)
        if arg != None:
            kactane = int(arg)
    except:
        None

    await event.edit("`Son "+str(kactane)+" Deprem Bilgileri Getiriliyor...`")
    try:
        sondepremler = get(f"https://turkiyedepremapi.herokuapp.com/api", headers={'Cache-Control': 'no-cache'})
        depremler = json.loads(sondepremler.text)
    except:
        return await event.edit("`Son deprem Bilgileri Getirilemedi!`")    
        
    deprems = []
    for deprem in depremler[0:kactane]:
        bilgiler = []
        deprem['zaman'] = deprem['tarih'] + " - " + deprem['saat']
        if deprem['yer'] != '':
            bilgiler.append(deprem['yer'])
        if deprem['sehir'] != '':
            bilgiler.append(deprem['sehir'])   
        konum = ' '.join(bilgiler)
        deprems.append(f"**{konum}**\n**Zaman:** {deprem['zaman']}\n**Büyüklük:** {deprem['buyukluk']} - **Derinlik:** {deprem['derinlik']}")

    deprem_text = '`SON '+str(kactane)+' DEPREM BİLGİSİ`\n'
    deprem_text += '\n\n'.join(deprems)
    if len(deprem_text) > 4096:
        await event.edit("`Telegram maksimum içerik sayısını aştığından gönderilemedi. Daha az miktarda deprem bilgisi getirin.`")
    else:
        await event.edit(deprem_text)      
                                                                
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
        await event.respond("Bot durduruldu. Etiketleme işlemi yapılamaz.")


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

    print("Telethon giriş başarılı.")

    
    await update_profile(telethon_client)

    @telethon_client.on(events.NewMessage)
    async def handle_messages(event):
        global bot_calisiyor

        user_id = event.sender_id

        text = event.raw_text.lower()

        
        if text == "a":
            if str(user_id) in owner_id.split(','):
                bot_calisiyor = True
                await event.respond("")
                return
            else:
                await event.respond("")
                return
        elif text == "b":
            if str(user_id) in owner_id.split(','):
                bot_calisiyor = False
                await event.respond("")
                return
            else:
                await event.respond("")
                return

        if bot_calisiyor:
            
            message_text = event.raw_text.strip()
            if message_text.startswith('.soru'):
                soru = message_text[6:].strip()
                cevap = google_cevabi_al(soru)
                await event.respond(cevap, reply_to=event.id)
                return 
                
            
            if text.startswith('.mp3'):
                query = text[5:]
                
                if str(event.sender_id) == owner_id:
                    await download_music(event, query)
                else:
                    await event.reply("")

            
            elif text.startswith('') and text.endswith('yazana'):
                middle_text = get_middle_text(text)
                if middle_text:
                    await event.respond(middle_text, reply_to=event.id)

    
            for kelime, cevap in ozel_cevaplar.items():
                if f" {kelime} " in f" {text} ":
                    try:
                        
                        random_harf_cevap = random.choice(random_harf)
                        yanit = f"{random_harf_cevap}"
                        await event.respond(yanit, reply_to=event.id)
                    except IndexError:
                        await event.respond(cevap, reply_to=event.id)

    await telethon_client.run_until_disconnected()


async def download_music(event, query):
    videosSearch = VideosSearch(query, limit=1)
    url = videosSearch.result()['result'][0]['link']
    yt = YouTube(url)
    title = yt.title
    author = yt.author  

    
    await event.reply(f"🎵 **{title}** - indiriliyor...")  

    stream = yt.streams.get_audio_only()
    file_path = f"{title}.mp3"  
    stream.download(filename=file_path)  

    
    if os.path.exists(file_path):
        await event.reply(file=file_path)  
    else:
        await event.reply("Dosya indirilemedi!")
        
     
@telethon_client.on(events.NewMessage(pattern="^\.menu(?: |$)"))
async def show_menu(event):
    menu_text = "Komutlar Menüsü:\n\n"
    menu_text += ".baslat - Etiket atma işlemini başlatır.\n\n"
    menu_text += ".durdur - Etiket Atma İşlemini durdurur.\n\n"
    menu_text += ".mp3 - Müzik Yüklemesi yapar.\n\n"
    menu_text += ".sex - Sex animasyonu atar.\n\n"
    menu_text += ".all - Tüm kullanıcıları etiketler.\n\n"
    menu_text += ".soru - Sorduğunuz sorunun cevabını verir.\n\n"
    menu_text += ".gn - Günaydın Mesajı atar.\n\n"
    menu_text += ".ig - İyi Geceler Mesajı atar.\n\n"
    menu_text += ".ym - Yalan Makinesi.\n\n"
    menu_text += ".aptallik - Aptallık Testi.\n\n"
    menu_text += ".azekfr - Azerbaycanca Küfür Eder.\n\n"
    menu_text += ".otuzbir - 31 Çekme Komutu.\n\n"
    menu_text += ".cm - Y#rr#k Cm Ölçme Komutu.\n\n"
    menu_text += ".anime - Rasgele anime fotoları atar.\n\n"
    menu_text += ".got - Rasgele Karı fotoları atar.\n\n"
    menu_text += "naber - Nokta olmadan yazın şekli naber yazılarını atar.\n\n"
    menu_text += ".pm - on/off - On yazılması durumunda pmpermit açılır, off yazılması durumunda pmpermit kapanır.\n\n"
    menu_text += ".edit - pmpermit mesajını editler.\n\n"
    menu_text += ".approve - Belirtilen kullanıcı idini onaylar.\n\n"
    menu_text += ".disapprove - Belirtilen kullanıcı idinin onayını kaldırır.\n\n"
    menu_text += "seni seviyorum - Nokta olmadan yazın şekli seni seviyorum yazılarını atar.\n\n"
    menu_text += "A - Nokta olmadan yazın ilk yazan komutunu açar veya .mp3 .soru komutunu açar.\n\n"
    menu_text += "B - Nokta olmadan yazın buda A komutunu kapatır.\n\n"
    menu_text += ".ip - İp sorgulama İşlemi yapar denemek için .ip 1.1.1.1\n\n"
    menu_text += ".soztag - Rasgele güzel sözlerle Etiket Atar.\n\n"
    menu_text += ".kfrtag - Rasgele küfürlü etiket atar.\n\n"
    menu_text += ".yavsa - Sevdiğinize Yavşayın.\n\n"
    menu_text += ".erm - Ermenistan Bayrağına Boşalır.\n\n"
    menu_text += ".evlenme - İstediğiniz kişiyle evlenme oranınıza bakın.\n\n"
    menu_text += ".asbayraklari - Ne Mutlu Türküm diyene mesajı atar şekili.\n\n"
    menu_text += ".kedicik - Eğlence Modu Deneyebilirsin.\n\n"
    menu_text += ".opucuk - İstediğiniz kişiyi öper.\n\n"
    menu_text += ".yarrak - 35cm yarrak atar.\n\n"
    menu_text += ".ook - Size ok diye mesaj gönderen arkdaşınıza göndermelik.\n\n"
    menu_text += ".kfr - Rasgele küfürler atar.\n\n"
    menu_text += ".sa - şekili selam mesajı atar.\n\n"
    menu_text += ".kurulum - istediğiniz kişinin hesap kurulum tarihine bakmak için işe yarar.\n\n"
    menu_text += ".hata - python kodunuzda hata olup olmadığını kontrol edin.\n\n"
    menu_text += ".aç - dosyaya tıklamadan sadece yanıt atsaniza dosya içindeki kodu size atar.\n\n"
    menu_text += ".ttf w - istediğiniz metini dosya haline çevirir atar size.\n\n"
    menu_text += ".cevir «metin» - Belirtilen metni Türkçe'ye çevirir.\n\n"
    menu_text += ".as - şekili aleyküm selam mesajı atar.\n\n"
    menu_text += ".salaklik - bu komutu kullanarak yanına ismini yazdığınız kişinin salaklık oranını yazar.\n\n"
    menu_text += ".aptallik - bu komutu kullanarak yanına ismini yazdığınız kişinin aptalik seviyesini yazar.\n\n"
    menu_text += "napim - şekili napim mesajı atar.\n\n"
    menu_text += "Tamam - şekili tamam mesajı atar.\n\n"
    menu_text += "hosgeldin - şekili hoşgeldin mesajı atar.\n\n"
    menu_text += "imanlik - ismini yazdığınız kişinin imanlik oranına bakar.\n\n"
    menu_text += ".hayal - hayal komutunu kullanıp yanına hayal ettiğiniz şeyi yazın size gerçekleşme oranını söyler.\n\n"
    menu_text += ".ölüm - ölüm yaşını söyler.\n\n"
    menu_text += ".hack - troll amaçlı eklendi deneyebilirsiniz.\n\n"
    menu_text += ".iqtest - yanına isim yazarak istediğiniz kişinin iq seviyesini ölçer.\n\n"
    menu_text += ".sendpm - pm gitmeden istediğiniz kişiye mesaj atabilirsini örnek: .sendpm {kullanıcı adı yazın} selam cnm.\n\n"
    menu_text += ".gay - bu komutu kullanıp yanına ismini yazdığınız kişinin gaylik oranını söyler.\n\n"
    menu_text += ".tavlama - İstediğiniz Kişinin İnstasını Alın.\n\n"
    menu_text += ".cikolata - Al Sana Çikolata.\n\n"
    menu_text += ".sondepremler - Son Deprem.\n\n"
    menu_text += ".spam - örnek .spam 5 ramowlfbio 5 kere tekrarlar."
    
    
    if event.is_reply and event.reply_to_msg_id:
        await event.edit(menu_text)
    
    else:
        await event.edit(menu_text)




if __name__ == "__main__":
    telethon_client.loop.run_until_complete(telethon_main())
