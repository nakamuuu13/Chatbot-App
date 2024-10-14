import { DIALOG_OPEN, FILES, NAME, CREATE } from "../actions/vectorStoreAction";

const initialState = {
    dialogOpen: false,
    files: [],
    name: '',
    create: false
};

export const vectorStoreReducer = (state = initialState, action) => {
    switch (action.type) {
        case DIALOG_OPEN:
            return {
                ...state,
                dialogOpen: action.payload
            };
        case FILES:
            return {
                ...state,
                files: action.payload
            };
        case NAME:
            return {
                ...state,
                name: action.payload
            };
        case CREATE:
            return {
                ...state,
                create: action.payload
            };
        default:
            return state;
    }
}