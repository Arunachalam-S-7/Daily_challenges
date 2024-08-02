def expand_around_center(left, right):
        while left >= 0 and right < len(S) and S[left] == S[right]:
            left -= 1
            right += 1
        return S[left + 1:right]

    if not S:
        return ""

    longest_palindrome = ""
    for i in range(len(S)):
        # Odd-length palindromes (single character center)
        palindrome1 = expand_around_center(i, i)
        if len(palindrome1) > len(longest_palindrome):
            longest_palindrome = palindrome1
        
        # Even-length palindromes (two characters center)
        palindrome2 = expand_around_center(i, i + 1)
        if len(palindrome2) > len(longest_palindrome):
            longest_palindrome = palindrome2

    return longest_palindrome
