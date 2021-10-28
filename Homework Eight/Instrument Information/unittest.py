from main import StringInstrument

def testPassed(testFeedback):
    myStringInstrument = StringInstrument('Guitar', 'Schecter', 2011, 1200, 6, 24)
    numStrings = myStringInstrument.numStrings

    if numStrings == 6:
        testFeedback.write('numStrings correctly set in constructor')
        return True
    else:
        testFeedback.write('numStrings incorrect!!')
        testFeedback.write('incorrect number returned: ') + str(numStrings)
        return False