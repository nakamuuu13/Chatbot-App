import { NavLinks } from '../modules/navigation/NavLinks';
import { Vectorstore } from '../modules/vectorstore/Vectorstore';

import './../../App.css';


export const LeftSidebar = ({ toggleSidebar, isOpen }) => {
    return (
        <div className={`left-sidebar ${isOpen ? 'open' : 'closed'}`}>
            <button className="left-sidebar-toggle-button" onClick={toggleSidebar}>
                {isOpen ? '◀' : '▶'}
            </button>
            <div className="left-sidebar-content">
                <NavLinks />
            </div>
        </div>
    );
};

export const RightSidebar = ({ toggleSidebar, isOpen }) => {
    return (
        <div className={`right-sidebar ${isOpen ? 'open' : 'closed'}`}>
            <button className="right-sidebar-toggle-button" onClick={toggleSidebar}>
                {isOpen ? '▶' : '◀'}
            </button>
            <div className="right-sidebar-content">
                <Vectorstore />
            </div>
        </div>
    );
};


