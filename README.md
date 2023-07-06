# SQLi-Automation

This Script Helps you to automate your SQLi Recon process!! I got this idea by seeing a tweet on Twitter regrading the same, but that dosen't work as intended. So I decided to make my own!! And share will other folks! The Script works this way:
1. It first checks all the "=" in urls.txt (from waybackurls etc).
2. It then replaces the value/contents of it to an SQLi payload.


#Installation Instructions:
1. git clone https://github.com/0x2458bughunt/SQLi-Automation
2. cd SQLi-Automation
3. chmod +x automate.sh
4. ./automate.sh

OR
1. git clone https://github.com/0x2458bughunt/SQLi-Automation
2. cd SQLi-Automation
3. cat command.txt - copy the command.
4. After copying, run it where your urls.txt is there.
5. Then run response_checker.py against the new file which has SQLi payloads.


#Note:
~# You can change SQLi payload according to your interest!
~# Make sure to give "-rt" value greater than or equal to the time delay you provided in your payload. This will avoid false Positives.
~# After it detects the time delay, make sure to exploit it manually or use Ghauri(https://github.com/r0oth3x49/ghauri) or SQLMap to confirm the Vulnerability.
~# You'll be needing qsreplace tool by tomnomnom installed. You can install it from here: https://github.com/tomnomnom/qsreplace


#Socials:
Twitter: https://twitter.com/0x2458/
BuyMeACoffee: https://buymeacoffee.com/0x2458/

Feel Free to contribute! And do give it a star if you like the tool! Good luck!
~0x2458
