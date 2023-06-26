const exampleFetch = () => {
  fetch(requestOptions)
    .then((response) => response.json())
    .then((data) => this.setState());
};

export default exampleFetch;
