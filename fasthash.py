#!/usr/bin/python3
import hashlib
import time

start_time = time.time()

file = open("hash.txt", 'r')
hashContainer = ""

for hash in file.readlines():
	hash = hash.strip('\n')
	# md5 hash all hash in every file line
	result = hashlib.md5(hash.encode())
	hashHex = result.hexdigest()
	#now concatenate the hash
	hashContainer += hashHex

#now print the concatenation hex string
#print("Hash Container: ", hashContainer)

#then print the hash of the hashContainer
newHash = hashlib.md5(hashContainer.encode())
newHashHex = newHash.hexdigest()
print("\nNew Generated Hash: ", newHashHex)

#prpgram execution time
print("\n\nProgram Execution time: ", (time.time() - start_time), " secs")

#print('\n\n\ninitial confirm result: 21906d6417e11481eaffa2968cbb31c4')
