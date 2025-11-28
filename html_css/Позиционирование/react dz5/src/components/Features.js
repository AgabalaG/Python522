import React from 'react';

const Features = () => {
  const features = [
    {
      title: 'Продажа велосипедов',
      description: 'Широкий выбор горных, шоссейных и городских велосипедов'
    },
    {
      title: 'Ремонт и обслуживание',
      description: 'Профессиональный ремонт и регулярное техническое обслуживание'
    },
    {
      title: 'Аксессуары',
      description: 'Все необходимые аксессуары для комфортной езды'
    }
  ];

  return (
    <section className="features" id="features">
      <h2>Наши услуги</h2>
      <div className="features-grid">
        {features.map((feature, index) => (
          <div key={index} className="feature-card">
            <h3>{feature.title}</h3>
            <p>{feature.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Features;
