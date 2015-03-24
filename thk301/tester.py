#!/usr/bin/py
#!/usr/bin/py

def mysT(thisL):
    if thisL ==thisL[::-1]:
        return 0
    else:
        counter=0
        while thisL!=thisL[::-1]:
            if thisL[thisL.index("c")+1:]=="d":
                thisL[thisL.index("c")+1:]=="c"
                counter=counter+1
            elif thisL[thisL.index("c")+1:]=="c":
                thisL[thisL.index("c")+1:]=="b"
                counter=counter+1
            elif thisL[thisL.index("c")+1:]=="b":
                thisL[thisL.index("c")+1:]=="a"
                counter=counter+1
    return counter





thisL="abcd"
print mysT(thisL)