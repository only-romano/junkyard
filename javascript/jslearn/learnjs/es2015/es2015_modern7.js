'use strict';
console.time('Timer');

let badPromise = new Promise( function(resolve, reject) {
  throw new Error('o_O');
});

let goodPromise = new Promise( function(resolve, reject) {
  resolve('resilt');
});

let worked = () => { console.log('Worked!') };
let notWorked = () => { console.log('Not worked!') };

  badPromise.catch(console.log);
  goodPromise.catch(notWorked);

  badPromise.then(notWorked, worked);
  goodPromise.then(worked, notWorked);

  badPromise.then(null, worked);
  goodPromise.then(null, notWorked);

  goodPromise.then(worked);


let promise = new Promise((resolve, reject) => {
  console.time('Timeout-Count')
  setTimeout(() => { 
    reject(new Error('Time is over!'));
  }, 100);
});

  promise
    .then(
      result => {
        console.log('Fulfilled: ' + result);
      },
      error => {
        console.timeEnd('Timeout-Count');
        console.log('Rejected: ' + error.message);
      }
    );


function httpGet(url) {
  return new Promise( function(resolve, reject) {
    let xhr = 'new XMLHTTPRequest()';
      xhr.open('GET', url, true);

      xhr.onload = function() {
        if (this.status == 200) {
          resolve(this.response);
        } else {
          let error = new Error(this.statusText);
            error.code = this.status;
            reject(error);
        }
      };

      xhr.onerror = function() {
        reject(new Error('Network Error'));
      };

      xhr.send();
  });
}

httpGet('/article/promise/user.json')
  .then(
    response => {
      console.log(`Fulfilled: ${response}`);
      return user;
    },
    error => console.log(`Regected: ${error}`)
  )
  .then(
    user => {
      console.log(user);
      return httpGet(`https://api.github.com/users/${user}`);
    }
  )
  .then(
    githubUser => {
      console.log(githubUser);
      githubUser = JSON.parse(githubUser);

      let img = new Image();
        img.src = githubUser.avatar_url;
        img.className = 'promise_avatar_example';
        documend.body.appendChild(img);

        setTimeout(() => img.remove(), 3000);
    }
  );


httpGet('/page-not-exist')
  .then(response => JSON.parse(response))
  .then(user => httpGet(`https:/ali.github.com/users/${user.name}`))
  .then(githubUser => {
    githubUser = JSON.parse(githubUser);

    let img = new Image();
      img.src = githubUser.avatar_url;
      img.className = 'promise-avatar-example';
      document.body.appendChild(img);

      return new Promise((resolve, reject) => {
        setTimeout(() => {
          img.remove();
          resolve();
        }, 3000);
      });
  })
  .catch(error => {
    console.log(error.message);
  })


promise = new Promise((resolve, reject) => resolve(1));

promise.then( function f1(result) {
  console.log(result);
  return 'f1';
})

promise.then(function f2(result) {
  console.log(result);
  return 'f2';
})


console.timeEnd('Timer');