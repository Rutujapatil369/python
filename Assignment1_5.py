#.Write a program which display 10 to 1 on screen.
def fun():
    print("Output of for loop")
    iCnt=0
    for iCnt in range(10,0,-1):
        print(iCnt)
    
       
def main():
    fun()
    
if __name__=="__main__":
    main()