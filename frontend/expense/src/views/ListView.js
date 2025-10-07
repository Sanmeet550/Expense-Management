import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router";

const ListView = ({ endpoint, formpoint }) => {
  const navigate = useNavigate();
  const [data, setData] = useState([]);
  const [columns, setColumns] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    console.log(endpoint, "End");
    const fetchData = async () => {
      try {
        const res = await fetch(endpoint);
        const jsonData = await res.json();
        setData(jsonData);

        // Dynamically generate columns from first row
        if (jsonData.length > 0) {
          const cols = Object.keys(jsonData[0]).map((key) => ({
            key,
            label: key.charAt(0).toUpperCase() + key.slice(1),
          }));
          setColumns(cols);
        }
      } catch (err) {
        console.error("Error fetching data:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [endpoint]);

  if (loading) return <p>Loading...</p>;

  if (data.length === 0) return <p>No data found</p>;

  return (
    <div className="container mt-4">
      <div className="d-flex justify-content-between align-items-center mb-2">
        <h3>List</h3>
        <button
          className="btn btn-success"
          onClick={() => navigate(formpoint, { state: { columns } })}
        >
          New
        </button>
      </div>

      {data.length === 0 ? (
        <p>No data found</p>
      ) : (
        <div className="table-responsive">
          <table className="table table-hover align-middle">
            <thead className="table-light">
              <tr>
                {columns.map((col) => (
                  <th key={col.key}>{col.label}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {data.map((row, idx) => (
                <tr key={idx}>
                  {columns.map((col) => (
                    <td key={col.key}>{row[col.key]}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default ListView;
