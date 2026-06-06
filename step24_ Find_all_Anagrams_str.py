def findAnagrams(s, p):

    result = []

    if len(p) > len(s):
        return result


    p_count = {}
    window_count = {}


    # first window
    for i in range(len(p)):

        p_count[p[i]] = p_count.get(p[i],0)+1

        window_count[s[i]] = window_count.get(s[i],0)+1


    if p_count == window_count:
        result.append(0)


    left = 0


    for right in range(len(p), len(s)):


        # add new character
        window_count[s[right]] = window_count.get(s[right],0)+1


        # remove old left character
        window_count[s[left]] -= 1


        if window_count[s[left]] == 0:
            del window_count[s[left]]


        left += 1


        if p_count == window_count:
            result.append(left)


    return result



s="cbaebabacd"
p="abc"

print(findAnagrams(s,p))