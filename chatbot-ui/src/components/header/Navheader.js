import React from 'react';
import { Link } from 'react-router-dom';

import './../../App.css';

export const Navheader = () => {
    return (
        <div className="Nav-header">
            <Link to="/" className="Nav-logo">Chat App</Link>
            <ul className="nav-links">
                <li><Link to="/chat">Chat</Link></li>
                <li><Link to="/vectorstore">Vectorstore</Link></li>
            </ul>
        </div>
    )
}