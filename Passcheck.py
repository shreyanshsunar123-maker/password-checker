import re
import sys
import string
import Dict
import math

# Input password.
password = input("Please insert your password here: ")
pass_stren = 0
charset=0


# Check for invalid characters.
valid_char = string.ascii_letters + string.digits + string.punctuation +"" +" "
invalid_char = [c for c in password if c not in valid_char]
if invalid_char:
    print("Invalid characters detected:", "".join(invalid_char))
    sys.exit()


# Checkers.
def repitition_check(p):
    p = p.translate(str.maketrans("","",string.punctuation + " "))
    length = len(p)
    for size in range(1, length // 2 +1):
        if length%size == 0:
            chunk = p[:size]
            if chunk * (length // size)== p:
                return True
    return False


def sequence_check(p,length):
    for i in range(len(p)-length+1):
        segment_part = p[i:i+length]
        if all(ord(segment_part[j+1])-ord(segment_part[j]) == 1 for j in range (length -1)):
            return True
    return False


def common_words(p):
    cleaned = p.lower().translate(str.maketrans("","", string.punctuation + " "))
    for c in Dict.common_words:
        if c in cleaned:
            return True
    return False
    

def character_check(p):
    global pass_stren
    global charset
    if re.search(r"[a-z]", password):
        pass_stren += 0.5
        charset+=26
    else : print(" Use small case letter.")

    if re.search(r"[A-Z]", password):
        pass_stren += 0.5
        charset+=26
    else : print(" Use Large case letter.")

    if re.search(r"[0-9]", password):
        pass_stren += 0.5
        charset+=10
    else : print(" Use Numbers.")

    if re.search(r"[!@#$%^&*()_+\-\[\]{};':\"\\|,.<>/? ]", password):
        pass_stren += 0.5
        charset+=len(string.punctuation+" ")+1
    else : print(" Use Symbols.")

    if not re.search(r"(.)\1{3}", password): pass_stren += 0.5
    else: print("Don't use repetitive words.")



# Evaluate password strength.

if repitition_check(password): print(" Repetition not suggested.")
else: pass_stren+=1

if sequence_check(password, length=4): print(" Sequence is not allowed.")
else: pass_stren+=1

if common_words(password): print("Simple words not recommended.")
else: pass_stren+=1

if len(password)>=14:pass_stren +=1.5
elif len(password)>=8:pass_stren += 1
else:pass_stren+= 1

character_check(password)

# Calculate Entropy.
Entropy = len(password)*math.log2(charset)
if Entropy >= 60: pass_stren+=2
elif Entropy >=40: pass_stren+=1.5
else: pass_stren+=1

#Result.
if pass_stren>=8:print(f"Password Strength: {pass_stren}/10,\n Level: Excellent.")
elif pass_stren>=6:print(f"Password Strength: {pass_stren}/10,\n Level: Very Good.")
elif pass_stren>=4:print(f"Password Strength: {pass_stren}/10,\n Level: Good.")
elif pass_stren<4:print(f"Password Strength: {pass_stren}/10,\n level: poor. ")

