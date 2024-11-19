import React, { useState, useEffect } from 'react';

function ImageComponent() {
  const [globalSrc, setGlobalSrc] = useState("");
  const [locallSrc, setLocalSrc] = useState("");
  const [fittingSrc, setFittingSrc] = useState("");

  const [text1, setText1] = useState("")
  const [text2, setText2] = useState("")

  const [data, SetData] = useState({})

  const updateImage = () => {
    // Update the image src here
    setGlobalSrc(`http://127.0.0.1:443/global_image?timestamp=${new Date().getTime()}`);
    setLocalSrc(`http://127.0.0.1:443/local_image?timestamp=${new Date().getTime()}`);
    setFittingSrc(`http://127.0.0.1:443/fitting_image?timestamp=${new Date().getTime()}`);
  };

  const get_submit = () => {
    let sending = {
      "text1": text1,
      "text2": text2,
    }

    console.log(sending)
    fetch("http://127.0.0.1:443/submit", {
      method: "POST",
      body: JSON.stringify(sending),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    }).then(json_data => {
      json_data.text().then(response => SetData(response))
    }).then( json_data => {
      updateImage()
      console.log(data)
      console.log(globalSrc)
      console.log(fittingSrc)
      console.log(locallSrc)
    }).catch((err) => {
        console.log("err fetch", err)
    });
  }


  return (
    <div>
      <button onClick={() => get_submit()}>BTN</button>
      <input value={text1} onChange={(e)=>setText1(e.target.value)}/>
      <input value={text2} onChange={(e)=>setText2(e.target.value)}/>
      {/* <p>{data}</p> */}
    
      {globalSrc ? <h2>Global Align</h2> : <div></div>}
      {globalSrc ? <img key={globalSrc} src={globalSrc} alt="Global Align" loading="lazy"/> : <div></div>}
      {globalSrc ? <h2>Fitting Align</h2> : <div></div>}
      {globalSrc ? <img key={fittingSrc} src={fittingSrc} alt="Fitting Align" loading="lazy"/> : <div></div>}
      {globalSrc ? <h2>Local Image</h2> : <div></div>}
      {globalSrc ? <img key={locallSrc} src={locallSrc} alt="Local Align" loading="lazy"/> : <div></div>}
    </div>
  );
}

export default ImageComponent;