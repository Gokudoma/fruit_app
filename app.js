const API_URL = '[http://127.0.0.1:8000/api/fruits/](http://127.0.0.1:8000/api/fruits/)';
const fruitListContainer = document.getElementById('fruit-list');
const addFruitForm = document.getElementById('add-fruit-form');

const fetchFruits = async () => {
    const response = await fetch(API_URL);
    const fruits = await response.json();
    
    fruitListContainer.innerHTML = ''; // Liste leeren

    fruits.forEach(fruit => {
        const fruitElement = document.createElement('div');
        fruitElement.innerHTML = `
            <h3>${fruit.name} (${fruit.brand})</h3>
            <p><strong>Farbe:</strong> ${fruit.color}</p>
            <p><strong>Herkunft:</strong> ${fruit.origin}</p>
        `;
        fruitListContainer.appendChild(fruitElement);
    });
};

addFruitForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const newFruit = {
        name: document.getElementById('name').value,
        color: document.getElementById('color').value,
        brand: document.getElementById('brand').value,
        origin: document.getElementById('origin').value,
    };

    await fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newFruit),
    });

    addFruitForm.reset();
    fetchFruits(); // Liste neu laden
});

// Initiales Laden der Früchte
fetchFruits();
