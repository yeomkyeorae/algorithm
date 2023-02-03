function solution(want, number, discount) {
  let answer = 0;
  const totalBuyingProducts = number.reduce((a, b) => { return a + b }, 0);
  
  const cart = {};
  want.forEach((product, index) => {
      cart[product] = number[index]; 
  });
  
  for(let i = 0; i <= discount.length - totalBuyingProducts; i++) {
      const sliced = discount.slice(i, i + totalBuyingProducts);
      const tempCart = {};
      sliced.forEach(product => {
         if(want.includes(product)) {
              if(Object.keys(tempCart).includes(product)) {
                  tempCart[product] += 1;
              } else {
                  tempCart[product] = 1;
              }
         } 
      });
      
      let flag = true;
      Object.keys(cart).forEach(product => {
          const productCnt = cart[product];
          if(productCnt !== tempCart[product]) {
              flag = false;
          }
      });
      
      if(flag) {
          answer += 1;
      }
  }
  
  return answer;
}