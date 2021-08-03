function solution(price, money, count) {
  let answer = -1;

  let neededMoney = 0;
  for (let i = 1; i <= count; i++) {
    neededMoney += price * i;
  }

  if (neededMoney - money > 0) {
    return neededMoney - money;
  } else {
    return 0;
  }
}
