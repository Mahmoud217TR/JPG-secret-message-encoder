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

# appending data after image data
def addOnImage(data,string):
    data += string.encode('utf-8')
    return data

# writing a new image
def writeNewImage(url,data):
    try:
        if url[-4:] != '.jpg':
            url+='.jpg'
        new = open(url, 'wb')
        new.write(data)
    except:
        print('Failed to write a new Image!')


if __name__ == '__main__':
    ogURL = input('Enter the jpg photo name: ')
    data = getImage(ogURL)
    addedData = input('Enter the Encoded Data: ')
    newData = addOnImage(data, addedData)
    newURL = input('Enter the new jpg photo name & path: ')
    writeNewImage(newURL, newData)