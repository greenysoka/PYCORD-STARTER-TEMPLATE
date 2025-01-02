# PYCORD STARTER TEMPLATE

Welcome to my py-cord guide for you!
Choose your language:

- [English](#Tutorial (in English))
- [German](#Anleitung (auf Deutsch))


## Tutorial (in English)
Here is what we need:

- Installed Python Version 3.11.x or below (NOT 3.12!) & [pip](https://pip.pypa.io/en/stable/installation/)
- [Visual Studio Code](https://code.visualstudio.com/download), Pycharm or another coding app
- [Discord](https://discord.com) Account where you own a discord server

You have everything? Great!
Then we can begin.

First, let's go to the official Discord developer website: 
https://discord.com/developers/applications

There we create a new bot by clicking on “New Application” in the top right corner:

![image](https://github.com/user-attachments/assets/d2e7f77b-ed08-45a2-b981-7c58658d6602)

Then give the bot a meaningful name and accept the Developer Terms of Service:

![image](https://github.com/user-attachments/assets/19036638-b483-45c4-bd0f-303400d4d7a7)

Now you are on the dashboard of your bot:

![image](https://github.com/user-attachments/assets/c4ced7c5-3f29-438e-811f-9f44218548b5)

Go to the “Bot” tab on the left and activate all 3 Privileged Gateway Intents:

![image](https://github.com/user-attachments/assets/9b92a528-43aa-43c8-bb90-fe2adc7099c2)
 **Do not forget to save changes!**

 Then go to the “OAuth2” tab on the left in the column and scroll down to the heading “OAuth2 URL Generator”. 
There you then select the options **bot** and **applications.commands**. These are always arranged slightly differently, so don't worry if you don't find them in the same position as in the screenshot.

![image](https://github.com/user-attachments/assets/23440872-5499-42ce-8c91-977c7847d7b8)

Then scroll down again, select the option “Administrator” and further down “Guild Install”. Once this is done, copy the generated link and open a new browser tab and paste the link there. A Discord window should then appear:

![image](https://github.com/user-attachments/assets/aeebcb4b-1b5d-4d39-9b37-7d79ea9dd742)

Discord will either open in the browser or the browser will redirect you directly to Discord. It makes no difference, the process is the same for both.
In the window that opens, select the server where you want to have the bot in the future. Then click on “Continue”:

![image](https://github.com/user-attachments/assets/e5801eb9-acb1-42db-87cd-1803c3aa2704)

Discord will then ask you what permissions you want to give the bot. Since we have previously selected Administrator in the selection window, this is also displayed here again. Click “Authorize”

The bot should now appear in your member list:

![image](https://github.com/user-attachments/assets/fa144701-6c4c-4713-b987-3765c86842e0)

If there have been problems up to this point that you have not been able to solve, please contact me on Discord. Write me a direct message: greenysoka
I will try to help you ^^

But now the bot is not online on the server. 
To do this, we first have to import the bot into our development environment. If you don't have any experience with this, we'll use the simple method.
If you already know how to do this, you can clone the repository.

Scroll to the top here on Github, click on the green button with “Code” at the top right and select “Download ZIP”

![image](https://github.com/user-attachments/assets/9fde6077-af2a-4694-b106-b6fb1f827584)

Then open your Visual Studio code or the program you want to use. In the tutorial we do it with Visual Studio Code.
It should look something like this:

![image](https://github.com/user-attachments/assets/cc0fcf80-c6ee-4e85-badd-a9f474bfc2d0)

Of course in your own theme and with other menu items. I have installed quite a few plugins.
Now look for the downloaded ZIP file (PYCORD-STARTER-TEMPLATE-main.zip) in your downloads, open it and drag the folder into your documents or onto your desktop, for example. It is important that you end up with the folder on your desktop and not the ZIP file. We cannot work with the ZIP file.
In the end it should look like this:

![image](https://github.com/user-attachments/assets/c336af09-4e61-45e2-8f53-452a1cd2a551)

Now open your Visual Studio code again, select the “Open folder” option and select the folder on your desktop:

![image](https://github.com/user-attachments/assets/0eb43ae3-1d6f-4807-a376-92ed8d97f6c3)

It should now look like this:

![image](https://github.com/user-attachments/assets/99e5aa14-ddb2-43f9-b442-f1bfa20960c6)

And now I can reassure you, the most difficult part of this tutorial is done!
The code is basically finished and can be tested directly.
But wait, how does the code know what our bot is?

To do this, please go back to the [Developer Portal](https://discord.com/developers/applications) and the “Bot” tab:

![image](https://github.com/user-attachments/assets/f2d7aa7b-e3a4-4908-b6d1-3b236f228bf3)

Then click on “Reset token”. A new token should then be generated. This is what it will look like:

![image](https://github.com/user-attachments/assets/d715383b-943f-42c5-9cfa-ae63357e1e79)

Copy this token and switch back to Visual Studio Code.
Open the file “main.py” and scroll to the bottom.
Paste your copied token where it says “abc”:

![image](https://github.com/user-attachments/assets/d7d04fb3-8e08-426d-b718-5fa2ef9c6631)

Something like this:

![image](https://github.com/user-attachments/assets/1a191df8-0261-4ed5-85a2-560bf86056db)

Now please open the terminal of Visual Studio Code and insert the following command:

```
pip install py-cord
```

This command installs the library so that you can work with Discord. 
Execute the command by pressing “Enter” and then the package should be installed. If this does not work, please contact me!

And then? That's it!
If all the steps have worked, we can now start the bot.
To do this, enter another command in the terminal:

```
python main.py
```

![image](https://github.com/user-attachments/assets/ae12f2c7-3697-49d1-bf32-c30dbb43e7c6)

You will know that everything has worked if this message appears. This means that the bot has been started and is now available!
Switch back to Discord and look at your server list:

![image](https://github.com/user-attachments/assets/5310320f-3cdc-4b76-8c1a-9687ae615280)

The bot is online and smiling at you :)

Every line of my code is described in more detail in main.py. I also link here to the official Py-Cord Guide. It describes how you can create commands, buttons, forms and more:

https://guide.pycord.dev/category/getting-started

If you want to continue and are looking for tutorials, go to YouTube and search for “Py-Cord” and not “discordpy”. These are two different libraries.

**But the whole thing was a bit too much for you and you don't want to waste too much time creating your own bot?

Then I have just the thing for you! My Discord service [GYX Creative](https://discord.gg/6y7mB96YUA) offers you free and personalized bots that you can configure completely according to your wishes! The bots are then mostly made and managed by me personally so you only get the best :)
From a simple command to a complete support or moderation system, everything can be realized!
Just open a ticket on the GYX server and we are there for you ^^




## Anleitung (auf Deutsch)
Hier ist, was wir brauchen:

- Installierte Python Version 3.11.x oder niedriger (NICHT 3.12!) & [pip](https://pip.pypa.io/en/stable/installation/)
- [Visual Studio Code](https://code.visualstudio.com/download), Pycharm oder eine andere Entwicklungsumgebung
- [Discord](https://discord.com) Konto, auf dem du einen Discord-Server besitzt

Du hast alles? Großartig!
Dann können wir beginnen.

Zuerst gehen wir auf die offizielle Developer-Website von Discord: 
https://discord.com/developers/applications

Dort erstellen wir einen neuen Bot indem wir oben rechts auf "New Application" oder "Neue Anwendung" klicken:

![image](https://github.com/user-attachments/assets/d2e7f77b-ed08-45a2-b981-7c58658d6602)

Danach gibst du dem Bot einen aussagekräftigen Namen und akzeptierst die Developer Terms of Service:

![image](https://github.com/user-attachments/assets/19036638-b483-45c4-bd0f-303400d4d7a7)

Jetzt befindest du dich auf dem Dashboard deines Bots:

![image](https://github.com/user-attachments/assets/c4ced7c5-3f29-438e-811f-9f44218548b5)

Gehe links zum Tab "Bot" und aktiviere alle 3 Privileged Gateway Intents:

![image](https://github.com/user-attachments/assets/9b92a528-43aa-43c8-bb90-fe2adc7099c2)
 **Vergiss nicht Änderungen abzuspeichern!**

Danach gehst du zum Tab "OAuth2" links in der Spalte und scrollst runter bis zur Überschrift "OAuth2 URL Generator". 
Dort wählst du dann die Optionen **bot** und **applications.commands**. Diese sind immer etwas unterschiedlich angeordnet, also keine Sorge wenn du sie nicht an der selben Position findest wie im Screenshot.

![image](https://github.com/user-attachments/assets/23440872-5499-42ce-8c91-977c7847d7b8)

Dann scrollst du nochmal weiter runter, wählst die Option "Administrator" und weiter unten "Guild Install". Sobald das erledigt ist, kopierst du den generierten Link öffnest einen neuen Browser Tab. Dort fügst du dann den Link ein. Dann sollte ein Fenster von Discord erscheinen:

![image](https://github.com/user-attachments/assets/aeebcb4b-1b5d-4d39-9b37-7d79ea9dd742)

Discord wird entweder im Browser geöffnet oder der Browser leitet dich direkt zu Discord weiter. Macht keinen Unterschied, der Ablauf ist bei beidem gleich.
Du wählst in dem Fenster, das sich geöffnet hat den Server aus wo du den Bot in Zukunft haben möchtest. Dann klickst du auf "Continue":

![image](https://github.com/user-attachments/assets/e5801eb9-acb1-42db-87cd-1803c3aa2704)

Discord wird dich dann noch fragen welche Berechtigungen du dem Bot geben möchtest. Da wir im Auswahlfenster vorher Administrator gewähl haben, wird das hier auch wieder angezeigt. Klicke "Autorisieren"

Der Bot sollte jetzt in deiner Mitgliederliste erscheinen:

![image](https://github.com/user-attachments/assets/fa144701-6c4c-4713-b987-3765c86842e0)

Wenn es bis hierhin Probleme gegeben hat, die du nicht lösen konntest, melde dich gerne auf Discord. Schreib mir eine Direktnachricht: greenysoka
Ich werde versuchen dir zu helfen ^^

Jetzt ist der Bot auf dem Server aber nicht online. 
Dazu müssen wir den Bot nämlich erst in unsere Entwicklungsumgebung importieren. Wenn du noch gar keine Erfahrung damit hast, nehmen wir die einfache Methode.
Wenn du bereits weißt wie das geht kannst du das Repository gerne klonen.

Scrolle hier auf Github ganz nach oben, klicke oben rechts auf den grünen Button mit "Code" und wähle "ZIP herunterladen"

![image](https://github.com/user-attachments/assets/9fde6077-af2a-4694-b106-b6fb1f827584)

Danach öffnest du dein Visual Studio Code oder das Programm das du nutzen möchtest. Im Tutorial machen wir es mit Visual Studio Code.
Das sollte ungefähr so aussehen:

![image](https://github.com/user-attachments/assets/cc0fcf80-c6ee-4e85-badd-a9f474bfc2d0)

Natürlich im eigenen Thema und mit anderen Menüpunkten. Ich habe relativ viele Plugins installiert.
Du suchst jetzt die heruntergeladene ZIP Datei (PYCORD-STARTER-TEMPLATE-main.zip) bei deinen Downloads, öffnest sie und ziehst den Ordner darin zb in deine Dokumente oder auf deinen Desktop. Wichtig ist, dass du am Ende den Ordner auf deinem Desktop hast und nicht die ZIP Datei. Mit der ZIP Datei können wir nämlich nicht arbeiten.
Am Ende sollte es so aussehen:

![image](https://github.com/user-attachments/assets/c336af09-4e61-45e2-8f53-452a1cd2a551)

Jetzt öffnest du wieder dein Visual Studio Code, wählst die Option "Ordner öffnen" und wählst den Ordner auf deinem Desktop aus:

![image](https://github.com/user-attachments/assets/0eb43ae3-1d6f-4807-a376-92ed8d97f6c3)

Das ganze sollte jetzt so aussehen:

![image](https://github.com/user-attachments/assets/99e5aa14-ddb2-43f9-b442-f1bfa20960c6)

Und damit kann ich dich beruhigen, der schwierigste Teil dieses Tutorials ist erledigt!
Der Code ist im Grunde fertig und kann direkt getestet werden.
Doch warte, wie weiß nun der Code was unser Bot ist?

Dazu gehst du bitte nochmal in das [Developer Portal](https://discord.com/developers/applications) und zum Tab "Bot":

![image](https://github.com/user-attachments/assets/f2d7aa7b-e3a4-4908-b6d1-3b236f228bf3)

Dort klickst du dann auf "Token zurücksetzen". Dann sollte ein neuer Token generiert werden. So sieht das dann aus:

![image](https://github.com/user-attachments/assets/d715383b-943f-42c5-9cfa-ae63357e1e79)

Diesen Token kopierst du und wechselst zurück in Visual Studio Code.
Öffne die Datei "main.py" und scrolle bis zum Boden.
Dort wo steht "abc" steht fügst du deinen kopierten Token ein:

![image](https://github.com/user-attachments/assets/d7d04fb3-8e08-426d-b718-5fa2ef9c6631)

In etwa so wie hier:

![image](https://github.com/user-attachments/assets/1a191df8-0261-4ed5-85a2-560bf86056db)

Jetzt öffne bitte das Terminal von Visual Studio Code und füge dort folgenden Befehl ein:

```
pip install py-cord
```

Dieser Befehl installiert die Bibliothek sodass du mit Discord arbeiten kannst. 
Führe den Befehl aus indem du "Eingabe" drückst und dann sollte das Paket installiert werden. Sollte das nicht klappen, melde dich bei mir!

Und dann? Das wars!
Wenn alle Schritte geklappt haben können wir den Bot nun starten.
Dazu gib im Terminal einen weiteren Befehl ein:

```
python main.py
```

![image](https://github.com/user-attachments/assets/ae12f2c7-3697-49d1-bf32-c30dbb43e7c6)

Du weißt dass alles geklappt hat, wenn genau diese Meldung erscheint. Das bedeutet dass der Bot gestartet wurde und nun erreichbar ist!
Wechsle zurück zu Discord und schau in deine Serverliste:

![image](https://github.com/user-attachments/assets/5310320f-3cdc-4b76-8c1a-9687ae615280)

Der Bot ist online und lächelt dich an :)


In der main.py ist jede Zeile meines Codes genauer beschrieben. Außerdem verlinke ich hier auch auf den offiziellen Py-Cord Guide. Dort wird beschrieben wie du Befehle, Buttons, Formulare und mehr erstellen kannst:

https://guide.pycord.dev/category/getting-started

Falls du weitermachen möchtest und Tutorials suchst, geh auf YouTube und suche nach "Py-Cord" und nicht "discordpy". Das sind nämlich zwei unterschiedliche Bibliotheken.

**Dir war das Ganze aber bisschen zu viel und du möchtest nicht zu viel Zeit auf die eigene Erstellung eines Bots verschwenden?**

Dann hab ich genau das richtige! Mein Discord Service [GYX Creative](https://discord.gg/6y7mB96YUA) bietet dir kostenlose und persönlich angefertigte Bots an, die du komplett nach deinen Wünschen konfigurieren kannst! Die Bots werden dann meist von mir persönlich angefertigt und verwaltet sodass du nur das beste bekommst :)
Vom einfachen Befehl bis hin zum kompletten Support oder Moderationssystem kann alles umgesetzt werden!
Öffne einfach ein Ticket auf dem GYX Server und wir sind für dich da ^^
