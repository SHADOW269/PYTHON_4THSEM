def dictionary():
    teststr= input("Enter a String")
    all_freq={}
    for i in teststr:
        if i in all_freq:
            all_freq[i]+=1
        else:
            all_freq[i]=1
    print(f"Count of all Character in {teststr} is:\n"+str(all_freq))
dictionary()