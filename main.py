'''
Hello dear reader! This is a personal tool that I made which asks a user for a valid IPv4 address
and using the Seven-Second Subnetting technique returns all 4 major subnet address including:
    1.) Network Address(subnet ID)
    2.) Broadcast Address
    3.) First Usable Host Address
    4.) Last Usable Host Address

This project is meant to further my knowledge & skills in subnetting + Python
'''

##############################################
# Here we define the seven-second matrix to do our calculations
# as well as all resepctive coloumns so we can have fixed access
import keyboard
SevenSecondMatrix = ((1,2,3,4,5,6,7,8),
    (9,10,11,12,13,14,15,16), 
    (17,18,19,20,21,22,23,24), 
    (25,26,27,28,29,30,31,32), 
    (128,192,224,240,248,252,254,255),
    (2,4,8,16,32,64,128,256),
    (128,64,32,16,8,4,2,1))


class SevenSecondMatrixClass:
    def __init__(self):
        # Chart Limits
        self.masks_col = range(0,4)
        self.decimal_col = 4
        self.network_col = 5
        self.maxhost_col = 6
        self.maxcol_len = range(8)

        #Necessary chart values
        self.CIDR_chart_row = None
        self.CIDR_octet = None
        
        #user IPv4 info.
        self.user_ip = None
        self.CIDR_val = None
        self.valid = False
        self.subnetmask = []


        #four important addresses for the user
        self.subnet_id = []
        self.broadcast_add = []
        self.first_usable_host = []
        self.last_usable_host = []
        self.delineation_val = None
    def is_valid_ip(self,address):
        try:
            split_address = address.split('/')
            self.user_ip = split_address[0].split('.')
            self.CIDR_val= int(split_address[1])
            valid = [int(i) for i in self.user_ip]
            valid = [b for b in valid if b >=0 and b <= 255]
            return len(valid)==4 and self.CIDR_val<=32     
        except:
            return False
  
    def calculate_subnetmask(self):
        #Obtain CIDR notation postion on chart to help calculate the appropriate subnet mask
        for i in self.masks_col:
            if(self.CIDR_val == SevenSecondMatrix[i][7]):
                self.CIDR_chart_row = 7
                self.CIDR_octet = i
                break
            elif(self.CIDR_val < SevenSecondMatrix[i][7]):
                for j in range(7,-1, -1):
                    if (SevenSecondMatrix[i][j] == self.CIDR_val):
                        self.CIDR_chart_row = j
                        self.CIDR_octet = i
                        break
        

        #Append 255 to all octets previous to the CIDR_octet
        for x in range(self.CIDR_octet):
            self.subnetmask.append(255)

        #Append the Decimal Value from the SevenSecondMatrix    
        self.subnetmask.append(SevenSecondMatrix[self.decimal_col][self.CIDR_chart_row])
        
        #Append 0 to all values after the CIDR_octet
        for y in range(self.CIDR_octet+1,4):
            self.subnetmask.append(0)

        print(f"Subnet mask: {self.subnetmask}")
        return True        

    def calculate_subnetID(self):
        for i in range(len(self.subnetmask)):
            if(self.subnetmask[i] == 255):
                self.subnet_id.append(self.user_ip[i])
            elif(self.subnetmask[i] == 0):
                self.subnet_id.append(0)
            else:
                target = int(self.user_ip[i])
                self.delineation_val = int(SevenSecondMatrix[self.maxhost_col][self.CIDR_chart_row])
                val = self.delineation_val

                while (val < 255):
                    if (target < val):
                        val -= self.delineation_val
                        self.subnet_id.append(val)
                        break
                    else: 
                        val += self.delineation_val
        print(f"Subnet ID: {self.subnet_id}")

    def calculate_broadcastaddr(self):
        for i in range(len(self.subnetmask)):
            if(self.subnetmask[i] == 255):
                self.broadcast_add.append(self.user_ip[i])
            elif(self.subnetmask[i] == 0):
                self.broadcast_add.append(255)
            else:
                val = self.subnet_id[i] + self.delineation_val - 1
                self.broadcast_add.append(val)

        print(f"Brodcast Address: {self.broadcast_add}")


    def calculate_usableAddr(self):
        self.first_usable_host = self.subnet_id
        self.first_usable_host[3] += 1

        self.last_usable_host = self.broadcast_add
        self.last_usable_host[3] -= 1
        print(f"First Usable Host Address: {self.first_usable_host}")
        print(f"Last Usable Host Address: {self.last_usable_host}")
        
    def user_menu(self):
        while not self.valid:
            ipvaddress = (input("Please enter a valid IP address with CIDR notation:"))
            self.valid = SevenSecondMatrixClass.is_valid_ip(self,ipvaddress)
        if self.valid: 
            print("Nice Job!")
        else:
            print("Please  Try Again.")

        self.calculate_subnetmask()
        self.calculate_subnetID()
        self.calculate_broadcastaddr()
        self.calculate_usableAddr()
    def start (self):
        print("+----------------------------+")
        print("Seven Second Subnetting Tool!")
        print("+----------------------------+")

        self.user_menu()

x = SevenSecondMatrixClass()
x.start()


