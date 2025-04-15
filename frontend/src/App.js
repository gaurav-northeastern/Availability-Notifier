// React component that sends updated POST body for visa appointment monitoring
import { useState } from "react";

function App() {
  const [email, setEmail] = useState("");
  const [visaType, setVisaType] = useState("table_B1B2Regular");
  const [location, setLocation] = useState("NEW DELHI");
  const [vac, setVac] = useState(false);
  const [message, setMessage] = useState("");

  const handleSubmit = () => {
    const payload = {
      email,
      visaType,
      location,
      vac,
    };

    fetch("http://localhost:5050/start", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    })
      .then((res) => res.json())
      .then((data) => setMessage(data.message || JSON.stringify(data)))
      .catch((err) => {
        console.error("Fetch error:", err);
        setMessage("Failed to start the checker");
      });
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
      <h1 className="text-3xl font-bold mb-6">Visa Notifier Setup</h1>

      <input
        type="email"
        placeholder="Enter your email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        className="p-2 mb-4 border rounded w-full max-w-md"
      />

      <div className="mb-4">
        <p className="font-semibold mb-2">Select Visa Type:</p>
        <label className="mr-4">
          <input
            type="radio"
            name="visaType"
            value="table_B1B2Regular"
            checked={visaType === "table_B1B2Regular"}
            onChange={(e) => setVisaType(e.target.value)}
          />{" "}
          B1/B2
        </label>
        <label className="mr-4">
          <input
            type="radio"
            name="visaType"
            value="table_F1Regular"
            checked={visaType === "table_F1Regular"}
            onChange={(e) => setVisaType(e.target.value)}
          />{" "}
          F1
        </label>
        <label>
          <input
            type="radio"
            name="visaType"
            value="table_F2Regular"
            checked={visaType === "table_F2Regular"}
            onChange={(e) => setVisaType(e.target.value)}
          />{" "}
          F2
        </label>
      </div>

      <div className="mb-4">
        <p className="font-semibold mb-2">Select Location:</p>
        <select
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          className="p-2 border rounded w-full max-w-md"
        >
          <option value="CHENNAI">CHENNAI</option>
          <option value="HYDERABAD">HYDERABAD</option>
          <option value="KOLKATA">KOLKATA</option>
          <option value="MUMBAI">MUMBAI</option>
          <option value="NEW DELHI">NEW DELHI</option>
        </select>
      </div>

      <div className="mb-6">
        <label className="inline-flex items-center">
          <input
            type="checkbox"
            checked={vac}
            onChange={(e) => setVac(e.target.checked)}
            className="mr-2"
          />
          Include VAC Appointments
        </label>
      </div>

      <button
        onClick={handleSubmit}
        className="bg-blue-600 text-white font-semibold px-6 py-2 rounded shadow hover:bg-blue-700"
      >
        Start Checker
      </button>

      {message && (
        <div className="mt-4 p-4 bg-white rounded shadow text-center w-full max-w-md">
          <p className="text-gray-800">{message}</p>
        </div>
      )}
    </div>
  );
}

export default App;
