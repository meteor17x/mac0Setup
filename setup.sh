xcode-select --install
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles' >> ~/.bash_profile
source ~/.bash_profile
brew install qt5
brew install aria2
brew install python3
brew install vapoursynth
brew install mpv --with-bundle --with-vapoursynth
brew install mkvtoolnix --with-qt5
#sudo python get-pip[4F900010].py
sudo pip install shadowsocks
sudo python3 setup.py
