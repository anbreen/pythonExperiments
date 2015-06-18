def pigTranslator(input):   
   pigEnd = input[0] + "ay";
   pigTranslated = input[1:] + pigEnd
   return pigTranslated

input = raw_input("Enter any word for the Pig Latin Translator")
if len(input) > 0 :
    print input + "Let's Continue"
    print pigTranslator(input)
else:
    print "String is Empty"

