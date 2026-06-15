class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = re.sub(r'[^a-zA-Z0-9]', '', s)
        s_new = s_new.lower()
        if s_new == s_new[::-1]:
            return True
        else:
            return False
        