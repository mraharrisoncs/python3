message =input("enter message")
newmessage=""
length =len(message)
for i in range (length):
    ASCIIvalue = (message[0:1])
    ASCIIvalue = [ord(c) for c in message]
    print (ASCIIvalue)
    for num in ASCIIvalue:
        ASCIIvalue =ASCIIvalue[+1]# this is where i think i am going wrong
    #ASCIIvalue= ASCIIvalue +[1}
        if ASCIIvalue >90:
            ASCIIvalue = ASCIIvalue- 26
        newmessage = (newmessage +[chr(ASCIIvalue)])
print(newmessage)


