class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answers = [[1], [1, 1]]
        
        if rowIndex < 2:
            return answers[rowIndex]
        
        rowIndex -= 1
        while rowIndex:
            tmp_answer = [1]
            
            parent = answers[-1]
            for i in range(len(parent) - 1):
                tmp_answer.append(parent[i] + parent[i + 1])
            
            tmp_answer.append(1)
            answers.append(tmp_answer)
            
            rowIndex -= 1
            
        return answers[-1]