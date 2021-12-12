sudo apt-get install -qq xterm  && echo Installing dependencies....
sleep 1
sudo xterm -e wget 0.0.0.0/test.py && sudo xterm -e sudo apt-get install -y build-essential autoconf automake libtool pkg-config libnl-3-dev libnl-genl-3-dev libssl-dev ethtool shtool rfkill zlib1g-dev libpcap-dev libsqlite3-dev libpcre3-dev libhwloc-dev libcmocka-dev hostapd wpasupplicant tcpdump screen iw usbutils git ruby default-jdk python3-pip python3-venv alien devscripts && echo Installed
sleep 1
echo Running the script.....
sleep 1
python3 test.py

