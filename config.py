#!/bin/python
#shadowsocks_conf = open("~/etc/shadowsocks.json",'w')
#print（）
import os
homepath = os.path.expanduser('~')
print("aria2 token")
aria2_token = input()
aria2_token = 'wwssaadd'
print("shadowsocks address")
shadowsocks_addr = input()
print("shadowsocks server port")
shadowsocks_port = input()
print("shadowsocks key")
shadowsocks_key = input()
print("ss encrypt method")
shadowsocks_method = input()


aria2_conf = open('%s/etc/aria2.conf' % homepath,'w')
aria2_conf.write('''\
enable-rpc = true
rpc-allow-origin-all = true
rpc-listen-all = true
rpc-secret = %s
max-concurrent-downloads = 7
dir = %s/Downloads
file-allocation = prealloc
bt-require-crypto = true
''' % (aria2_token, homepath))

aria2_plist = open('%s/Library/LaunchAgents/aria2.plist' % homepath,'w')
aria2_plist.write('''\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
	<dict>
		<key>Label</key>
		<string>com.aria2.app</string>
		<key>ProgramArguments</key>
		<array>
			<string>/usr/local/bin/aria2c</string>
			<string>--conf-path=%s/etc/aria2.conf</string>
		</array>
		<key>RunAtLoad</key>
		<true/>
		<key>KeepAlive</key>
		<true/>
	</dict>
</plist>
''' % (homepath))

mpv_conf = open('%s/.config/mpv/mpv.conf' % homepath,'w')
mpv_conf.write('''\
sub-auto=fuzy
vo=opengl-hq:interpolation
autofit-larger=100%
autofit-smaller=100%
''')


shadowsocks_conf = open('%s/etc/shadowsocks.json' %homepath,'w')
shadowsocks_conf.write('''\
{
    "server":"%s",
    "server_port":%s,
    "local_port":1080,
    "password":"%s",
    "method":"%s",
    "timeout":300
}
''' % (shadowsocks_addr,shadowsocks_port,shadowsocks_key,shadowsocks_method))

shadowsocks_plist = open('%s/Library/LaunchAgents/shadowsocks.plist' % homepath,'w')
shadowsocks_plist.write('''\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
	<dict>
		<key>Label</key>
		<string>com.shadowsocks.app</string>
		<key>ProgramArguments</key>
		<array>
			<string>python</string>
			<string>%s/shadowsocks/shadowsocks/local.py</string>
			<string>-c</string>
			<string>%s/etc/shadowsocks.json</string>
		</array>
		<key>RunAtLoad</key>
		<true/>
	</dict>
</plist>
''' % homepath)
