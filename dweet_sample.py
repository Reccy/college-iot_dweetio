import fcntl, socket, struct, dweepy, time, platform, random

def getTemp():
    return random.randint(1,1000)
    
def getHumidity():
    return 10
    
def getOS():
    return platform.platform()
    
# from http://stackoverflow.com/questions/159137/getting-mac-address
def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])

def post(dic):
    thing = 'sample_thing_27856856398256986587921635'
    print dweepy.dweet_for(thing, dic)
    
def getReadings():
    dict = {}
    dict["temperature"] = getTemp();
    dict["mac-address"] = getHwAddr('eth0')
    dict["humidity"] = getHumidity()
    dict["operating system"] = getOS()
    return dict

while True:
    dict = getReadings();
    post(dict)
    time.sleep(5)
