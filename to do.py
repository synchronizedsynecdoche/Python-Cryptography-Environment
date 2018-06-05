# perhaps make this leaner by passing the cipher as an argument instead
# of having 10000 files

# BUGS:
#   have ciphertype so only one file
#    must be a multiple of 16 unless stream cryptography has padding class
# Use bytes
#from SE:
my_str = "hello world"
bytes = str.encode(my_str)
type(bytes) # ensures its bytes
my_decoded_str = str.decode(bytes)
type(my_decoded_str) # ensures its string

#add bcrypt!

add checks because str.encode() in DecryptionRoutine is weird when being passed non-ASCII ciphertext , see CipherAES for what I think
is the fixed version

try using the thing=thing thing for function arguments for staging()
