export const LOGIN_STATE = "LOGIN_STATE";

export const setLoginState = (loginState) => {
    return {
        type: LOGIN_STATE,
        payload: loginState
    }
};