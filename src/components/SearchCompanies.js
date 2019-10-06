import React from "react";
import Select from "react-select";
import companyData from "./company_info";
import CanvasJSReact from "./canvasjs/canvasjs.react";
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

class SearchCompanies extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      inputValue: "",
      one: [],
      two: [],
      three: [],
      currentCompanyInfo: [],
      currentYear: 1,
      dataPoints: []
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleSumbit = this.handleSumbit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }
  handleChange(event) {
    this.setState({ currentYear: event.target.value });
    console.log(this.state.currentYear);
  }

  handleInputChange(event) {
    event.preventDefault();
    this.setState({ inputValue: event.target.value });
    console.log(this.state.inputValue);
  }

  handleSumbit(event) {
    event.preventDefault();
    const body = { company: this.state.inputValue };
    fetch("/investment", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ company: this.state.inputValue })
    })
      .then(data => {
        if (data.status === 200) {
          return data.json();
        } else {
          throw new Error("error cannot get data");
        }
      })
      .then(res => {
        console.log(res);
        this.setState({ inputValu: "" });
        this.setState({ one: [] });
        this.setState({ two: [] });
        this.setState({ three: [] });
        this.setState({ dataPoints: [] });

        this.setState({ currentCompanyInfo: res[0] });
        this.setState({ one: res[1]["1Y"] });
        this.state.one.forEach((arr, index) => {
          this.setState(prevState => {
            let newState = [
              ...prevState.dataPoints,
              { x: index, y: arr["close"] }
            ];
            prevState.dataPoints = newState;
          });
        });
        this.setState({ two: res[1]["2Y"] });
        this.setState({ three: res[1]["3Y"] });
        console.log(this.state.dataPoints);
      });
  }
  generateGraph() {
    const options = {
      animationEnabled: true,
      exportEnabled: true,
      theme: "light2",
      title: {
        text: "Stock Price"
      },
      axisY: {
        title: "Closing Price",
        includeZero: false,
        suffix: "%"
      },
      axisX: {
        title: `Year ${this.state.currentYear}`,
        // prefix: "W",
        interval: 20
      },
      data: [
        {
          type: "line",
          // toolTipContent: "Week {x}: {y}%",
          dataPoints: this.state.dataPoints
        }
      ]
    };
    return <CanvasJSChart options={options} />;
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSumbit}>
          <input
            type="text"
            onChange={this.handleInputChange}
            value={this.state.inputValue}
          ></input>
          <button type="submit">Submit</button>
        </form>
        <select onChange={this.handleChange}>
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
        </select>
        {this.generateGraph()}
      </div>
    );
  }
}

export default SearchCompanies;
