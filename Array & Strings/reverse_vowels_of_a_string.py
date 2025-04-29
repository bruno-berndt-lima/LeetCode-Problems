class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        left, right = 0, len(s) - 1
        str_array = list(s)

        while left < right:
            if str_array[left] in vowels and str_array[right] in vowels:
                str_array[left], str_array[right] = str_array[right], str_array[left]
                left += 1
                right -= 1
            elif str_array[left] in vowels:
                right -= 1
            elif str_array[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1

        return "".join(str_array)
