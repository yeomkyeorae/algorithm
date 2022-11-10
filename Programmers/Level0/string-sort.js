function solution(myString) {
    const strArr = Array.from(myString);
    const lowerStrArr = strArr.map(ch => ch.toLowerCase());
    lowerStrArr.sort();
    
    const answer = lowerStrArr.join('');
    return answer;
}