import {combineReducers} from 'redux';

import { loginReducer } from './loginReducer';
import { chatReducer } from './chatReducer';

export const rootReducer = combineReducers({
    login: loginReducer,
    chat: chatReducer
});