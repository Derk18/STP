# reusable code

percentage=int(input("Enter your marks: "))
Test_mark=int(input("Enter your papers mark: "))
def mark(percentage,Test_mark):
    marks=(percentage/Test_mark)*100
    print("marks: ")
    print(marks)

    if marks>40:
        return"you have passed"
    else:
        return"You have failed"
     
result=mark(percentage,Test_mark)            
print(result)