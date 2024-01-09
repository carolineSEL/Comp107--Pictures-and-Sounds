#Lab 6: Splicing Sounds
#Caroline Lamb
#5/12/2020

def copySoundInto(sound, tape, startIndex):
  newTape = duplicateSound(tape)
  newSound = duplicateSound(sound)
  numSamples = getNumSamples(newSound)
  tapeSamples = getNumSamples(newTape)
  #copies as much of the sound as there is room for on the tape
  soundToCopy = min(numSamples, tapeSamples-startIndex)
  targetIndex = startIndex
  #copies original sound from beginning to end of the tape
  for sourceIndex in range(0, soundToCopy):
    sourceSamp = getSampleValueAt(newSound, sourceIndex)
    setSampleValueAt(newTape, int(sourceIndex + startIndex), sourceSamp)
    sourceIndex = sourceIndex + 1
  return newTape
    
def copySoundIntoAtSec(sec):
  sound = makeSound(pickAFile())
  tape = makeSound(pickAFile())
  rate = getSamplingRate(sound)
  sec = rate/sec
  newSound = copySoundInto(sound,tape,sec)
  return newSound 
  
def reverse(sound):
  #create a new empty sound with same # of samples and
  #sampling rate as the original sound
  newSound = makeEmptySound(getNumSamples(sound), int(getSamplingRate(sound)))
  #set up index to start at end of new sound
  newIndex = getNumSamples(newSound) - 1
  #loop through original sound, setting values in new sound
  for index in range(getNumSamples(sound)):
    value = getSampleValueAt(sound, index)
    setSampleValueAt(newSound, newIndex, value)
    newIndex = newIndex - 1
  #return the new sound
  return newSound
  
def forwardAndReverse(sound):
  #make new sound with twice as many samples and the same sampling rate
  numSamples = getNumSamples(sound)
  samplingRate = int(getSamplingRate(sound))
  newSound = makeEmptySound(numSamples * 2, samplingRate)
  numSamplesTape = getNumSamples(newSound)
  #make reversed version of sound
  reversedSound = reverse(sound)
  #copy original sound into empty sound
  index = 0
  newSound = copySoundInto(sound, newSound, index)
  newSound = copySoundInto(reversedSound, newSound, numSamples - index)
  return newSound