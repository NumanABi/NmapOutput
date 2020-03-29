#Nmap aracındaki sonuclarin xml olarak bastirilmasi
#(Python + Nmap + cmd = xml)

import os
os.system("nmap metingerdan.com -oX mett1.xml")
os.system("nmap planetekno.com -oX mett2.xml")
os.system("nmap instagram.com -oX mett3.xml")
os.system("nmap facebook.com -oX mett4.xml")
os.system("nmap linkedin.com -oX mett5.xml")
os.system("nmap bankofamerica.com -oX mett6.xml")
#Birden çok test edilecek site belirtilebilir
