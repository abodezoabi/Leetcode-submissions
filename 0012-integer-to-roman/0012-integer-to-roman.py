class Solution:
    def intToRoman(self, num: int) -> str:
        thousands = num // 1000  # =3.749->3
        hundreds = (num % 1000) // 100  # 749//100=7.49->7
        tens = (num % 100) // 10  # 49//10 ->4
        ones = num % 10  # 9

        thousands_map = ["", "M", "MM", "MMM"]
        hundreds_map = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens_map = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones_map = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        ans = (thousands_map[thousands] + hundreds_map[hundreds] +
        tens_map[tens] + ones_map[ones] )

        return ans

 
