import React, { useState, useEffect } from 'react';

function App() {
    const [message, setMessage] = useState('');

    useEffect(() => {
        // Use the backend URL from the environment variable
        const backendUrl = process.env.REACT_APP_BACKEND_URL;

        fetch(backendUrl)
            .then(response => response.json())
            .then(data => setMessage(data.message))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>React Frontend</h1>
            <p>Message from Flask Backend:</p>
            <h2>{message || 'Loading...'}</h2>
        </div>
    );
}

export default App;
