is_waiting = True
has_time = False
has_time2 = True

# the first condition must be an "if"!

if is_waiting: # Don't forget the colon! (:)
    print("I am waiting") # dont forget the indentation. Simply press "tab"
    print("I am still waiting")
    print("I am still waiting")
elif has_time: # elif stands for "else if". When the first "if" condition is false, the following "elif" condition is checked
    print("I have time")
elif has_time2: # you can set up more than one elif condition
    print("I am waiting too")
else: # if none of the previous conditions were true, the "else" clause is executed
    print("I am not waiting")

print("Done")


if "Hallo" == "Hello":
    print("same word")
else:
    print("different word")

if "Hallo" != "Hello":
    print("same word")
else:
    print("different word")

if "Hallo"     != "Hello":
    # platzhalter für einrückungen nach doppelpunkten
    pass
else:
    print("different word")