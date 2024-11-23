import React, { useState } from "react";
import PosMapTable from "./PosMapTable"

const App = () => {
  const [text1, setText1] = useState("");
  const [text2, setText2] = useState("");
  const [globalSrc, setGlobalSrc] = useState("");
  const [localSrc, setLocalSrc] = useState("");
  const [fittingSrc, setFittingSrc] = useState("");
  const [responseData, setResponseData] = useState({});
  const [has_data, setHasData] = useState(false);

  const updateImage = () => {
    setGlobalSrc(`http://127.0.0.1:443/global_image?timestamp=${new Date().getTime()}`);
    setLocalSrc(`http://127.0.0.1:443/local_image?timestamp=${new Date().getTime()}`);
    setFittingSrc(`http://127.0.0.1:443/fitting_image?timestamp=${new Date().getTime()}`);
  };

  const handleSubmit = () => {
    if (text1 == "" || text2 == "") {
      return 
    }

    const payload = {
      text1,
      text2,
    };

    fetch("http://127.0.0.1:443/submit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    })
      .then(response => response.json())
      .then((data) => {
        setResponseData(data);
        setHasData(true)
        updateImage()
        console.log(data)
      })
      .catch((error) => console.error("Error:", error));
  };

  return (
    <div style={{ fontFamily: "Arial, sans-serif", padding: "20px", justifyContent: 'start' }}>
      <h1>Syntatic Text Alignment</h1>
      <div style={{ marginBottom: "20px" }}>
        <textarea
          rows={5}
          placeholder="Enter first large text"
          style={{ width: "100%", marginBottom: "10px", padding: "10px" }}
          value={text1}
          onChange={(e) => setText1(e.target.value)}
        />
        <textarea
          rows={5}
          placeholder="Enter second large text"
          style={{ width: "100%", marginBottom: "10px", padding: "10px" }}
          value={text2}
          onChange={(e) => setText2(e.target.value)}
        />
        <button
          onClick={handleSubmit}
          style={{
            padding: "10px 20px",
            backgroundColor: "#007BFF",
            color: "white",
            border: "none",
            cursor: "pointer",
          }}
        >
          Submit
        </button>
      </div>
      
      {has_data && (
      <div style={{justifyContent: 'start', width: '1000px'}}>
        <PosMapTable/>
      <h2>Parsed Strings:</h2>
      <h3>Text Input 1</h3>
      {responseData && 
        <div style={{display: 'flex', flexDirection: 'row', alignItems:'center', padding: '0px'}}>
        <div style={{display: 'flex', flexDirection: 'column', marginLeft: '20px', marginRight: '20px'}}>
          <h3>Token in Speech</h3>
          <h3>Part of Speech</h3>
        </div>
        {responseData['t1'].map((data) => {
          return (
            <div style={{display: 'flex', flexDirection: 'column', marginLeft: '15px'}}>
              <p>{data[0]}</p>
              <p>{data[1]}</p>
            </div>
          )
        })}
      </div>
      }

  <h3>Text Input 2</h3>
      {responseData && 
        <div style={{display: 'flex', flexDirection: 'row', alignItems:'center', padding: '0px'}}>
        <div style={{display: 'flex', flexDirection: 'column', marginLeft: '20px', marginRight: '20px'}}>
          <h3>Token in Speech</h3>
          <h3>Part of Speech</h3>
        </div>
        {responseData['t2'].map((data) => {
          return (
            <div style={{display: 'flex', flexDirection: 'column', marginLeft: '15px'}}>
              <p>{data[0]}</p>
              <p>{data[1]}</p>
            </div>
          )
        })}
      </div>
      }

      <div >
        {globalSrc && (
          <div style={{ textAlign: "center" }}>
            <h2>Global Align</h2>
            <img
              key={globalSrc}
              src={globalSrc}
              alt="Global Align"
              style={{ width: "min(80%, 1000px)"}}
              loading="lazy"
            />
          </div>
        )}
        {fittingSrc && (
          <div style={{ textAlign: "center" }}>
            <h2>Fitting Align</h2>
            <img
              key={fittingSrc}
              src={fittingSrc}
              alt="Fitting Align"
              style={{ width: "min(80%, 1000px)"}}
              loading="lazy"
            />
          </div>
        )}
        {localSrc && (
          <div style={{ textAlign: "center" }}>
            <h2>Local Align</h2>
            <img
              key={localSrc}
              src={localSrc}
              alt="Local Align"
              style={{ width: "min(80%, 1000px)"}}
              loading="lazy"
            />
          </div>
        )}
      </div>
      </div>
      )}
    </div>
  );
};

export default App;

