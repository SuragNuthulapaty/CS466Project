import React, { useState, useEffect } from 'react';

function ImageComponent() {
  const [globalSrc, setGlobalSrc] = useState("http://127.0.0.1:443/global_image");
  const [locallSrc, setLocalSrc] = useState("http://127.0.0.1:443/local_image");
  const [fittingSrc, setFittingSrc] = useState("http://127.0.0.1:443/fitting_image");

  const updateImage = () => {
    // Update the image src here
    setGlobalSrc(`http://127.0.0.1:443/global_image?timestamp=${new Date().getTime()}`);
    setLocalSrc(`http://127.0.0.1:443/local_image?timestamp=${new Date().getTime()}`);
    setFittingSrc(`http://127.0.0.1:443/fitting_image?timestamp=${new Date().getTime()}`);
  };

  return (
    <div>
      <button onClick={updateImage}>BTN</button>
      <h2>Global Align</h2>
      {<img key={globalSrc} src={globalSrc} alt="Global Align"/>}
      <h2>Fitting Align</h2>
      {<img key={fittingSrc} src={fittingSrc} alt="Fitting Align"/>}
      <h2>Local Image</h2>
      {<img key={locallSrc} src={locallSrc} alt="Local Align"/>}
    </div>
  );
}

export default ImageComponent;