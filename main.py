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
        self.subnet_id = None
        self.broadcast_add = None
        self.first_avaliable_host = None
        self.last_avaliable_host = None
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
                #Added one to get the appropriate 'octet'
                self.CIDR_octet = i + 1
            elif(self.CIDR_val < SevenSecondMatrix[i][7]):
                for j in range(7,-1, -1):
                    if (SevenSecondMatrix[i][j] == self.CIDR_val):
                        self.CIDR_chart_row = j
                        #Added one to get the appropraite 'octet'
                        self.CIDR_octet = i + 1

        print(f"should be on row:{self.CIDR_chart_row}")
        print(f"on octet #: {self.CIDR_octet}")
        return True


               

    def user_menu(self):
        while not self.valid:
            ipvaddress = (input("Please enter a valid IP address with CIDR notation:"))
            self.valid = SevenSecondMatrixClass.is_valid_ip(self,ipvaddress)
        if self.valid: 
            print("Nice Job!")
        else:
            print("Please  Try Again.")

        self.calculate_subnetmask()
        
    
        
    def start (self):
        self.user_menu()

x = SevenSecondMatrixClass()
x.start()


