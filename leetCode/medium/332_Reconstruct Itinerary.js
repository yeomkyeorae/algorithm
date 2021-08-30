/**
 * @param {string[][]} tickets
 * @return {string[]}
 */
let answer = [];
let done = false;

function go(obj, start, lastTrip, candidate, visited) {
  if (candidate.length === lastTrip) {
    answer = candidate.join(",").split(",");
    done = true;
    return;
  }

  if (done || !obj[start]) {
    return;
  }

  obj[start].forEach((city, index) => {
    if (!done && visited[start][index] === 0) {
      candidate.push(city);
      visited[start][index] = 1;
      go(obj, city, lastTrip, candidate, visited);
      candidate.pop();
      visited[start][index] = 0;
    }
  });
}

var findItinerary = function(tickets) {
  const obj = {};
  const visited = {};

  tickets.forEach(ticket => {
    if (Object.keys(obj).includes(ticket[0])) {
      obj[ticket[0]].push(ticket[1]);
      visited[ticket[0]].push(0);
    } else {
      obj[ticket[0]] = [ticket[1]];
      visited[ticket[0]] = [0];
    }
  });

  Object.keys(obj).forEach(key => {
    obj[key].sort();
  });

  const start = "JFK";
  done = false;
  go(obj, start, tickets.length + 1, [start], visited);

  return answer;
};
