import React, { useState } from "react";
import "./App.css";

function App() {

  const [formData, setFormData] = useState({
    Age: "",
    CGPA: "",
    Internships: "",
    Projects: "",
    Backlogs: ""
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
  };

  return (
    <div className="container">
      <h2>Student Placement Prediction</h2>

      <form onSubmit={handleSubmit}>

        <input
          type="number"
          name="Age"
          placeholder="Age"
          onChange={handleChange}
        />

        <input
          type="number"
          name="CGPA"
          placeholder="CGPA"
          onChange={handleChange}
        />

        <input
          type="number"
          name="Internships"
          placeholder="Internships"
          onChange={handleChange}
        />

        <input
          type="number"
          name="Projects"
          placeholder="Projects"
          onChange={handleChange}
        />

        <input
          type="number"
          name="Backlogs"
          placeholder="Backlogs"
          onChange={handleChange}
        />

        <button type="submit">Predict</button>

      </form>

    </div>
  );
}

export default App;