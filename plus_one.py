class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 0
        flag = True
        carry = 1
        while(i < len(digits) and flag):
            i_neg = 0 - i - 1
            carry = carry+digits[i_neg]
            add_num = (carry % 10)
            digits[i_neg]=add_num
            carry = carry // 10
            if (carry > 0):
                flag = True
            else:
                flag = False
            i = i + 1

        if i == len(digits) and flag:
            digits.insert(0,carry)
        return digits

            

        