# Python-discord-webhook-keylogger
Keylogger I made in python, fixed the biggest issues. Made it WAY less leggier and made it look better (Make sure to read the code so you can edit it)


![This is what the webhook looks like](https://i.postimg.cc/GhSxX7qb/Screenshot-2023-07-01-131439.png)

You may need to either turn off windows defender or add it to your exclusions list to test it.

**Fixed issues:**
-   Less lag
-   Tracks key presses other than words
-   Made it not bold or italic
-   Made the IP at the bottom


#### How to set it up

 1. Make a discord server
 2. Go to server settings > Integrations > Webhooks
 3. Click 'New Webhook'
 4. Click on the new Webhook and edit it to your liking
 5. Open the webhook​.​py file in your text editor
 6. Go back to discord and click 'Copy Webhook URL'
 7. Replace "WEBHOOK_LINK_HERE" with your webhook link
 
 **Optional:**
 
 1. To edit the Webhook color go to line 66 or go to the `"color": 0x113d22` line
 2.  replace `0x113d22` with your color
---
1. To edit the logo go to line 71 or go to the `YOUR_LOGO_LINK_HERE` 
2. replace `YOUR_LOGO_LINK_HERE` with your logo link

 

### Installation

  
The following instructions will install Keylogger using pip3 .

    pip3 install -r requirements.txt
    
  then

        
    python keylogger.py

Now that the keylogger is running check the webhook!

----

Feel free to contribute to fix any problems, or to submit an issue.

Please note, this repository is for educational purposes only. No contributors, major or minor, are to fault for any actions done by this program.
    
----

**My hack forums link:** 
[Hack forums](https://hackforums.net/member.php?action=profile&uid=5380867)
