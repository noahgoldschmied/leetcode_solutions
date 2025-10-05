class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = {}
        answer = []
        for word in strs:
            sortedword = sorted(word)
            s = ""
            for char in sortedword:
                s += char
            if s not in sorted_words:
                sorted_words[s] = len(answer)
                array = []
                array.append(word)
                answer.append(array)
            else:
                answer[sorted_words[s]].append(word)
            
        return answer