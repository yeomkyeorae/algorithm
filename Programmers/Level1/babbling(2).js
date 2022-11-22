const BABBLES = ["aya", "ye", "woo", "ma"];

function solution(babbling) {
    let answer = 0;
    
    for(let i = 0; i < babbling.length; i++) {
        const babble = babbling[i];

        let doubleFlag = false;
        ["ayaaya", "yeye", "woowoo", "mama"].forEach(double => {
            if(babble.indexOf(double) >= 0) {
                doubleFlag = true;
            }
        });
        
        if(doubleFlag) {
            continue    
        }
        
        let sub = '';
        for(let j = 0; j < babble.length; j++) {
            sub += babble[j];
            
            if(BABBLES.includes(sub)) {
                sub = '';
            }
        }

        if(BABBLES.includes(sub) || sub === '') {
            answer += 1;
        }
    }
    
    return answer;
}