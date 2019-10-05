const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const cors = require("cors");
const companyRoutes = require("./controllers/companies");
const fs = require("fs");
const { spawn } = require("child_process");

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
function runScript(file) {
  return spawn("python", ["-u", path.join(__dirname, file)]);
}

app.get("/companies", (req, res) => {
  // run a python script
  const subprocess = runScript("test.py");

  var outputData = null;

  // send the data from the standard output of the python script
  subprocess.stdout.on("data", data => {
    res.send(data);
  });
});

// catch all
app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "../src/index.html"));
});

app.listen(port, () => console.log(`listening on port ${3000}`));
