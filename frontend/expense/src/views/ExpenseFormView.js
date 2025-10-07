import React, { useEffect } from "react";
import { useLocation, useNavigate } from "react-router";
import DynamicForm from "./FormView";

export default function ExpenseFormView() {
  const location = useLocation();
  const navigate = useNavigate();

  const columns = location.state?.columns || [];
  const fastApi = process.env.REACT_APP_FASTAPI_URL;

  const handleSubmit = async (formData) => {
    console.log("Form submitted:", formData);

    // Example: call your FastAPI endpoint
    try {
      const res = await fetch(`${fastApi}/expense-category/create`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });
      const result = await res.json();
      console.log("Saved:", result);
      navigate(-1); // go back to the list page
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="container mt-4">
      <h3>New Record</h3>
      <DynamicForm columns={columns} onSubmit={handleSubmit} />
    </div>
  );
}
