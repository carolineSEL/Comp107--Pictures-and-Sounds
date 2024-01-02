#Lab: Simple Picture MAnipulation
#Caroline Lamb
#4/11/2020

#This function changes the red values in a picture by the amount specified by the "multiplyer" parameter.
def changeRed(picture,multiplyer):
#"picture" parameter represents the picture that is being manipulated, "multiplyer" represents amount color values are being changed by.
  newPict = duplicatePicture(picture)
  #gets all pixels and changes the red values for each.
  for px in getAllPixels(newPict):
    value = getRed(px)
    setRed(px, value * multiplyer)
  return newPict
#To call function ex.: myPict = makePicture(pickAFile()) ,  newPict = changeRed(myPict,.75) , show(myPict)

#This function changes the blue values in a picture by the amount specified by the "multiplyer" parameter.
def changeBlue(picture,multiplyer):
  newPict = duplicatePicture(picture)
  #Gets all pixels and changes the blue values
  for px in getAllPixels(newPict):
    value = getBlue(px)
    setBlue(px, value * multiplyer)
  return newPict

#This funtion changes the green values in a picture by the amount specified by the "multiplyer" parameter.
def changeGreen(picture, multiplyer):
  newPict = duplicatePicture(picture)
  #gets all pixels and changes the green value of the pixels by "multiplyer" amount.
  for px in getAllPixels(newPict):
    value = getGreen(px)
    setGreen(px, value * multiplyer)
  return newPict

#This function creates a sunset effect.
def makeSunset(picture,multiplyer):
  pict = changeBlue(picture,multiplyer)
  newPict = changeGreen(pict,multiplyer)
  return newPict
#To call function: myPict = makePicture(pickAFile()) , newPict = makeSunset(myPict,0.70) , show(newPict)

#This function creates a negative image 
def negative(picture):
  newPict = duplicatePicture(picture)
  #changes pixel values to be negative values
  for px in getAllPixels(newPict):
    rvalue = getRed(px)
    gvalue = getGreen(px)
    bvalue = getBlue(px)
    negColor = makeColor(255-rvalue, 255-gvalue, 255-bvalue)
    setColor(px, negColor)
  return newPict

#This function creates a grayscale version of an image 
def grayscale(picture):
  newPict = duplicatePicture(picture)
  #changes pixel values to grayscale.
  for px in getAllPixels(newPict):
    rvalue = getRed(px)
    gvalue = getGreen(px)
    bvalue = getBlue(px)
    intensity = (rvalue + gvalue + bvalue)/3
    newColor = makeColor(intensity, intensity, intensity)
    setColor(px, newColor)
  return newPict

def weightedGrayScale(picture):
  newPict = duplicatePicture(picture)
  for px in getAllPixels(newPict):
    newRValue = getRed(px) * 0.299
    newGValue = getGreen(px) * 0.587
    newBValue = getBlue(px) * 0.114
    luminance = newRValue + newGValue + newBValue 
    newColor = makeColor(luminance, luminance, luminance)
    setColor(px, newColor)
  return newPict

#This function makes an image appear purple.
def purpleEffect(picture):
  newPict = changeBlue(myPict,1.2)
  newPict2 = changeGreen(newPict,0.7)
  return newPict2
#To call function: myPict = makePicture(pickAFile()) , newPict = purpleEffect(myPict) , show(newPict)

#This finction turns an image entirely green.
def greenTint(picture):
  newPict = grayscale(picture)
  for px in getAllPixels(newPict):
    setGreen(px, 255)
  return newPict


  
  