const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const cors = require("cors");
const companyRoutes = require("./controllers/companies");
const fs = require("fs");
const { spawnSync } = require("child_process");

const app = express();
const port = 3000;
app.use(cors());
app.use(bodyParser.json());
app.use(
  bodyParser.urlencoded({
    extended: true
  })
);
app.use(express.static("build"));

// run a python script, takes a file name as a parameter
function runScript(file, args) {
  // establish the tail of the python script call
  tail = [path.join(__dirname, "../python", file)];

  // add each argument to the tail
  args.forEach(item => {
    tail.push(item);
  });

  // run the python script
  return spawnSync("python", tail);
}

// run investment.py upon receiving a request
app.post("/investment", (req, res) => {
  const company = req.body.company;
  // run a python script
  const subprocess = runScript("investment.py", [company]);
  // convert the json string to the proper format
  const pfJSON = runScript("sdReplace.py", [subprocess.stdout]);

  // // send the data from the standard output of the python script
  res.send(subprocess.stdout);
  console.log(subprocess.stdout);
  // res.send(subprocess.stdout)
  console.log(JSON.parse(pfJSON.stdout));
  res.send(JSON.parse(pfJSON.stdout));
});

// run investment.py upon receiving a request
app.get("/past", (req, res) => {
  const company = req.body.company;

  // run a python script
  const subprocess = runScript("historical.py", [company]);

  // send the data from the standard output of the python script
  res.send(subprocess.stdout);
});

// catch all
app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "../src/index.html"));
});

app.listen(port, () => console.log(`listening on port ${3000}`));
