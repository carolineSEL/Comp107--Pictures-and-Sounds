#Simple Picture Manipulation
##Author: Caroline Lamb
##Date: 4/11/2020

###Description
This script, written in Jython, provides a collection of functions for basic image manipulation. These functions allow users to alter color properties, apply various effects like grayscale and sunset, and create specific color tints in images.

###Functions
changeRed(picture, multiplier): Alters the red value in an image based on the provided multiplier.
changeBlue(picture, multiplier): Modifies the blue value in an image according to the specified multiplier.
changeGreen(picture, multiplier): Changes the green value in an image as per the given multiplier.
makeSunset(picture, multiplier): Creates a sunset effect by modifying blue and green values.
negative(picture): Generates a negative of the given image.
grayscale(picture): Converts the image to grayscale.
weightedGrayScale(picture): Applies a weighted grayscale effect on the image, considering human eye perception.
purpleEffect(picture): Applies a purple tint to the image.
greenTint(picture): Converts the image to a green tint.
Usage
To use these functions in Jython, you need to have an image file to manipulate. The script uses Jython-specific functions like makePicture() and pickAFile() to select and load an image. Example usage is as follows:

myPict = makePicture(pickAFile())
newPict = changeRed(myPict, 0.75)
show(newPict)

###Requirements
Jython Environment: This script is specifically designed for Jython, a Java implementation of Python, which can easily integrate with Java libraries and environments.
An image processing toolkit compatible with Jython.
Installation
Ensure Jython is installed and properly set up in your environment. There is no additional installation required if the necessary Jython image processing toolkit is already in place.

###Note
This script is intended for educational purposes and demonstrates basic image manipulation techniques using Jython.

###License
This project is open-source and available for all users.
