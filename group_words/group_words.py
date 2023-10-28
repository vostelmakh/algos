# Sample Input ["eat", "tea", "tan", "ate", "nat", "bat"]
# Sample Output [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]

def groupAnagrams(strs):
    groups = {}
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word in groups:
            groups[sorted_word].append(word)
        else:
            groups[sorted_word] = [word]
    
    return list(groups.values())

res = groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(res)
