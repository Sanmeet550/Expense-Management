import { BrowserRouter, Routes, Route } from "react-router";
import App from "./components/App";
import Dashboard from "./components/Dashboard";
import Department from "./components/Department";
import Expense from "./components/Expense";
import ExpenseReport from "./components/ExpenseReport";
import DepartmentFormView from "./views/DepartmentFormView";
import ExpenseFormView from "./views/ExpenseFormView";
import FormView from "./views/FormView";

function projectRoute() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />}>
          <Route index element={<Dashboard />} />
          <Route path="/expense" element={<Expense />} />
          <Route path="/expense-report" element={<ExpenseReport />} />
          // Department
          <Route path="/department" element={<Department />} />
          // View button
          <Route path="/new" element={<FormView />} />
          // Department form
          <Route path="/department/form" element={<DepartmentFormView />} />
          //Expense form
          <Route path="/expense/form" element={<ExpenseFormView />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default projectRoute;
