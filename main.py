import random
placeHolder ="[name]"
Result ="[result]"
scorepoint ="[score]"

with open("./Input/Names/StudentsNames.txt") as names_file:
    names = names_file.readlines()
    print(names)
with open("./Input/Letters/Starting_Letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        r = random.randint(40, 100)
        printingResult = ""
        if r < 50:
            printingResult = "Failed"
        else:
            printingResult = "passed"

        stripper = name.strip()
        newLetter = letter.replace(placeHolder,stripper)
        newScore = newLetter.replace(scorepoint,str(r))
        newResult =newScore.replace(Result,printingResult)
        #print(newResult)
        with open(f"./Output/ReadyToSend/letter_for{stripper}.dox",mode="w") as completed:
            completed.write(newResult)