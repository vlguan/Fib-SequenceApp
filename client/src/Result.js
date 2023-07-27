import React from "react";
import { useLocation } from "react-router-dom";
function ResultPage() {
    const location = useLocation();
    const { data } = location.state;
    
  return (
    <div>
      <h1>Fibonacci Sequence Length of {data.length}</h1>
      <div>{data && data.join(", ")}</div>
    </div>
  );
}

export default ResultPage;