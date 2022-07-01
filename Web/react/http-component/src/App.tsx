import React, { useEffect, useState } from "react";
import "./App.css";

import Get from "./component/Get.jsx";

function App() {
  return (
    <Get
      url="http://localhost:3000/api/zhihu"
      loading={() => {
        return (
          <div className="container">
            <h1 className="text">Loading...</h1>
          </div>
        );
      }}
      error={(err) => {
        <div className="container">
          <h1 className="error">{err.message}</h1>
        </div>;
      }}
    >
      {(data) => {
        return (
          <div className="container">
            <h1 className="emoji">{data.greeting.emoji}</h1>
            <h1 className="text">{data.greeting.text}</h1>
          </div>
        );
      }}
    </Get>
  );
}

export default App;
