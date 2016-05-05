import sys # Import "sys" Python library.
# import signal # Import "signal" Python library. I don't know why I imported this library, though. lol

while True: # While the invisible variable is true, do this stuff:
	
	print """
	 .---. .-. .-..----.   .----..-. .-. .---. .----..-.  .-..----.  .---. .-. .----. .-. .-.   .----..-..-.  .----.
	{_   _}| {_} || {_     | {_  |  `| |/  ___}| {}  }\ \/ / | {}  }{_   _}| |/  {}  \|  `| |   | {_  | || |   | {_  
	  | |  | { } || {__    | {__ | |\  |\     }| .-. \ }  {  | .--'   | |  | |\      /| |\  |   | |   | || `--.| {__ 
	  `-'  `-' `-'`----'   `----'`-' `-' `---' `-' `-' `--'  `-'      `-'  `-' `----' `-' `-'   `-'   `-'`----'`----
	""" # Print the title of the file. :) Also, triple-quoting allows strings to go across lines.
	
	print "[!] No UTF-8 Encoding Enabled [!]" # There is no UTF-8 encoding enabled, so tell script runners that.
	
	# letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # All the letters in the English alphabet.
	
	invalidchars = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", "\\\\", "|", ";", ":", "'", '"', ",", "<", ".", ">", "/", "?"] # Invalid characters that we will NOT allow in the key. The \\\\ value is a normal \ because \ is an escape key if not indicated otherwise.
	
	message = raw_input("Message:") # The message you would like to encrypt. The script runner will input their message.
	
	print "Your message is '" + message + "'." # This tells you what your message is.
	
	key = raw_input("Key:") # The key that you would like to encrypt your message with. The script runner will input their message.
	
	if key in invalidchars: # If any characters match any character in the invalid characters array defined above, do this stuff:
	
		print "Invalid character in key: '" + key + "'" # Tell the script runner that he has an invalid character in his key.
		print "l22" # for debugging purposes
		print "                           " + key.index(invalidchars) # Tell the script runner where the problem is. *currenly debugging*
		print "l24" # for debugging purposes
		
		
	keylen = str(key) # keylen = key lenGTH; Turn the variable key into a string and make the result the value of the variable keylen.
	
	if key[0] in letter:
		
		if key[0] in letter[0]:
			
			nkey = str(1) + key[1:]
		
		if key[0] in letter[1]:
			
			nkey = str(2) + key[1:]
		
		if key[0] in letter[2]:
			
			nkey = str(3) + key[1:]
		
		if key[0] in letter[3]:
			
			nkey = str(4) + key[1:]
		
		if key[0] in letter[4]:
			
			nkey = str(5) + key[1:]
		
		if key[0] in letter[5]:
			
			nkey = str(6) + key[1:]
		
		if key[0] in letter[6]:
			
			nkey = str(7) + key[1:]
		
		if key[0] in letter[7]:
			
			nkey = str(8) + key[1:]
		
		if key[0] in letter[8]:
			
			nkey = str(9) + key[1:]
		
		if key[0] in letter[9]:
			
			nkey = str(10) + key[1:]
		
		if key[0] in letter[10]:
			
			nkey = str(11) + key[1:]
		
		if key[0] in letter[11]:
			
			nkey = str(12) + key[1:]
		
		if key[0] in letter[12]:
			
			nkey = str(13) + key[1:]
		
		if key[0] in letter[13]:
			
			nkey = str(14) + key[1:]
		
		if key[0] in letter[15]:
			
			nkey = str(16) + key[1:]
		
		if key[0] in letter[16]:
			
			nkey = str(17) + key[1:]
		
		if key[0] in letter[17]:
			
			nkey = str(18) + key[1:]
		
		if key[0] in letter[18]:
			
			nkey = str(19) + key[1:]
		
		if key[0] in letter[19]:
			
			nkey = str(20) + key[1:]
		
		if key[0] in letter[20]:
			
			nkey = str(21) + key[1:]
		
		if key[0] in letter[21]:
			
			nkey = str(22) + key[1:]
		
		if key[0] in letter[22]:
			
			nkey = str(23) + key[1:]
		
		if key[0] in letter[23]:
			
			nkey = str(24) + key[1:]
		
		if key[0] in letter[24]:
			
			nkey = str(25) + key[1:]
		
		if key[0] in letter[25]:
			
			nkey = str(26) + key[1:]
