import { Link } from 'react-router-dom';

import './../../../App.css';

export const NavLinks = () => {
    return (
        <div className="Nav-links-sidebar">
            <Link to="/" className="Nav-logo">Chat App</Link>
            <li><Link to="/chat">Chat</Link></li>
        </div>
    )
}