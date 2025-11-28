import React from 'react';

const Gallery = () => {
  const galleryItems = [
    'Горный велосипед',
    'Шоссейный велосипед',
    'Городской велосипед',
    'Электрический велосипед',
    'Детский велосипед',
    'Велосипедные аксессуары'
  ];

  return (
    <section className="gallery" id="gallery">
      <h2>Наша продукция</h2>
      <div className="gallery-grid">
        {galleryItems.map((item, index) => (
          <div key={index} className="gallery-item">
            {item}
          </div>
        ))}
      </div>
    </section>
  );
};

export default Gallery;
