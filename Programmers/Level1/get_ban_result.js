function solution(id_list, report, k) {
    const banCntObj = {};
    const banContentObj = {};
    id_list.forEach(id => {
        banCntObj[id] = 0;
        banContentObj[id] = new Set();
    });
    
    report.forEach(el => {
        const arr = el.split(" ");
        if(!banContentObj[arr[0]].has(arr[1])) {
            banContentObj[arr[0]].add(arr[1])
            banCntObj[arr[1]] += 1
        }
    });
    
    const answer = [];
    id_list.forEach(id => {
        let cnt = 0;
        banContentObj[id].forEach(op => {
             if(banCntObj[op] >= k) {
                 cnt += 1;
             }
        });
        answer.push(cnt);
    });
    
    return answer;
}