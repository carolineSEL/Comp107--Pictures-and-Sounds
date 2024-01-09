#Lab: Combining Pictures
#Caroline Lamb
#4/24/2020

#This function modifies a picture that has a subject in front of a green screen by replacing all of the green pixels with the color from the corresponding pixels in another picture.
def swapBack(pict, bg, newBg):
  newPict = duplicatePicture(pict)
  for y in range(getHeight(newPict)):
    for x in range(getWidth(newPict)):
      pxl = getPixel(newPict, x, y)
      bgpx = getPixel(bg, x, y)
      if (distance(getColor(pxl), getColor(bgpx)) < 110):
        setColor(pxl, getColor(getPixel(newBg, x, y)))
  return newPict
  
#This function modifies a picture that has a subject in front of a green screen by replacing all of the green pixels with the color from the correpsonding pixels in another picture.
def chromakey(pict, bg):
  newPict = duplicatePicture(pict)
  for y in range(getHeight(newPict)):
    for x in range(getWidth(newPict)):
      px = getPixel(newPict, x, y)
      #A definition of green
      if (getRed(px) > 80 and getBlue(px) > 80):
        #then grab the color at the same spot from the bg
        setColor(px, getColor(getPixel(bg, x, y)))
  return newPict

#This function blends two images by overlaying one picture with another.
def blendPictures(pict1, pict2, overlapAmt):
  width1 = getWidth(pict1)
  height1 = getHeight(pict1)
  width2 = getWidth(pict2)
  height2 = getHeight(pict2)
  #set up width and height for new canvas
  newWidth = width1 + width2 - overlapAmt
  newHeight = min(height1, height2)
  #create the canvas to hold the blended pictures
  newCanvas = makeEmptyPicture(newWidth, newHeight)
  #copy the first picture up to the overlap section
  for x in range(width1 - overlapAmt):
    for y in range(newHeight):
      color = getColor(getPixel(pict1, x, y))
      setColor(getPixel(newCanvas, x, y), color)
  #copy the blended section
  #50% pict1 and 50% pict2
  pict2_x = 0
  for pict1_x in range(width1 - overlapAmt, width1):
    for y in range(newHeight):
      pixel1 = getPixel(pict1, pict1_x, y)
      pixel2 = getPixel(pict2, pict2_x, y)
      newRed = 0.50 * getRed(pixel1) + 0.50 * getRed(pixel2)
      newGreen = 0.50 * getGreen(pixel1) + 0.50 * getGreen(pixel2)
      newBlue = 0.50 * getBlue(pixel1) + 0.50 * getBlue(pixel2)
      color = makeColor(newRed, newGreen, newBlue)
      setColor(getPixel(newCanvas, pict1_x, y), color)
    pict2_x = pict2_x + 1
  #copy the remaining section of pict2
  targetX = width1
  for x in range(overlapAmt, width2):
    for y in range(newHeight):
      color = getColor(getPixel(pict2, x, y))
      setColor(getPixel(newCanvas, targetX, y), color)
    targetX = targetX + 1
  return newCanvas
