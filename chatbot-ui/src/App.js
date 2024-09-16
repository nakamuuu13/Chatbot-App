import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Login } from './components/pages/Login';
import { Chat } from './components/pages/Chat';

import './App.css';

export const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/chat" element={<Chat />} />
      </Routes>
    </Router>
  );
}