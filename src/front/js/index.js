//import react into the bundle
import React from "react";
import ReactDOM from "react-dom";
import 'react-toastify/dist/ReactToastify.css';
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" />


//include your index.scss file into the bundle
import "../styles/index.css";

//import your own components
import Layout from "./layout";

const cors = require("cors");


//render your react application
ReactDOM.render(<Layout />, document.querySelector("#app"));
