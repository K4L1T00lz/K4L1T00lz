import os

root = os.getuid()

if root != 0 :
    print('You must be root')
else:
    print(
    '[1] Aircrack-ng\n'
    '[2] Burpsuite\n'
    '[3] Crackmapexec\n'
    '[4] Hydra\n'       
    '[5] John\n'
    '[6] Metasplot\n'
    '[7] Nmap\n'
    '[8] Airgeddon\n'
    '[9] SqlMap\n'
    '[10] Wireshark\n'
    '[11] Nikto\n'
    '[12] Hashcat\n'
    '[13] Wordlists\n'
    '[14] Bully\n'
    '[15] Bettercap\n'
    )
    tc = input()

if tc == 1 :
    os.system("xterm -e sudo apt install -y airckrack-ng")
    print('Aircrack is installed.')
if tc == 2 :
    os.system("sudo xterm -e wget https://github.com/K4L1T00lz/Burpinstall/releases/download/burpsuite/burpsuite.sh && sudo bash burpsuite.sh")
    print('Burpsuite is installed.')
if tc == 3 :
    os.system("sudo xterm -e sudo pip install pipx && sudo xterm -e pipx ensurepath && sudo xterm -e pipx install crackmapexec")
    print('Crackmapexec is installed.')
if tc == 4 :
    os.system("xterm -e sudo apt install -y hydra")
    print('Hydra is installed.')
if tc == 5 :
    os.system("xterm -e sudo apt install -y john")
    print('John is installed.')
if tc == 6 :
    os.system("xterm -e curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && xterm -e ./msfinstall")
    print('Metasploit is installed.')
if tc == 7 :
    os.system("xterm -e wget https://nmap.org/dist/nmap-7.92-1.x86_64.rpm && sudo xterm -e sudo alien -v nmap-7.92-1.x86_64.rpm && sudo xterm -e sudo dpkg --install nmap_7.92-2_amd64.deb ")
    print('Nmap is installed.')
if tc == 8:
    os.system("xterm -e wget https://raw.githubusercontent.com/K4L1T00lz/airgeddoninstall/main/airgeddoninstall.sh && sudo chmod +x airgeddoninstall.sh && sudo xterm -e sudo bash airgeddoninstall.sh ")
    print('Airgeddon is installed.')
if tc == 9 :
    os.system("xterm -e wget https://raw.githubusercontent.com/K4L1T00lz/sqlmapinstall/main/sqlmapinstall.sh && sudo chmod +x sqlmapinstall.sh && sudo xterm -e sudo bash sqlmapinstall.sh")
    print('SqlMap is installed.')
if tc == 10 :
    os.system("xterm -e sudo apt install wireshark")
    print('Wireshark is installed.')
if tc == 11 :
    os.system("xterm -e wget https://raw.githubusercontent.com/K4L1T00lz/niktoinstall/main/niktoinstall.sh && sudo chmod +x niktoinstall.sh && sudo bash niktoinstall.sh")
    print('Nikto is installed.')
if tc == 12 :
    os.system("xterm -e sudo apt install -y hashcat")
    print('Hashcat is installed.')
if tc == 13 :
    os.system("xterm -e sudo git clone --depth 1 https://github.com/danielmiessler/SecLists.git /seclists")
    print('SecLists is installed.')
if tc == 14 :
    os.system("xterm -e sudo apt install bully")
    print('Bully is installed.')
if tc == 15 :
    os.system("xterm -e go get -u github.com/bettercap/bettercap && sudo mv go/bin/bettercap /usr/bin/bettercap")
    print('Bettercap is installed.')