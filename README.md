# Alertbot
 
Alertbot that sends crypto price data to a discord server.
Can be installed and used on a standalone server by installing requirements.txt and selecting the following;

pair = 'LUNA/USDT' 

WEBHOOK_URL = "https://discord.com/api/webhooks/889265250875080725/nAh5DI_**********************************" 

DISCORD_USERID = "<@606915182**********>"

Installation instructions


Linux:
apt-get install python3-pip // asennetaan pip (pythonin pakettihallinta)  
apt-get install git // asennetaan git  
git clone https://github.com/Sienebob/Alertbot.git  
Cat alertbot.py // muutetaan seuraaviin kohtiin omat tiedot:  
nano alertbot.py  
WEBHOOK_URL = oma discord webhook url (näkyy discordissa)  
DISCORD_USERID = oma discordin käyttäjänumero (näkyy discordissa)  
pip3 install -r requirements.txt // asennetaan tarvittavat python paketit  
Python3 alertbot.py // ajaa ohjelman  
Jos ohjelma halutaan ajastaa jotta se suorittaisi itseään tietyin väliajoin voidaan käyttää komentoa  
Crontab –e // tähän syötetään aika kuinka usein tiedostoa ajetaan esim 5min välein:  


Windows:  
Asennetaan python: https://www.python.org/downloads/  
Ladataan haluamalla tavalla itse ohjelma: https://github.com/Sienebob/Alertbot/  
Muutetaan tekstieditorilla alertbot.py tiedostoon seuraaviin kohtiin omat tiedot:  
WEBHOOK_URL = oma discord webhook url (näkyy discordissa)  
DISCORD_USERID = oma discordin käyttäjänumero (näkyy discordissa)  
Avataan komentokehoite (win+r) -> cmd, navigoidaan samaan kansioon jossa löytyy requirements.txt  
pip install requirements.txt // asentaa tarvittavat paketit  
python alertbot.py ajaa itse alertbot ohjelman.  
