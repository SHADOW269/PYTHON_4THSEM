def nearly_equal(a,b):
    if len(a)!=len(b) or a==b:
        return False
    differing_chars=sum(1 for i in range (len(a)) if a[i]!=b[i])
    return differing_chars==1
string1=input("Enter the first string:")
string2=input("Enter the second string:")
print(f"Are string {string1} and {string2} nearly equal?")
print(nearly_equal(string1,string2))