import React, { useState } from "react";

import axios from "axios";

function Home() {
  const [input, setInput] = useState("");
  const [data, setData] = useState(null);

  const fetchFibData = async () => {
    try{
      const { data } = await axios.get(`/api/fib`, {
        params: {
          n: input
        }
      })
      setData(data)
      console.log(data)
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
        <button type="button" onClick={fetchFibData}>Get Data</button>
        <div>
        {data && data.map((item, index) => (
          <p key={index}>{item}</p>
            ))}
        </div>
      </form>
    </div>
  )
}
export default Home;
