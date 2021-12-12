sudo apt-get install -qq xterm  && echo Installing dependencies....
sleep 1
sudo xterm -e wget https://raw.githubusercontent.com/K4L1T00lz/K4L1T00lz/main/K4L1T00lz-cli.py && sudo xterm -e sudo apt-get install -y build-essential autoconf automake libtool pkg-config libnl-3-dev libnl-genl-3-dev libssl-dev ethtool shtool rfkill zlib1g-dev libsqlite3-dev libpcre3-dev libhwloc-dev libcmocka-dev hostapd wpasupplicant tcpdump screen iw usbutils git ruby default-jdk python3-pip python3-venv alien devscripts golang libpcap-dev libusb-1.0-0-dev libnetfilter-queue-dev
&& echo Dependencies Installed
sleep 1
echo Running the script.....
sleep 1
sudo python3 K4L1T00lz-cli.py
