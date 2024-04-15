def searchpincode(fname):
    
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
    

    pincode1=577228
    while(pincode1!="0"):
        pincode1=input("Enter pincode: ")
        if pincode1=="0":
            break
        position1=pincodes.index(pincode1)
        location1=locations[position1]
        district1=districts[position1]
        state1=states[position1]
        s2=pincode1+","+location1+","+district1+","+state1
        print(s2)
        
    
searchpincode("Pincode_30052019.csv")
