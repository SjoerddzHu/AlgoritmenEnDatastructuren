import random


looping = True
hashed = dict()
listOfDoubles = list()
try: 
	while True:
		randomFloat = random.random()
		
		randomFloatHash = hash(randomFloat) % (2**32)

		if randomFloatHash in hashed.keys():
			print("Collision found")
			listOfDoubles.append([
				[hashed[randomFloatHash], randomFloat]
				,[randomFloatHash, hash(hashed[randomFloatHash]) % (2**32)]
			]) 	
		else:
			hashed[randomFloatHash] = randomFloat
except KeyboardInterrupt:
	for pair in listOfDoubles:
		hashes = pair[0]
		values = pair[1]
		print(hashes, values)