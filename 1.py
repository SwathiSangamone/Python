def searchpincode(fname):#this function hepls to get the details of pincode
    
    f1=open(fname,"r")
    locations=[]
    pincodes=[]
    districts=[]
    states=[]
    s1=f1.readline()
    for i in range(0,5,1):
        s1=f1.readline().replace("\n","")
        list1=s1.split(",")
        locations.append(list1[3])
        pincodes.append(list1[4])
        districts.append(list1[7])
        states.append(list1[8])
    pincode1=input("Enter pincode: ")
    position1=pincodes.index(pincode1)
    location1=locations[position1]
    district1=districts[position1]
    state1=states[position1]
    s2=pincode1+","+location1+","+district1+","+state1
    print(s2)
searchpincode("Pincode_30052019.csv")
