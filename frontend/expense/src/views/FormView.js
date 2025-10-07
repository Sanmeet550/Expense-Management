import React, { useState } from "react";

const DynamicForm = ({ columns, onSubmit }) => {
  // Initialize form state based on columns
  const initialState = columns.reduce((acc, col) => {
    acc[col.key] = "";
    return acc;
  }, {});

  const [formData, setFormData] = useState(initialState);

  const handleChange = (e, key) => {
    setFormData({ ...formData, [key]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
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
      <button type="submit" className="btn btn-primary">
        Submit
      </button>
    </form>
  );
};

export default DynamicForm;
