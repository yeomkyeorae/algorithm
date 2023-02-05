function solution(order) {
  let answer = 0;
  
  const main = [];
  for(let i = order.length; i > 0; i--) main.push(i);
  
  const isToGo = {};
  const sub = [];
  
  let orderIx = 0;
  while(answer !== order.length) {
      const num = order[orderIx];
      
      if(isToGo[num] === undefined) {
          while(true) {
              const popped = main.pop();
              if(popped === num) {
                  orderIx += 1;
                  answer += 1;
                  break;
              } else {
                  isToGo[popped] = true;
                  sub.push(popped);
              }
          }
      } else {
          if(sub.length > 0) {
              const popped = sub.pop();
              if(popped === num) {
                  orderIx += 1;
                  answer += 1;
              } else {
                  break;
              }
          } else {
              break;
          }
      }
  }
  
  return answer;
}