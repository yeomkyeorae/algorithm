function solution(elements) {
    const answerSet = new Set();
    
    const length = elements.length;
    for(let start = 0; start < length; start++) {
        for(let len = 1; len <= length; len++) {
            let tmp = 0;
            for(let j = 0; j < len; j++) {
                let ix = start + j;
                let divIx = ix % length;
                tmp += elements[divIx];
            }
            answerSet.add(tmp);
        }
    }
    
    return answerSet.size;
}