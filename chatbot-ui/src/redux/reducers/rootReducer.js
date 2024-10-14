import {combineReducers} from 'redux';

import { loginReducer } from './loginReducer';
import { chatReducer } from './chatReducer';
import { vectorStoreReducer } from './vectorStoreReducer';

export const rootReducer = combineReducers({
    login: loginReducer,
    chat: chatReducer,
    vectorStore: vectorStoreReducer
});