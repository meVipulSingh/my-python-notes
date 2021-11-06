sub1 = int(input("enter firt subject marks : "))
sub2 = int(input("enter second subject marks : "))
sub3 = int(input("enter third subject marks : "))
 
if(sub1<33 or sub2<33 or sub3<33):
     print("you are fail because you ha less then 33% in one of your subject")
elif(sub1+sub2+sub3)/3 <40:
    print("you are fail due to total percentage is less then 40")
else:
    print("congratulation you are passed!")
