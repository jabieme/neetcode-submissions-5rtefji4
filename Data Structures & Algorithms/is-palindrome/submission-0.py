class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        last = len(string) - 1
        first = 0

        while first < last:
            if string[first] != string[last]:
                return False;
            first = first + 1
            last = last - 1
        return True