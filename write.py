# writing a new image
def writeNewImage(url,data):
    try:
        if url[-4:] != '.jpg':
            url+='.jpg'
        new = open(url, 'wb')
        new.write(data)
    except:
        print('Failed to write a new Image!')
