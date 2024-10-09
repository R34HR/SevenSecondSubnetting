'''
Hello dear reader! This is a personal tool that I made which asks a user for a valid IPv4 address
and using the Seven-Second Subnetting technique returns all 4 major subnet address including:
    1.) Network Address(subnet ID)
    2.) Broadcast Address
    3.) First Usable Host Address
    4.) Last Usable Host Address

This project is meant to further my knowledge in subnetting and skills in Python
'''

SevenSecondMatrix = [[1,2,3,4,5,6,7,8],
    [9,10,11,12,13,14,15,16], 
    [17,18,19,20,21,22,23,24], 
    [25,26,27,28,29,30,31,32], 
    [128,192,224,240,248,252,254,255],
    [2,4,8,16,32,64,128,256],
    [128,64,32,16,8,4,2,1]]

def valid_ip(address):
    try:
        hosts = address.split('.')
        valid = [int(i) for i in hosts]
        valid = [b for b in valid if b >=0 and b <= 255]
        return len(hosts) == 4 and len(valid) == 4
        
    except:
        return False
  
Decimal_Coloum = 4

UserIP = (input("Please enter a valid IP address with CIDR notation:"))
Valid = valid_ip(UserIP)
print(Valid)


