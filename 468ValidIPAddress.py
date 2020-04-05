# 468. Validate IP Address
"""
"""
#-------------------------------------------------------------------------------
#    Approach- 
#-------------------------------------------------------------------------------

"""

"""

#-------------------------------------------------------------------------------
#    Soluton 1 
#-------------------------------------------------------------------------------
class Solution():
    def validate_IPv4(self, IP):
        copnts = IP.split('.')
        print(copnts)
        for x in copnts:
            # Validate integer in range (0, 255):
            # 1. length of chunk is between 1 and 3
            if len(x) == 0 or len(x) > 3:
                return "Neither"
            # 2. no extra leading zeros
            # 3. only digits are allowed
            # 4. less than 255
            if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
                return "Neither"
        return "IPv4"


    def validate_IPv6(self, IP):
        copnts = IP.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        for x in copnts:
            if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                return "Neither"
        return "IPv6"


    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if IP.count('.') == 3:
            return self.validate_IPv4(IP)
        elif IP.count(':') == 7:
            return self.validate_IPv6(IP)
        else:
            return "Neither"

#-------------------------------------------------------------------------------
#    test
#-------------------------------------------------------------------------------
IP ="1.0.1."
soln = Solution()
print(soln.validIPAddress(IP))