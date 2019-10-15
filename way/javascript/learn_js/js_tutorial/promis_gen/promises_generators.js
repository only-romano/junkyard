'use strict';

(function () {
  httpGet("http://learn.javascript.ru/article/promise/user.json")
    .then(
      response => alert(`Fulfilled: ${response}`),
      error => alert(`Rejected: ${error}`)
    );
});

(function () {
  httpGet('http://learn.javascript.ru/article/promise/user.json')
  // 1. Получить данные о пользователе в JSON и передать дальше
  .then(response => {
    console.log(response);
    let user = JSON.parse(response);
    return user;
  })
  // 2. Получить информацию с github
  .then(user => {
    console.log(user);
    return httpGet(`https://api.github.com/users/${user.name}`);
  })
  // 3. Вывести аватар на 3 секунды (можно с анимацией)
  .then(githubUser => {
    console.log(githubUser);
    githubUser = JSON.parse(githubUser);

    let img = new Image();
    img.src = githubUser.avatar_url;
    img.className = "promise-avatar-example";
    document.body.appendChild(img);

    setTimeout(() => img.remove(), 3000); // (*)
  });
});

(function () {
  httpGet('http://learn.javascript.ru/article/promise/userNoGithub.json')
    .then(JSON.parse)
    .then(user => httpGet(`https://api.github.com/users/${user.name}`))
    .then(
      JSON.parse,
      function githubError(error) {
        if (error.code == 404) {
          return {name: "NoGithub", avatar_url: 'http://learn.javascript.ru/article/promise/anon.png'};
        } else {
          throw error;
        }
      }
    )
    .then(function showAvatar(githubUser) {
      let img = new Image();
      img.src = githubUser.avatar_url;
      img.className = "promise-avatar-example";
      document.body.appendChild(img);
      setTimeout(() => img.remove(), 3000);
    })
    .catch(function genericError(error) {
      alert(error); // Error: Not Found
    });
});

(function() {
  function* showUserAvatar() {
    let userFetch = yield fetch('http://learn.javascript.ru/article/generator/user.json');
    let userInfo = yield userFetch.json();

    let githubFetch = yield fetch(`https://api.github.com/users/${userInfo.name}`);
    let githubUserInfo = yield githubFetch.json();

    let img = new Image();
      img.src = githubUserInfo.avatar_url;
      img.className = 'promise-avatar-example';
      document.body.appendChild(img);

    yield new Promise(resolve => setTimeout(resolve, 3000));
      img.remove();

    return img.src;
  }

  function execute(generator, yieldValue) {
    let next = generator.next(yieldValue);
      if (!next.done) {
        next.value.then(
          result => execute(generator, result),
          err => generator.throw(err)
        );
      } else {
        console.log( next.value );
      }
  }

  execute( showUserAvatar() );
});


(function() {
  co(function*() {
    let result = yield new Promise(resolve => setTimeout(resolve, 1000, 1));
    throw new Error("Sorry that happended");
    return result;
  }).then(alert).catch(alert);
});

(function() {
  Object.defineProperty(window, 'result', {
    set: value => alert(JSON.stringify(value))
  });

  co(function*() {
    result = yield function*() { return 1; }();
    result = yield function*() { return 2; };
    result = yield Promise.resolve(3);
    result = yield function(callback) { setTimeout( () => callback(null, 4), 1000 ); };
    result = yield {
      one: Promise.resolve(1),
      two: function*() { return 2; }
    };
    result = yield [
      Promise.resolve(1),
      function*() { return 2; }
    ];
  });
});

(function() {
  co( function*() {
    let result = yield* gen();
    alert(result);
  });

  function* gen() { return yield* gen2(); }

  function* gen2() {
    let result = yield new Promise(resolve => setTimeout(resolve, 1000, 'Hello!'));
    return result;
  }
});

(function() {
  function* fetchUser(url) {
    let userFetch = yield fetch(url);
    let user = yield userFetch.json();

    return user;
  }

  function* fetchGithubUser(user) {
    let githubFetch = yield fetch(`https://api.github.com/users/${user.name}`);
    let githubUser = yield githubFetch.json();

    return githubUser;
  }

  function sleep(ms){
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  function* fetchAvatar(url) {
    let user = yield* fetchUser(url);
    let githubUser = yield* fetchGithubUser(user);

    return githubUser.avatar_url;
  }

  function* showUserAvatar() {
    let avatarUrl;

    try {
      avatarUrl = yield* fetchAvatar('https://raw.githubusercontent.com/Ridj/ridj.github.io/master/user.json');
    } catch(e) {
      avatarUrl = 'http://learn.javascript.ru/article/generator/anon.png';
    }

    let img = new Image();
      img.src = avatarUrl;
      img.className = 'promise-avatar-example';
    document.body.appendChild(img);

    yield sleep(2000);
      img.remove();

    return img.src;
  }

  co(showUserAvatar);
})();