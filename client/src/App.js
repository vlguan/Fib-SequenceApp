import React from "react";
import { BrowserRouter } from "react-router-dom";

import Home from "./Home";
function App() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'start' }}>
    <BrowserRouter>
      <Home />
    </BrowserRouter>
    </div>
    
  );
}

export default App;
