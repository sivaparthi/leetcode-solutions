class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]

        dec = 0
        binary = int(binary)
        count = 0
        while binary:
            digit = binary % 10
            if digit == 1:
                digit = 0
            else:
                digit = 1
            dec = dec + (digit * (2 ** count))
            binary = binary // 10
            count += 1 
        return dec