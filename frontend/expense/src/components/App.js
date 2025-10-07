import React from "react";
import { Outlet, NavLink } from "react-router";

export default function App() {
  return (
    <div className="d-flex" style={{ height: "100vh" }}>
      {/* Sidebar */}
      <div className="bg-dark text-white p-3" style={{ width: "250px" }}>
        <h3 className="text-center">💰 Expenses</h3>
        <ul className="nav flex-column mt-4">
          <li className="nav-item">
            <NavLink to="/" end className="nav-link text-white">
              Dashboard
            </NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/expense" className="nav-link text-white">
              Expenses
            </NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/expense-report" className="nav-link text-white">
              Reports
            </NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/department" className="nav-link text-white">
              Department
            </NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/settings" className="nav-link text-white">
              Settings
            </NavLink>
          </li>
        </ul>
      </div>

      {/* Main Content Area */}
      <div className="flex-grow-1 d-flex flex-column">
        {/* Header */}
        <header className="bg-light p-3 border-bottom">
          <h4>Expense Management System</h4>
        </header>

        {/* Dynamic Content */}
        <main className="p-4" style={{ overflowY: "auto" }}>
          <Outlet />
        </main>
      </div>
    </div>
  );
}
