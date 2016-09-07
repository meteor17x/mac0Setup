xcode-select --install
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles' >> ~/.bash_profile
source ~/.bash_profile
brew install qt5
brew install aria2
brew install python3
brew install vapoursynth
brew install mpv --with-bundle --with-vapoursynth
brew linapps mpv
brew install mkvtoolnix --with-qt5
#sudo python get-pip[4F900010].py
curl -# -o get-pip.py https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
rm get-pip.py
#sudo pip install shadowsocks
git clone -b master https://github.com/shadowsocks/shadowsocks.git
sudo python3 setup.py
brew cask install firefox
brew cask install gimp
brew cask install virtualbox
brew cask install libreoffice

aria2c https://dl.google.com/chrome/mac/stable/GGRO/googlechrome.dmg
