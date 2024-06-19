// internal use variables
const apiPort = process.env.REACT_APP_API_PORT;

// outside use variables
const config = {
  apiPort: apiPort,
  apiURL: `http://localhost:${apiPort}`,
};

export default config;
