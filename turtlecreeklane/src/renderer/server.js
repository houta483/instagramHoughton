const express = require('express');
const path = require('path');
const app = express();
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const PORT = 3434;

app.use(bodyParser.json());
app.use(cookieParser());

app.listen(PORT, () => console.log(`Listening on port ${PORT}`))

app.get('/connections', connections);

app.get('/', (req, res, next) => {
  res.send('/Users/Tanner/code/products/Instagram/turtlecreeklane/src/renderer/components/LandingPage/SystemInformation.vue')
})

function connections(req, res) {
  let spawn = require('child_process').spawn;

  let process = spawn('python', ["python/connections.py",
    req.query.file
  ]);

  process.stdout.on('data', (data) => {
    res.send(data.toString());
  })
}