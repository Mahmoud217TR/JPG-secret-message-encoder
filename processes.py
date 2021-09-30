from read import getImage,getMessage
from add import addOnImage
from write import writeNewImage

def write():
    ogURL = input('Enter the jpg photo name: ')
    data = getImage(ogURL)
    addedData = input('Enter the Encoded Data: ')
    newData = addOnImage(data, addedData)
    newURL = input('Enter the new jpg photo name & path: ')
    writeNewImage(newURL, newData)

def read():
    print(getMessage('tst.jpg'))