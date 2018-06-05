
import argparse

class kwargParse(object):


	def argspawn(self):

        global p
        p = argparse.ArgumentParser()
	
		p.add_argument('-c','--cipher', type=str, nargs='+', help="Cipher argument")
		p.add_argument('-l','--key-length',type=int,nargs='+',help="Choose a key length [128,192,256]")
        p.add_argument('-r','--use-dev-random',help="Force /dev/random as the entropy pool")
		p.add_argument('-u','--use-dev-urandom',help="Force /dev/urandom as the entropy pool")
		p.add_argument('-m','--mode-of-operation',type=str,nargs='+',help="Specify mode of operation")
		p.add_argument('-v','--verbose',help="Be verbose")
		p.add_argument('-s','--security-considerations',help="Print security recommendations")
		p.add_argument('-D','--debug',help="Print debug information")
		p.add_argument('-e','--encrypt',help="Encrypt")
		p.add_argument('-d','--decrypt',help="Decrypt")
		p.add_argument('-M','--message',type=str,nargs='+',help="Pass the message to encrypt as an argument, mainly for debugging purposes, and not safe")
		p.add_argument('-P','--pbkdf',type=str,nargs='+',help="Force PBKDF2 as the key derivation algorithm")
		p.add_argument('-S','--sha', help="Force SHA1 as the key derivation algorithm")
		p.add_argument('-i','--interactive',help="Drops to an interacive shell-like environment")
		p.add_argument('-h','--help',help="Print this message")
		p.add_argument('-k','--key',help="Pass the key as an argument, mainly for debugging purposes, and not safe")


		a = p.parse_args()

	
