#!/usr/bin/python3
from datetime import datetime

NM=input("Enter Name");
AG=int(input("Enter Age"));
MS=int(input("No. of time you want to print the output"));
HA=datetime.now().year+100-AG;
print("Hi " + NM);  
report=("You will be 100 year old in " + str(HA));
print (" %s \n"%report * MS);
