import { DIALOG_OPEN } from "../actions/vectorStoreAction";

const initialState = {
    dialogOpen: false
};

export const vectorStoreReducer = (state = initialState, action) => {
    switch (action.type) {
        case DIALOG_OPEN:
            return {
                ...state,
                dialogOpen: action.payload
            };
        default:
            return state;
    }
}