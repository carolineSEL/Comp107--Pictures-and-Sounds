#Lab:Copying a Picture into a Bigger Picture and Scaling Pictures
#4/19/2020
#Caroline Lamb

#This function copies a picture into another picture
def copyInto(picture, canvas, upperLeftX, upperLeftY):
  newCanvas = duplicatePicture(canvas)
  pictureWidth = getWidth(picture)
  pictureHeight = getHeight(picture)
  canvasWidth = getWidth(newCanvas)
  canvasHeight = getHeight(newCanvas)
  #This only copies as much of the picture onto the canvas as there is room for.
  widthToCopy = min(pictureWidth, canvasWidth-upperLeftX)
  heightToCopy = min(pictureHeight, canvasHeight-upperLeftY)
  #copies however much of the picture as will fit over to the canvas edge
  targetX = upperLeftX
  for sourceX in range(widthToCopy):
    targetY = upperLeftY
    for sourceY in range(heightToCopy):
      #copies color of pixel at source location to target location.
      sourcePix = getPixel(picture, sourceX, sourceY)
      color = getColor(sourcePix)
      destPix = getPixel(newCanvas, targetX, targetY)
      setColor(destPix, color)
      targetY = targetY + 1
    targetX = targetX + 1
  return newCanvas
#Analysis Question: you could use this function to copy a picture onto another picture if the canvas is a picture.

#This function creates a new picture inside an empty one with the specified matte width.
def matte(picture,matteWidth,color):
  pictureWidth = getWidth(picture)
  pictureHeight = getHeight(picture)
  canvasWidth = (pictureWidth + matteWidth)
  canvasHeight = (pictureHeight + matteWidth)
  myCanvas = makeEmptyPicture(canvasWidth, canvasHeight, color)
  newPict = copyInto(picture,myCanvas,50,50)
  return newPict

#This function scales a picture to one quarter its original size.
#original width and height divided by two
def quarter(orig):
  newWidth = getWidth(orig)/2
  newHeight = getHeight(orig)/2
  #makes empty canvas to store new picture.
  newCanvas = makeEmptyPicture(newWidth, newHeight)
  #copy other pixels onto canvas
  for targetX in range(newWidth):
    for targetY in range(newHeight):
      color = getColor(getPixel(orig, targetX*2, targetY*2))
      setColor(getPixel(newCanvas, targetX, targetY), color)
  return newCanvas
  
#This function tiles a picture onto a canvas as many times as it can.
def tile(picture, canvas):
  for targetY in range(0, getHeight(canvas), getHeight(picture)):
    for targetX in range(0, getWidth(canvas), getWidth(picture)):
      canvas = copyInto(picture, canvas, targetX, targetY)
  return canvas
  
#this function quarters a picture 4 times and tiles it.
def tileWithQuarters(picture):
  canvas = makeEmptyPicture(getWidth(picture)*2, getHeight(picture)*2)
  newPict = duplicatePicture(picture)
  x = getWidth(picture)/2
  y = getHeight(picture)/2
  newPict2 = tile(newPict,canvas)
  return newPict2
