import os


b = '██╗  ██╗ █████╗ ██╗     ██╗████████╗ ██████╗  ██████╗ ██╗     ███████╗\n'
a = '██║ ██╔╝██╔══██╗██║    ███║╚══██╔══╝██╔═████╗██╔═████╗██║     ╚══███╔╝\n'
n = '█████╔╝ ███████║██║    ╚██║   ██║   ██║██╔██║██║██╔██║██║       ███╔╝\n'
n1 = '██╔═██╗ ██╔══██║██║     ██║   ██║   ████╔╝██║████╔╝██║██║      ███╔╝\n'
e = '██║  ██╗██║  ██║███████╗██║   ██║   ╚██████╔╝╚██████╔╝███████╗███████╗\n'
r = '╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝\n'

banner = b + a + n + n1 + e +r

root = os.getuid()

if root != 0 :
    print('You must be root')
    exit()
else:
    
    print(banner)
    
    def aircrack():
        os.system("xterm -e sudo apt install -y airckrack-ng")
        print('Aircrack is installed.')
    def burpsuite():
       os.system("sudo xterm -e wget https://github.com/K4L1T00lz/Burpinstall/releases/download/burpsuite/burpsuite.sh && sudo bash burpsuite.sh")
       print('Burpsuite is installed.')
    def crackmapexec():
       os.system("sudo xterm -e sudo pip install pipx && sudo xterm -e pipx ensurepath && sudo xterm -e pipx install crackmapexec")
       print('Crackmapexec is installed.')
    def hydra():
       os.system("xterm -e sudo apt install -y hydra")
       print('Hydra is installed.')
    def john():
       os.system("xterm -e sudo apt install -y john")
       print('John is installed.')
    def metasploit() :
       os.system("xterm -e curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && xterm -e ./msfinstall")
       print('Metasploit is installed.')
    def nmap():
       os.system("xterm -e wget https://nmap.org/dist/nmap-7.92-1.x86_64.rpm && sudo xterm -e sudo alien -v nmap-7.92-1.x86_64.rpm && sudo xterm -e sudo dpkg --install nmap_7.92-2_amd64.deb ")
       print('Nmap is installed.')
    def airgeddon():
       os.system("xterm -e wget https://raw.githubusercontent.com/K4L1T00lz/airgeddoninstall/main/airgeddoninstall.sh && sudo chmod +x airgeddoninstall.sh && sudo xterm -e sudo bash airgeddoninstall.sh ")
       print('Airgeddon is installed.')
    def sqlmap():
       os.system("xterm -e wget https://raw.githubusercontent.com/K4L1T00lz/sqlmapinstall/main/sqlmapinstall.sh && sudo chmod +x sqlmapinstall.sh && sudo xterm -e sudo bash sqlmapinstall.sh")
       print('SqlMap is installed.')
    def wireshark():
       os.system("xterm -e sudo apt install wireshark")
       print('Wireshark is installed.')
    def nikto():
       os.system("xterm -e wget https://raw.githubusercontent.com/K4L1T00lz/niktoinstall/main/niktoinstall.sh && sudo chmod +x niktoinstall.sh && sudo bash niktoinstall.sh")
       print('Nikto is installed.')
    def hashcat():
       os.system("xterm -e sudo apt install -y hashcat")
       print('Hashcat is installed.')
    def seclists():
       os.system("xterm -e sudo git clone --depth 1 https://github.com/danielmiessler/SecLists.git /seclists")
       print('SecLists is installed.')
    def bully():
       os.system("xterm -e sudo apt install bully")
       print('Bully is installed.')
    def bettercap():
       os.system("xterm -e go get -u github.com/bettercap/bettercap && sudo mv go/bin/bettercap /usr/bin/bettercap")
       print('Bettercap is installed.')

    def main():
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
        '[13] SecLists\n'
        '[14] Bully\n'
        '[15] Bettercap\n'
        )

        tc = input('Choose an option ')
        
        if tc == '1' :
            aircrack()
        elif tc == '2' :
            burpsuite()
        elif tc == '3' :
            crackmapexec()
        elif tc == '4' :
            hydra()
        elif tc == '5' :
            john()
        elif tc == '6' :
            metasploit()
        elif tc == '7' :
            nmap()
        elif tc == '8' :
            airgeddon()
        elif tc == '9' :
            sqlmap()
        elif tc == '10' :
            wireshark()
        elif tc == '11'  :
            nikto()
        elif tc == '12' :
            hashcat()
        elif tc == '13' :
            seclists()
        elif tc == '14' :
            bully()
        elif tc == '15' :
            bettercap()
        else :
            print('Invalid option')
            exit()
    main()