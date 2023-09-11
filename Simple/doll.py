doll_cost = 30
transport_cost = 8
gst=0.12
additional_transport_charge = 2
number = int(input('How many dolls do you want?'))
if number==1:
    transpor_charge=transport_cost

else:
    transpor_charge=transport_cost+additional_transport_charge
noOf_dolls=doll_cost*number
findCharge=noOf_dolls*gst
charge=noOf_dolls+transpor_charge+findCharge


print(charge)

