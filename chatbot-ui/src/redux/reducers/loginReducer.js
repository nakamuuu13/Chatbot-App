import { LOGIN_STATE } from '../actions/loginAction';

const initialState = {
    loginState: false
};

export const loginReducer = (state = initialState, action) => {
    switch (action.type) {
        case LOGIN_STATE:
            return {
                ...state,
                loginState: action.payload
            };
        default:
            return state;
    }
};