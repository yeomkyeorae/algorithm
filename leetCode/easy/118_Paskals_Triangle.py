/**
* @ param {number} numRows
* @ return {number[][]}
*/
var generate = function(numRows) {
    const answer = [[1]]

    if(numRows > 1) {
        answer.push([1, 1])

        for(let i=0
            i < numRows - 2
            i + +) {
            const tmp = [1]

            let start = 0
            let end = 1

            const last = answer[answer.length - 1]

            while(end < last.length) {
                const summation = last[start] + last[end]
                tmp.push(summation)
                start++
                end++
            }

            tmp.push(1)
            if(tmp.length > 2) {
                answer.push(tmp)
            }
        }
    } else {
        return answer
    }

    return answer
}
