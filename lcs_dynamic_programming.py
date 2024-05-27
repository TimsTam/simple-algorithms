# This program implements a dynamic programming approach to find the
# longest common subsequence (LCS) between two strings.

def lcs_dynamic_programming(s1, s2):
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # length of longest subsequence
    length = dp[len(s1)][len(s2)]

    # backtrack to get subsequence
    lcs = ""
    i = len(s1)
    j = len(s2)
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs = s1[i - 1] + lcs
            i -= 1
            j -= 1
            length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[len(s1)][len(s2)], lcs


string1 = "maelstrom"
string2 = "becalm"
dp = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]  # Initializes a 2D list with zeros
print(lcs_dynamic_programming(string1, string2))


