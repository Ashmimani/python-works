text="RACECAR"

for i in range (0,len(text)):
    left=i
    right=i
    while(left>=0 and right<len(text) and text[left]==text[right]):
        current_palindromic_text=text[left:right+1]
        print(current_palindromic_text)
        left=left-1
        right=right+1


