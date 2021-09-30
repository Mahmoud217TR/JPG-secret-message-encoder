from read import getImage
from add import  addOnImage
from write import writeNewImage

if __name__ == '__main__':
    ogURL = input('Enter the jpg photo name: ')
    data = getImage(ogURL)
    addedData = input('Enter the Encoded Data: ')
    newData = addOnImage(data, addedData)
    newURL = input('Enter the new jpg photo name & path: ')
    writeNewImage(newURL, newData)