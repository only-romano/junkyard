'use strict';

function nodecount(node) {
  return node.children.map(nodecount).reduce((acc, it) => it + acc, 1);
}

function nodecount(root) {
  const stack = [root];
  let result = 0;
  while (stack.length) {
    result++;
    stack.push(...stack.pop().children);
  }
  return result;
}

function fac(n) {
  const stack = [n];
  let result = 1;
  while (true) {
    const top = stack.pop();
    result *= top;
    if (top == 1) return result;
    stack.push(top - 1);
  }
}

console.log(nodecount({
  children: [
      {children: [
        {children: []},
        {children: [
          {children: []}
        ]},
      ]},
      {children: []},
  ],
}));
