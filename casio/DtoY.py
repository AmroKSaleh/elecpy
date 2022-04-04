transType = int(input("D To Y 0|Y To D 1"))

if transType:
    # Y to D
    print("Draw a Y shape")
    r1 = float(input("left   \ R1:"))
    r2 = float(input("right  / R2:"))
    r3 = float(input("bottom | R3:"))

    print("Draw upside triangle")
    # calculate r
    ra = ((r1*r2)+(r2*r3)+(r1*r3))/(r1)
    rb = ((r1*r2)+(r2*r3)+(r1*r3))/(r2)
    rc = ((r1*r2)+(r2*r3)+(r1*r3))/(r3)

else:
    # D to Y
    print("Draw upside triangle")
    ra = float(input("right / Ra:"))
    rb = float(input("left  \ Rb:"))
    rc = float(input("top   - Rc:"))

    print("Draw a Y shape")
    # calculate r1, r2, r3 from ra, rb, rc
    r1 = (rb*rc)/(ra+rb+rc)
    r2 = (ra*rc)/(ra+rb+rc)
    r3 = (ra*rb)/(ra+rb+rc)

print("R1 lt \ in Y",r1,sep="")
print("R2 rt / in Y",r2,sep="")
print("R3 btm | in Y",r3,sep="")

print("Ra rt / in D",ra,sep="")
print("Rb lt \ in D",rb,sep="")
print("Rc tp - in D",rc,sep="")
