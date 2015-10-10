print "--------------------------------------------------------------------------"
print "Welcome to the English to Pyglatin translator."
print 'Translate any English word by entering it below. To exit, either answer "no" after entering text, or simply enter "quit" '
pyg = "ay" 
import sys
done = False
while done == False:

	original = raw_input('Enter a word:') 

	if original == "quit":
		print "------------------------------------------------------------------------------------"
		sys.exit("GoodBye")
	elif len(original) > 0 and original.isalpha():
    		word = original.lower() 
    		first = word[0] 
    
    		if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
        		new_word = word + pyg 
        		print new_word.upper()[0] + new_word[1:] 

		else: 
        		new_word = word[1:] + word[0] + pyg
        		print new_word.upper()[0] + new_word[1:]
   		 
	else: 
    		print 'The given word was not in English.'
    		print 'The likely error was that you used a numerical character; Try again with all alphabetical characaters.'
    	print "------------------------------------------------------------------"
	tryAgain = raw_input('Would you like to translate another word? Yes/No')
	
	if (tryAgain == 'Y' or tryAgain == "Yes" or tryAgain == "yes" or tryAgain == "y" or tryAgain == ' Y' or tryAgain == " Yes" or tryAgain == " yes" or tryAgain == " y"):
		done = False
	else:
		done = True


