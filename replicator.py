#!/usr/bin/env python

def goodPython(stringthing):
    i = 0
    combination = ""
    for l in stringthing:
        combination += l.upper()+(l.lower()*i)
        if i == len(stringthing) - 1: return combination
        combination += "-"
        i = i + 1

def badPython(stringthing):
    theLengthOfTheString = 0
    combination = ""
    for letter in stringthing:
        theLengthOfTheString = theLengthOfTheString + 1
    for number in range(theLengthOfTheString):
        letter = stringthing[number]
        # Checks to see if the letter equals "o" or not. If it does not it'll go on to the next elif check.
        if letter == "o" or letter == "O":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "O"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "o" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        # Checks to see if the letter equals "e" or not. If it does not it'll go on to the next elif check.
        elif letter == "e" or letter == "E":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "E"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "e" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "v" or letter == "V":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "V"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "v" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "h" or letter == "H":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "H"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "h" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "q" or letter == "Q":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "Q"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "q" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "a" or letter == "A":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "A"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "a" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "s" or letter == "S":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "S"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "s" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "d" or letter == "D":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "D"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "d" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "b" or letter == "B":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "B"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "b" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "r" or letter == "R":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "R"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "r" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "z" or letter == "Z":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "Z"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "z" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "g" or letter == "G":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "G"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "g" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "c" or letter == "C":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "C"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "c" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "p" or letter == "P":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "P"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "p" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "i" or letter == "I":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "I"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "i" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "y" or letter == "Y":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "Y"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "y" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "t" or letter == "T":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "T"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "t" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "j" or letter == "J":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "J"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "j" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "n" or letter == "N":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "N"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "n" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "l" or letter == "L":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "L"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "l" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "f" or letter == "F":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "F"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "f" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "m" or letter == "M":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "M"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "m" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "x" or letter == "X":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "X"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "x" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "u" or letter == "U":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "U"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "u" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "w" or letter == "W":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "W"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "w" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"
        elif letter == "k" or letter == "K":
            # Here it adds the capital version of the letter to the combination.
            combination = combination + "K"
            # Here it decalres the string following as the letter multiplied with the amount of iterations that has happend up until this point.
            followingString = "k" * number
            # Here it adds everything together.
            combination = combination + followingString
            # If the iteration muber is equal to the theLengthOfTheString-1, it'll jump out, since it knows its at the end.
            if number == theLengthOfTheString-1:
                # Returns the finished combination of words.
                return combination
            # If not it'll just add a hyphen at the end of the current letter string.
            else:
                combination = combination + "-"

print(goodPython("aabBde"))
print(badPython("aabBde"))
