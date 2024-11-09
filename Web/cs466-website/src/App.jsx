import React, { useState, useEffect } from 'react';

function ImageComponent() {
  return (
    <div>
      <h2>Global Align</h2>
      {<img src={"http://127.0.0.1:443/global_image"} alt="Global Align"/>}
      <h2>Fitting Align</h2>
      {<img src={"http://127.0.0.1:443/fitting_image"} alt="Fitting Align"/>}
      <h2>Local Image</h2>
      {<img src={"http://127.0.0.1:443/local_image"} alt="Local Align"/>}
    </div>
  );
}

export default ImageComponent;