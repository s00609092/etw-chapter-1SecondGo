aclNum = int(input("what is the IPv4 ACL number?"))
if aclNum >= 1 and aclNum <= 99:
    print("this is a standard Ipv4 ACL")
    elif aclNum > = 100 and aclNum < = 199:
        print(" This is an extended IPv4 ACL")
        else:
            print ("This is not a standard or extended IPv4 ACL.")
