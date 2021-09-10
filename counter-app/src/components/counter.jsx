import React, { Component } from "react";

class Counter extends React.Component {
  state = {
    count: 0,
    tags: [],
  };

  renderTags() {
    if (this.state.tags.length === 0) return <p>There are no tags!!</p>;
    return (
      <ul>
        {this.state.tags.map((tag) => (
          <li key={tag}>{tag}</li>
        ))}
      </ul>
    );
  }
  render() {
    return (
      <React.Fragment>
        <div>
          {this.state.tags.length == 0 && "Please create a new tag!"}
          {this.renderTags()}
        </div>
      </React.Fragment>
    );
  }
}

export default Counter;
