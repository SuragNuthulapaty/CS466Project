import React, { useState, useEffect } from 'react';

function ImageComponent() {
  const [imageUrl, setImageUrl] = useState('');

  useEffect(() => {
    fetch('http://localhost:443/local_image')
      .then(response => response.text())
      .then(html => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const imgSrc = doc.querySelector('img').src;
        setImageUrl(imgSrc);
        console.log(imgSrc)
      })
      .catch(error => console.error('Error fetching image:', error));
  }, []);

  return (
    <div>
      <h2>Local Image</h2>
      {imageUrl && <img src={"http://localhost:443/local_image"} alt="Local Align" />}
      
       {/* <div dangerouslySetInnerHTML={{__html: '<strong>strong text</strong>'}} /> */}
    </div>
  );
}

export default ImageComponent;