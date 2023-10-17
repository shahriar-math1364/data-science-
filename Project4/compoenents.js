import React from 'react';

const DragAndDropArea = () => {
  const handleDrop = (e) => {
    e.preventDefault();
    const file = e.dataTransfer.files[0];
    if (file) {
      // Upload the image to the FastAPI backend
      uploadImage(file);
    }
  };

  const allowDrop = (e) => {
    e.preventDefault();
  };

  const uploadImage = async (file) => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('/upload/', {
        method: 'POST',
        body: formData,
      });
      if (response.ok) {
        const data = await response.json();
        // Handle the inference result here
        console.log(data.result);
      }
    } catch (error) {
      console.error('Error uploading image:', error);
    }
  };

  return (
    <div
      onDragOver={allowDrop}
      onDrop={handleDrop}
      style={{ border: '2px dashed #ccc', padding: '20px' }}
    >
      <p>Drag and drop a potato plant leaf image here.</p>
    </div>
  );
};

export default DragAndDropArea;
