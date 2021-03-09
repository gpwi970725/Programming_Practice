class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, string):  # index : digits에서 현재 인덱스 / string : 현재 만드는중인 문자열
            # 문자열이 만들어져야하는 길이만큼 만들어졌으면 종료
            if len(string) == len(digits):
                answer.append(string)
                return
            
            for char in dic[digits[index]]:
                dfs(index + 1, string + char)
            
        # digits가 빈 문자열일 때 예외처리
        if not digits:
            return digits
        
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        answer = []
        
        dfs(0, "")
        return answer
