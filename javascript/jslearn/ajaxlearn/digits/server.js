let http = require('http');
let url = require('url');
let querystring = require('querystring');
let static = require('node-static');
let file = new static.Server('.');


function accept(req, res) {
  if (req.url == '/digits') {
    res.writeHead(200, {
      'Content-Type': 'text/plain',
      'Cache-Control': 'no-cache'
    });

    let i = 0;
    let timer = setInterval(write, 1000);
    write();

    function write() {
      res.write(new Array(1000).join(++i + '') + ' ');
        if (i == 9) {
          clearInterval(timer);
          res.end();
        }
    }
  } else file.serve(req, res);
}


if (!module.parent) http.createServer(accept).listen(8080);
else exports.accept = accept;
