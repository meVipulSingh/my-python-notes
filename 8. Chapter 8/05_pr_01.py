def greatest(sum1, sum2, sum3):           
    if(sum1>sum2):
        if(sum1>sum3):
            return sum1

        else:
            return sum3
    else:
        if(sum2>sum3):
            return sum2
        else:
            return sum3
m = greatest(14,78,55)
print("The greatest of three numbers is " + str(m))