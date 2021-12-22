import random
import string
# colors
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
# code
print (cyan+b+"""







████████╗███████╗███╗░░░███╗██████╗░
╚══██╔══╝██╔════╝████╗░████║██╔══██╗
░░░██║░░░█████╗░░██╔████╔██║██████╔╝
░░░██║░░░██╔══╝░░██║╚██╔╝██║██╔═══╝░
░░░██║░░░███████╗██║░╚═╝░██║██║░░░░░
░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚═╝░░░░░

███╗░░░███╗░█████╗░██╗██╗░░░░░
████╗░████║██╔══██╗██║██║░░░░░
██╔████╔██║███████║██║██║░░░░░
██║╚██╔╝██║██╔══██║██║██║░░░░░
██║░╚═╝░██║██║░░██║██║███████╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝






"""+b+cyan)

print (yellow+b+"              <===[[ coded by K34G2R8 ]]===>"+b+yellow)
print (" ")
print (gren+b+"        <---( Github-  KEAGTORB)--->"+b+gren)
print (" ")

def randomString(stringLength=6):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

email =  (randomString() + str(random.randint(1000,10000)) + "@kobrandly.com" )
print("Your random email is : "+email)