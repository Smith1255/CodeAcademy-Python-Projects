print "        ---------------------------------------------       "
print "Welcome to the English to Pyglatin translator."
print "To translate any word into Pyglatin, enter any English word."
pyg = "ay" 
original = raw_input('Enter a word:') 


if len(original) > 0 and original.isalpha():
    word = original.lower() 
    first = word[0] 
    
    if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
        new_word = word + pyg 
        print new_word.upper()[0] + new_word[1:] 
        done = False
    else: 
        new_word = word[1:] + word[0] + pyg
        print new_word.upper()[0] + new_word[1:]
	done = False
    
    
else: 
    print 'The given word was not in English.'
    print 'The likely error was that you used a numerical character; Try again with all alphabetical characaters.'
    


    done = True
    while True:
        print "    --------------------------     "
	pyg = "ay" 
        original = raw_input('Enter a word:') 


        if len(original) > 0 and original.isalpha():
            word = original.lower() 
            first = word[0] 
    
            if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
                new_word = word + pyg 
                print new_word.upper()[0] + new_word[1:] 
		done = False
        
            else: 
                new_word = word[1:] + word[0] + pyg
                print new_word.upper()[0] + new_word[1:]
		done = False
    
    
        else: 
            print 'The given word was not in English.'
            print 'The likely error was that you used a numerical character; Try again with all alphabetical characaters.'
