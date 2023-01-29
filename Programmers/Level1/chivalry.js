function solution(number, limit, power) {
    let answer = 0;
    
    for(let j = 1; j <= number; j++) {
        const yaksuSet = new Set();
        for(let i = 1; i <= Math.round(Math.pow(j, 1/2)) + 1; i++) {  // 약수를 구할 때 제곱수를 활용한다.
            if(j === 1) {
                yaksuSet.add(1);
            }
            if(j % i === 0) {
                yaksuSet.add(i);
                yaksuSet.add(j / i);
            }
        }
        const numOfYaksu = yaksuSet.size;
        if(numOfYaksu > limit) {
            answer += power;
        } else {
            answer += numOfYaksu;
        }
    }
    
    return answer;
}
