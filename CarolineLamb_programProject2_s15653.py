#Programming Project 2
#Caroline Lamb
#5/28/2020

def echoes(sound, delay, num):
  soundLength = getNumSamples(sound)
  newLength = soundLength + (delay*num) #number of samples
  newSound = makeEmptySound(newLength, int(getSamplingRate(sound)))
  echoAmp = 1.0
  for echoCount in range(num+1):
    #60% smaller each time after the original sound
    for soundIndex in range(soundLength):
      newSoundIndex = soundIndex + (delay*echoCount)
      value1 = getSampleValueAt(sound, soundIndex) * echoAmp
      value2 = getSampleValueAt(newSound, newSoundIndex)
      setSampleValueAt(newSound, newSoundIndex, value1+value2)
    echoAmp = echoAmp * .6
  return newSound

#takes a python list of numbers, and a sampling rate
#and returns a sound object
def listToSound(list, samplingRate):
  newSound = makeEmptySound(len(list), int(samplingRate))
  for pos in range(getNumSamples(newSound)):
    setSampleValueAt(newSound, pos, list[pos])
  return newSound
  
def normalize(sound):
  newSound = duplicateSound(sound)
  #find the largest sample value
  largest = 0
  for s in getSamples(newSound):
    largest = max(largest, abs(getSampleValue(s)))
  #compute the multiplication factor
  factor = 32767.0/largest
  #change the sample values
  for s in getSamples(newSound):
    value = getSampleValue(s)
    setSampleValue(s, value * factor)
  return newSound
  
#blend two sounds together, rescaling the resulting sound if necessary 
#to avoid clipping
def blendSoundsNoClipping(sound1, sound2):
  if getSamplingRate(sound1) != getSamplingRate(sound2):
    print "Error! Sounds must have the same sampling rate."
    return
  minLength = min(getNumSamples(sound1), getNumSamples(sound2))
  newSoundList = [0.0] * minLength
  #now add the sample values of the two sounds together,
  #placing the result in newSoundList
  for pos in range(minLength):
    samp1 = getSampleValueAt(sound1, pos)
    samp2 = getSampleValueAt(sound2, pos)
    newSoundList[pos] = samp1 + samp2
  maxVal = max(newSoundList) #calculate the maximum sample value
  if maxVal > 32767: 
    normalize(newSoundList)
  sampRate = getSamplingRate(sound1)
  newSound = listToSound(newSoundList, sampRate)
  return newSound

def copySoundInto1(sound, tape, startIndex):
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
  
#copy sound into dest at startIndex.  A new sound is returned (dest is not modified).
def copySoundInto(sound, dest, startIndex):
  if not isinstance(sound, Sound):
      print "copySoundInto(sound, dest, startIndex): First parameter is not a sound"
      raise ValueError
  if not isinstance(dest, Sound):
      print "copySoundInto(sound, dest, startIndex): Second parameter is not a sound"
      raise ValueError
  newSound = duplicateSound(dest)
  sound.copySoundInto(newSound, startIndex)
  return newSound

#This function gradually decreases the volume of a sound by thirds.
def gradualDecrease(sound):
  newSound = duplicateSound(sound)
  numSamples = getNumSamples(newSound)
  #decrease volume of 1st 3rd by 30%
  for index in range(numSamples/3):
    value = getSampleValueAt(newSound, index)
    setSampleValueAt(newSound, index, value * 0.70)
  #decrease volume of 2nd 3rd by 60%
  for index in range(numSamples/3, numSamples * 2/3):
    value = getSampleValueAt(newSound, index)
    setSampleValueAt(newSound, index, value * 0.40)
  #decrease volume of last 3rd by 90%
  for index in range(numSamples * 2/3, numSamples):
    value = getSampleValueAt(newSound, index)
    setSampleValueAt(newSound, index, value * 0.10)
  return newSound
  
def increaseAndDecrease(sound):
  newSound = duplicateSound(sound)
  numSamples = getNumSamples(newSound)
  # double volume in first half
  for index in range(numSamples/2):
    value = getSampleValueAt(newSound, index)
    setSampleValueAt(newSound, index, value * 2)
  # decrease the volume of second half by 40%
  for index in range(numSamples/2, numSamples):
    value = getSampleValueAt(newSound, index)
    setSampleValueAt(newSound, index, value * 0.60)
  # return the new sound
  return newSound

def collage(sound1, sound2, sound3):
  gradualDecreaseSound1 = gradualDecrease(sound1)
  blendedSound1And2 = blendSoundsNoClipping(sound1, sound2)
  echoBlendedSounds = echoes(blendedSound1And2, (getNumSamples(blendedSound1And2) * 1/2), 3)
  increasedAndDecreaseSound3 = increaseAndDecrease(sound3)
  sound1NumSamples = getNumSamples(sound1)
  sound2NumSamples = getNumSamples(sound2)
  sound3NumSamples = getNumSamples(sound3)
  numSams1 = getNumSamples(gradualDecreaseSound1)
  numSamps2 = getNumSamples(blendedSound1And2)
  numSamps3 = getNumSamples(echoBlendedSounds)
  numSamps4 = getNumSamples(increasedAndDecreaseSound3)
  newSoundLength = (numSamps3 + numSamps2 + numSams1 + numSamps4 + sound3NumSamples + sound2NumSamples + sound1NumSamples)
  newSound = makeEmptySound(newSoundLength)
  newSound = copySoundInto(sound1, newSound, 0)
  newSound = copySoundInto(sound2, newSound, (sound1NumSamples -1))
  newSound = copySoundInto(sound3, newSound, (sound1NumSamples + sound2NumSamples -2))
  newSound = copySoundInto(gradualDecreaseSound1, newSound, (sound3NumSamples + sound2NumSamples + sound1NumSamples -3))
  newSound = copySoundInto(blendedSound1And2, newSound, (numSams1 + sound3NumSamples + sound2NumSamples + sound1NumSamples -4))
  newSound = copySoundInto(echoBlendedSounds, newSound, (numSamps2 + numSams1 + sound3NumSamples + sound2NumSamples + sound1NumSamples -5))
  newSound = copySoundInto(increasedAndDecreaseSound3, newSound, (numSamps3 + numSamps2 + numSams1 + sound3NumSamples + sound2NumSamples + sound1NumSamples -6) )
  return newSound