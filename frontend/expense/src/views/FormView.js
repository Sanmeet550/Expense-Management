import React, { useState } from "react";
import { useLocation, useNavigate } from "react-router";

const DynamicFormPage = ({ defaultEndpoint }) => {
  const location = useLocation();
  const navigate = useNavigate();

  // Get columns and optionally endpoint from state
  const columns = location.state?.columns || [];
  const endpoint = location.state?.createpoint || defaultEndpoint;
  console.log(location);

  // Initialize form state dynamically based on columns
  const initialFormData = columns.reduce((acc, col) => {
    acc[col.key] = "";
    return acc;
  }, {});

  const [formData, setFormData] = useState(initialFormData);

  const handleChange = (e, key) => {
    setFormData({ ...formData, [key]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });
      const result = await res.json();
      console.log("Saved:", result);
      navigate(-1); // go back to the list page
    } catch (err) {
      console.error("Error submitting form:", err);
    }
  };

  return (
    <div className="container mt-4">
      <h3>New Record</h3>
      <form onSubmit={handleSubmit}>
        {columns.map((col) => (
          <div className="mb-3" key={col.key}>
            <label className="form-label">{col.label}</label>
            <input
              type="text"
              className="form-control"
              value={formData[col.key]}
              onChange={(e) => handleChange(e, col.key)}
            />
          </div>
        ))}
        <button type="submit" className="btn btn-primary me-2">
          Submit
        </button>
        <button
          type="button"
          className="btn btn-secondary"
          onClick={() => navigate(-1)}
        >
          Cancel
        </button>
      </form>
    </div>
  );
};

export default DynamicFormPage;
