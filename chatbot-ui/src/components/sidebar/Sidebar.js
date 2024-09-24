import './../../App.css';


export const LeftSidebar = ({ toggleSidebar, isOpen }) => {
    return (
        <div className={`left-sidebar ${isOpen ? 'open' : 'closed'}`}>
            <button className="left-sidebar-toggle-button" onClick={toggleSidebar}>
                {isOpen ? '◀' : '▶'}
            </button>
            <div className="left-sidebar-content">
                <h2>Left Sidebar</h2>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                    <li>Item 3</li>
                </ul>
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
                <h2>Right Sidebar</h2>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                    <li>Item 3</li>
                </ul>
            </div>
        </div>
    );
};


