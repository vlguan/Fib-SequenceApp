import React, { useState } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import Home from "./Home";
import ResultPage from "./Result";
function App() {
  const [data, setData] = useState(null);
  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'start' }}>
    <BrowserRouter>
    <Routes>
      <Route path='/' element = {<Home setData={setData}/>}/>
      <Route path='/result' element = {<ResultPage data = {data}/>}/>
    </Routes>
    </BrowserRouter>
    </div>
    
  );
}

export default App;
