f1=open("Pincode_30052019.csv","r")
locations=[]
pincodes=[]
districts=[]
states=[]
count1=0
s1=f1.readline()
for i in range(0,153000,1):
    count1=count1+1
    s1=f1.readline()
    list1=s1.split(",")
    locations.append(list1[3])
    pincodes.append(list1[4])
    if (count1 > 107000) and (count1 < 110000):
        print(list1[4],count1)
    districts.append(list1[7])
    states.append(list1[8])
     #pincode1=input("Enter pincode :")
while(True):
    pincode1=input("Enter pincode :")
    if pincode1=="quit":
        break
    position=pincodes.index(pincode1)
    location1=locations[position]
    district1=districts[position]
    state1=states[position]
    s2=pincode1+","+location1+","+district1+","+state1
    print(s2)
