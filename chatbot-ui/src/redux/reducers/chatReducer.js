import { SEND_MESSAGE, RESPONSE_MESSAGE, RESPONSE_MESSAGE_STREAM, SET_LOADING } from './../actions/chatAction';
const initialChatState = {
    userMessages: [],
    aiMessages: [],
    isLoading: false,
};

export const chatReducer = (state = initialChatState, action) => {
    switch (action.type) {
        // userのメッセージはこれまでのstateを保持
        case SEND_MESSAGE:
            return {
                ...state, 
                userMessages: [...state.userMessages, action.payload]
            };
        // AIのメッセージは最初の回答のみ全てのstateを保持
        case RESPONSE_MESSAGE:
            return {
                ...state, 
                aiMessages: [...state.aiMessages, action.payload]
            };
        // 2回目以降のメッセージは最後の要素以外のstateを保持
        case RESPONSE_MESSAGE_STREAM:
            return {
                ...state,
                aiMessages: [
                    ...state.aiMessages.slice(0, -1),
                    action.payload
                ]
            };
        case SET_LOADING:
            return {
                ...state, 
                isLoading: [action.payload]
            };
        default:
            return state;
    }
};