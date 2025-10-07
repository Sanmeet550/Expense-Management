import React, { useEffect, useState } from "react";
import ListView from "../views/ListView";

export default function Department() {
  const fastApi = process.env.REACT_APP_FASTAPI_URL;
  // useEffect(() => {
  //   console.log(fastApi);
  //   const fetchDepartmentList = async () => {
  //     try {
  //       const resp = await fetch();
  //       const data = await resp.json();
  //       console.log(data);
  //     } catch (error) {
  //       console.error("Error Fetching", error);
  //     }
  //   };

  //   fetchDepartmentList();
  // }, []);

  return (
    <ListView
      endpoint={`${fastApi}/department/all_department`}
      formpoint={"/department/form"}
    />
  );
}
