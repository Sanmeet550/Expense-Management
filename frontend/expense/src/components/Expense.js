import React, { useState } from "react";
import ListView from "../views/ListView";

export default function Expense() {
  const fastApi = process.env.REACT_APP_FASTAPI_URL;
  return (
    <ListView
      endpoint={`${fastApi}/expense-category/all-category`}
      formpoint={"/expense/form"}
    />
  );
}
