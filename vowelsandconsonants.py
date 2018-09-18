word=input()
vowels=['a','e','i','o','u']
consonants=['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
if(word in vowels):
	print("vowels")
elif(word in consonants):
	print("consonants")
else:
	print("invalid")
