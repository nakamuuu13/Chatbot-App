import React, { useState, useEffect } from 'react';
import './App.css';

import axios from 'axios';

export function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    // FlaskバックエンドのエンドポイントにGETリクエストを送信
    axios.get('http://localhost:5001/api/helloworld')
      .then((response) => {
        setMessage(response.data.message);
      })
      .catch((error) => {
        console.error('There was an error!', error);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>chatbot-ui</h1>
        <p>{message}</p>
      </header>
    </div>
  );
}