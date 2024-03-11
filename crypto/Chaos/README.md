Writup for Chaos Challenge:

So first off, if we look at the code of the challenge, we can see that the challenge consists of ciphering the flag using an AES key and an IV, the IV is already given as a gift but we don't know the key yet.
Alright, now if we look at the key generation we can see that it is using the function getRandom() : 

def getRandom(bits, rounds):
    for _ in range(rounds):
        a = getrandbits(bits)
        print(f'{a}')
    a = getrandbits(bits)
    return a.to_bytes(32, 'little')

so this function takes a number of bits which is 256 in our case and a number of rounds which is 100 in our cas as an argument then it will generate 100 random numbers of 256 using the getrandbits function of the random module.
now we need to know 2 things here, the first thing is that in reality it generates 101 numbers, it will print 100 numbers and then will return the 101 th number which will be our key that we need to look for, and the second thing is that the getrandbits can be cracked using the rand crack module, but wait the randcrack module works with 32 bits numbers where it needs 624 numbers to recover the state and then can predict all the following numbers but here we generating 256 bits numbers.
so here we'll be using another module which is extend_mt19937_predictor and since it's 256 bits numbers we'll need this time 78 numbers because 256 is 32 * 8 and 624/8 equals 78 numbers.
alright, now we know everything, let's code.

first off we'll 

