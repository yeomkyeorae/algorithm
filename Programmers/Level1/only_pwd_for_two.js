const alphabet = 'abcdefghijklmnopqrstuvwxyz';

function solution(s, skip, index) {
    let answer = '';
    
    for(let i = 0; i < s.length; i++) {
        const ch = s[i];
        
        let nextIndex = alphabet.indexOf(ch) + 1;
        let cnt = 0;

        while(cnt !== index) {
            const tmpIndex = nextIndex % 26;

            nextIndex += 1;
            if(skip.includes(alphabet[tmpIndex])) {
                continue
            }
            
            cnt += 1;
        }

        answer += alphabet[(nextIndex - 1) % 26];
    }
    
    return answer;
}