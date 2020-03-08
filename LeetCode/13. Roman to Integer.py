class Solution:
    def romanToInt(self, s):
        sysms = {'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
        result, temp
        
        for letters in reversed(s):
            number = sysms[letters]
            
            if number >= temp:
                result += number
            else:
                result -= number
                
            temp = number
        return result
        
