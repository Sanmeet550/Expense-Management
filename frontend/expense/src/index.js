import ReactDOM from "react-dom/client";
import App from "./components/App";
import projectRoute from "./Routes";
import "bootstrap/dist/css/bootstrap.min.css";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(projectRoute());
