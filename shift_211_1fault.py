import re


#file to apply a shift to the coordinate section of a .cif file

#ask for name of text file here:

infilename=input("Enter name of text file not cif file: ")
print("Opening "+ infilename)

infile=open(infilename,"rt")

#make the filename of the output

outfilename=f"shifted211_{infilename}"

#open the output file for writing

outfile=open(outfilename,"wt")

print("Output file will be called "+ outfilename)

#Now go through the input file line by line doing things to it
#first define things that are always the same

#unit cell parameters
#unita=7.3328
#unitc=4.145
#supercell size in multiple of TiBe12 cell scm x scm x scm
scmx=16.0
scmy=16.0
scmz=16.0
safety=0.277/(2*scmx)
#safety margin of half distance from twin plane to next layer of atoms to make it not a disaster when floats are rounded
faultline=2.0

faultsafe=faultline+safety

for thisline in infile:
    #that already read the line

    #understand the line
    numberpattern=r'[0-9]\.[0-9]+'
    firstnumber=re.search(numberpattern,thisline)
    lastboring=firstnumber.start()-1
    #lastboring is the position in the line where the stuff that isn't numbers ends
    
    numbersection=re.findall(numberpattern,thisline)

    #print("Read a line \n")
    
    occupancy=numbersection[0]
    xcoord=float(numbersection[1])
    ycoord=float(numbersection[2])
    zcoord=float(numbersection[3])

    

    #print(f"Occupancy is {occupancy}\n")
    #print(f"xcoord is {str(xcoord)}\n")
    #print(f"ycoord is {str(ycoord)}\n")
    #print(f"zcoord is {str(zcoord)}\n")

    checker=(2.0*xcoord)+ycoord+zcoord
    

    if checker<=(faultsafe):
    #if checker <= bottomsafe:
        #print("Found a line to leave in place\n")
        outfile.write(thisline)
    #write it as is
    elif checker >(faultsafe):
        #make the new numbers
        newxcoord=xcoord
        newycoord=ycoord-(0.5/scmy)
        newzcoord=zcoord+(0.5/scmz)
        #print("Found a line to shift\n")
        #print(f"New xcoord is {str(newxcoord)}\n")
        #print(f"New ycoord is {str(newycoord)}\n")
        #print(f"New zcoord is {str(newzcoord)}\n")
        #now check it is inside the supercell
        if newxcoord < 1.0 and newycoord < 1.0 and newzcoord < 1.0:

            newxstring=str(newxcoord)
            newystring=str(newycoord)
            newzstring=str(newzcoord)
            
            newlinestring=f"{thisline[0:lastboring]}  {occupancy}  {newxstring}  {newystring}  {newzstring}\n"
            #print("Its new position is inside the supercell\n")
        
            #write its shifted position
            outfile.write(newlinestring)
        else:
            #don't put it in
            continue
            #print("Its new position was outside the supercell\n")

infile.close()
outfile.close()

    #when we have got out of the for loop, close both files
