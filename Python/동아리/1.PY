def find_longest_common_substring_with_edit(str1, str2):
    m, n = len(str1), len(str2)

    # Initialize a 2D DP table to store the length of common substrings.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize variables to keep track of the best match.
    max_length = 0
    max_i = 0
    max_j = 0
    edit_used = False  # Indicates if an edit has been used

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0

            if dp[i][j] > max_length:
                max_length = dp[i][j]
                max_i = i
                max_j = j

    # Construct the common substring.
    common_substring = []
    while max_i > 0 and max_j > 0:
        if str1[max_i - 1] == str2[max_j - 1]:
            common_substring.append(str1[max_i - 1])
            max_i -= 1
            max_j -= 1
        else:
            if not edit_used:
                common_substring.append(str2[max_j - 1])
                edit_used = True
            else:
                break
            max_j -= 1

    common_substring.reverse()

    return "".join(common_substring)

# Example usage:
str1 = "ABCDG"
str2 = "AEDG"

result = find_longest_common_substring_with_edit(str1, str2)
print("Longest Common Substring with 1 Edit Allowed:", result)
