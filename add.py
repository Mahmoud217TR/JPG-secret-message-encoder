# appending data after image data
def addOnImage(data,string):
    data += string.encode('utf-8')
    return data
