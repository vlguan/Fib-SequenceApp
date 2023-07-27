import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

import axios from "axios";

function Home() {
  const [input, setInput] = useState("");
  const [data, setData] = useState(null);
  const [error, setError] = useState("");
  const navigate = useNavigate();
  const fetchFibData = async () => {
    try{
      setError("")
      const n = parseInt(input, 10);
      if (isNaN(n) || n < 0){
        setError("Please enter a non-negative integer.");
        setData(null)
        return;
      }
      const { data } = await axios.get(`/api/fib`, {
        params: {
          n: input
        }
      })
      if (!error){
        navigate('/result',{ state:{ data } });
      }
    } catch(error){
      console.error(error)
    }
  };
  const handleInputChange = (e) => {
    setInput(e.target.value);
  }
  return (
    <div>
      <form>
        <div>
          <label>
            Input your Number 
          </label>
          <input type="text"
            id="n"
            value={input} 
            onChange={handleInputChange}></input>
        </div>
        {error && <p style={{ color: "red" }}>{error}</p>}
        {input < 0 && <div style={{ color: "red" }}>Please use a positive number.</div>}
        <button type="button" onClick={fetchFibData}>Get Data</button>
      </form>
    </div>
  )
}
export default Home;
