import {combineReducers} from 'redux';

import { loginReducer } from './loginReducer';
import { chatReducer } from './chatReducer';
import { dialogReducer } from './dialogReducer';

export const rootReducer = combineReducers({
    login: loginReducer,
    chat: chatReducer,
    dialog: dialogReducer
});