import re

# to get the original image if there is another secret message in it
def getImage(url):
    try:
        h = open(url, 'rb')
        data = h.read().hex()
        r = re.search('ffd9', data)
        end = r.span()[1]
        return (bytes.fromhex(data[:end]))
    except:
        print("Couldn't read File: File not Found or Image Corrupted!")
        exit(-1)