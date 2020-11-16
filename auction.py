# 0,1,6,9 are flippable
# find al flippable numbers between 1 and 650 which lead to different numbers
# 11 can be flipped but leads to 11 so needs to be discarded
# 16 can be flipped and leads to 91, so needs to be saved
# I consider 116 flippable even if returns 911, which is > 650. Not sure if the action accept paddles with $$ > 650.


def auctionString(X=650):
    
    n_list = [6,9] #these should be simple
    verbose = True
    blist = ["2","3","4","5","7","8"]

    for n in range(12,X):
        n_str = str(n)
        stop=False
    
    #Skip all numbers that don't have 0,1,6 or 9-> not flippable
        for b in blist:
            if b in n_str:
                stop=True
                break

    #Skip the ones that end with 0-> those are not valid.
        if stop or n_str[-1]=="0":
            continue

    #Skip the ones that flipped are equal to themselves.
        new_num = ""
        for digit in n_str[::-1]:
            if digit=="1" or digit=="0":
                new_num+=digit
            elif digit=="6":
                new_num+="9"
            else :
                new_num+="6"
        if new_num == n_str:
            continue

    #Store output in a list
        n_list.append(n)
    
    print("Total flippable numbers:",len(n_list))
    if verbose:
        print(n_list)

        
def main():
    auctionString()
    


if __name__ =="__main__":
    main()
