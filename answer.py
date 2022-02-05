en = open("en5", 'r').read().split()	
correct = [None, None, None, None, None]
yellow = []
guess = []
prev_tries = []
no = []
checker = []
for i in range(6):
	print("Enter the word entered")
	word = str(input())
	print("Enter letters in green, seperate using space")
	green = str(input()).split()
	prev_tries.append(word)
	rank = 0
	for i in green:
		if word.count(i) > 1:
			print(f"Please enter the location of the letter {i.upper()} in green")
			index = int(input())
			correct[index-1] = i
		elif i not in word:
			print(f"{i.upper()} is not there in the word, it will be ignored")
		else:
			correct[word.index(i)] = i 
	print("Please enter letters in yellow, seperate using space")
	yellown = str(input()).split()
	for i in yellown:
		if i not in word:
			print(f"{i.upper()} is not in the word, it will be ignored")
		else:
			yellow.append(i)
	for i in word:
		if i not in green and i not in yellow:
			no.append(i)
	used = yellow + green + no
	used = list(set(used))
	for i in en:
		add = True
		for j in yellow:
			if j not in i:
				add = False
		for n, j in enumerate(correct):
			if not j == None:
				if not correct[n] == i[n]:
					add = False
		for j in no:
			if j in i:
				add = False
		for j in prev_tries:
			for k in yellow:
				if k in j:
					checker.append(k)
			for k in checker:
				try:
				
					if j.index(k) == i.index(k):
						add = False
				except:
					pass
			checker = []
				 
		if add:
			guess.append(i)
	goodtry = []
	if len(guess) < 40:
		print("The following may be the word", end = "")
		print(guess)
	else:
		print("too many guesses")
	for i in en:
		for j in used:
			rank += i.count(j)
		if rank == 0:
			goodtry.append(i)
		rank = 0
	print("these are good tries:", end = "")
	print(goodtry[1:11])
	print("if you still want guesses, press y and enter")
	i = str(input())
	if i.lower() == "y":
		print(guess)			
				
	guess = []
	yellown = []
	green = []
	
