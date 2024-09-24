import { MainContainer, ChatContainer, MessageList, Message, MessageInput, Avatar } from '@chatscope/chat-ui-kit-react';
import { useSelector, useDispatch } from 'react-redux';
import { sendMessage, responseMessage, responseMessageStream, setLoading } from '../../../redux/actions/chatAction';

import { POST } from '../../../apis/api';

import styles from "@chatscope/chat-ui-kit-styles/dist/default/styles.min.css";
import logo from './ai_logo.png';

export const ChatUiKit = ({ isRightSidebarOpen, isLeftSidebarOpen }) => {
    const dispatch = useDispatch();
    const { userMessages, aiMessages, isLoading } = useSelector((state) => state.chat);

    // 送信ボタンを押したときの処理
    const handleSendMessage = (text) => {
        const newMessage = {
            message: text,
            sentTime: "just now",
            sender: "User",
            position: "normal",
            direction: "outgoing"
        };
        dispatch(sendMessage(newMessage));
        handleReplyStream(text);
    };

    // メッセージを受け取り初回の処理
    const handleResponseMessage = (text) => {
        const newMessage = {
            message: text,
            sentTime: "just now",
            sender: "AI",
            position: "normal",
            direction: "incoming"
        };
        dispatch(responseMessage(newMessage));
    };

    // メッセージを受け取り2回目以降の処理
    const handleResponseMessageStream = (text) => {
        const newMessage = {
            message: text,
            sentTime: "just now",
            sender: "AI",
            position: "normal",
            direction: "incoming"
        };
        dispatch(responseMessageStream(newMessage));
    }

    // メッセージを受け取ったときの処理
    const handleReplyStream = async (text) => {
        try {
            dispatch(setLoading(true));
            const data = { text: text,
                           response_type: "stream" };
            await POST("/api/chat/create_response", data, {
                handleResponseMessage,
                handleResponseMessageStream
            });
        } catch (error) {
            console.error("handleReplyStream error", error);
            handleResponseMessage("Error from server");
        } finally {
            dispatch(setLoading(false));
        }
    };

    // user と AI のメッセージをまとめる
    const messages = [];
    const maxLength = userMessages.length;

    for (let i = 0; i < maxLength; i++) {
        if (i < userMessages.length) {
            messages.push(userMessages[i]);
        }
        if (i < aiMessages.length) {
            messages.push(aiMessages[i]);
        }
    };

    // サイドバーの幅（固定値）
    const sidebarWidth = 250; 

    // 左右のマージンをサイドバーの開閉に応じて計算
    const leftMargin = isLeftSidebarOpen ? `${sidebarWidth}px` : '0';
    const rightMargin = isRightSidebarOpen ? `${sidebarWidth}px` : '0';

    return (
        <div style={{ 
            position: "relative", 
            height: "700px", 
            marginLeft: leftMargin, 
            marginRight: rightMargin, 
            width: `calc(100% - ${isLeftSidebarOpen ? sidebarWidth : 0}px - ${isRightSidebarOpen ? sidebarWidth : 0}px)`
        }}>
            <MainContainer>
                <ChatContainer>
                    <MessageList>
                        {messages.map((msg, index) => (
                            <Message
                                key={index}
                                model={{
                                    message: msg.message,
                                    sentTime: msg.sentTime,
                                    sender: msg.sender,
                                    position: msg.position,
                                    direction: msg.direction
                                }}>
                                {msg.direction === "incoming" && <Avatar src={logo} name="ai_logo" />}
                            </Message>
                        ))}
                    </MessageList>
                    <MessageInput
                        placeholder="ご質問は何でしょうか？"
                        attachButton={true}
                        onSend={handleSendMessage}
                        fancyScroll={false}
                    />
                </ChatContainer>
            </MainContainer>
        </div>
    );
};