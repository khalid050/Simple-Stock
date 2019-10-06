import React from "react";
import Select from "react-select";
import companyData from "./company_info";

class SearchCompanies extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      inputValue: ""
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleSumbit = this.handleSumbit.bind(this);
  }
  handleChange(selectedOption) {
    this.setState({ selectedOption }, () =>
      console.log(`Option selected:`, this.state.selectedOption)
    );
  }

  handleInputChange(event) {
    event.preventDefault();
    this.setState({ inputValue: event.target.value });
    console.log(this.state.inputValue);
  }

  handleSumbit(event) {
    event.preventDefault();
    const body = { company: this.state.inputValue };

    event.preventDefault();
    fetch("/investment", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ company: this.state.inputValue })
    })
      .then(data => {
        if (data.status === 200) {
          return data.json;
        } else {
          throw new Error("error cannot get data");
        }
      })
      .then(response => {
        console.log(response);
      })
      .catch(err => {
        console.log("there is an error", err);
      });
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
      </div>
    );
  }
}

export default SearchCompanies;
