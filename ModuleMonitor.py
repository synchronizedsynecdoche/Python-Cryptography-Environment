#add this somewhere 
                    #if fun: print "Dude weed lmao"

class Monitor(object):

    #make the inputhandler pass the which one, instead of the current spaghetti conditionals
    def Cipher(self, whichOne):
        
        if whichOne == "AES":
            
            print "Rijndael is the de-facto symmetric encryption " \
                  "algorithm. It takes a key of size 128, 192, or 256 " \
                  "bits. It operates on block sizes of 128 bits (unless" \
                  "using a stream cipher mode), and uses 10,12, or 14 rounds." \
                  "Additionally, it's standardization led to AES-NI, an x86 " \
                  "instruction set for optimization on newer hardware, yielding" \
                  "excellent performance even on low end hardware"

        elif whichOne = "Camellia":

    def Considerations(self):

        print "Python Cryptography Environment is a tool, and like " \
              "all tools, misuse can lead to undesirable results. Using" \
              "a single letter key will allow an attacker to simply guess/" \
              "brute force the key. Even with the strongest cipher, and the " \
              "strongest key derivation function, the entropy from the user " \
              "password is still important. Additionally, this tool has no way " \
              "of guaranteeing the secrecy of sensitive materials (key, plaintext) in memory," \
              "this is a limitation of python, it can not be fixed within this script," \
              "or in the cryptography module used. Always assume that your key continues" \
              "in memory until computer shutdown. The documentation for the module used" \
              "has a page outlining the severity of this issue" \
              "https://cryptography.io/en/latest/limitations/ ."

