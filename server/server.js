const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
const cors = require("cors");
const companyRoutes = require("./controllers/companies");

// allow execution of synchronus commands
const { execSync } = require("child_process");

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

app.get("/companies", companyRoutes.sendCompanyData);

// catch all
app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "../src/index.html"));
});

app.listen(port, () => console.log(`listening on port ${3000}`));
