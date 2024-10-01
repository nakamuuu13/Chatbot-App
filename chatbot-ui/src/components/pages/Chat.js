import React, { useState } from 'react';
import { Navheader } from "../header/Navheader";
import { ChatUiKit } from "../modules/chat/ChatUiKit";
import { RightSidebar, LeftSidebar } from "../sidebar/Sidebar";

import './../../App.css';

export const Chat = () => {
    const [isRightSidebarOpen, setIsRightSidebarOpen] = useState(false);
    const [isLeftSidebarOpen, setIsLeftSidebarOpen] = useState(false);

    // サイドバーの開閉状態を切り替える関数
    const toggleRightSidebar = () => {
        setIsRightSidebarOpen(!isRightSidebarOpen);
    };
    const toggleLeftSidebar = () => {
        setIsLeftSidebarOpen(!isLeftSidebarOpen);
    };

    return (
        <div>
            {/* <Navheader /> */}
            <div className="chat-container">
                <LeftSidebar toggleSidebar={toggleLeftSidebar} isOpen={isLeftSidebarOpen} />
                <ChatUiKit isRightSidebarOpen={isRightSidebarOpen} isLeftSidebarOpen={isLeftSidebarOpen} />
                <RightSidebar toggleSidebar={toggleRightSidebar} isOpen={isRightSidebarOpen} />
            </div>
        </div>
    );
};
