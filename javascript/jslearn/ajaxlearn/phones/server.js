let http = require('http');
let url = require('url');
let querystring = require('querystring');
let static = require('node-static');
let file = new static.Server('.', { cache: 0 });


function accept(req, res) {
  file.serve(req, res);
}


if (!module.parent) http.createServer(accept).listen(8080);
else exports.accept = accept;
