const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const cors = require("cors");
const companyRoutes = require("./controllers/companies");
const fs = require("fs");
const { exec } = require("child_process");

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

app.get("/companies", (req, res) => {
  const company = req.body.company;
  exec("python test.py", (err, stdout, stderr) => {
    if (err) {
      res.send("bad file");
      return;
    }

    res.send(stdout);
  });
});

// catch all
app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "../src/index.html"));
});

app.listen(port, () => console.log(`listening on port ${3000}`));
