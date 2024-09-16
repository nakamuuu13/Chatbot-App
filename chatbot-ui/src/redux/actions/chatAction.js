export const SEND_MESSAGE = 'SEND_MESSAGE';
export const RESPONSE_MESSAGE = 'RESPONSE_MESSAGE';
export const RESPONSE_MESSAGE_STREAM = 'RESPONSE_MESSAGE_STREAM';
export const SET_LOADING = 'SET_LOADING';

export const sendMessage = (message) => ({
    type: SEND_MESSAGE,
    payload: message,
});

export const responseMessage = (message) => ({
    type: RESPONSE_MESSAGE,
    payload: message,
});

export const responseMessageStream = (message) => ({
    type: RESPONSE_MESSAGE_STREAM,
    payload: message,
});

export const setLoading = (isLoading) => ({
    type: SET_LOADING,
    payload: isLoading,
});