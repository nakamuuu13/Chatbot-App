import { DIALOG_OPEN } from "../actions/dialogAction";

const initialState = {
    dialogOpen: false
};

export const dialogReducer = (state = initialState, action) => {
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