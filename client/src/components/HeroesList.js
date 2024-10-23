import React, { useEffect, useState } from "react";

function HeroesList() {
  const [heroes, setHeroes] = useState([]);

  useEffect(() => {
    const fetchHeroes = async () => {
      try {
        const response = await fetch("http://localhost:6000/heroes"); // Adjust the URL if needed
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const data = await response.json();
        setHeroes(data); // Assuming the response returns an array of heroes
      } catch (error) {
        console.error("Error fetching heroes:", error);
      }
    };

    fetchHeroes();
  }, []);

  return (
    <div>
      <h1>Heroes List</h1>
      <ul>
        {heroes.map((hero) => (
          <li key={hero.id}>
            {hero.name} ({hero.super_name})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default HeroesList;
