export const DIALOG_OPEN = 'DIALOG_OPEN';

export const setOpen = (dialogOpen) => {
    return {
        type: DIALOG_OPEN,
        payload: dialogOpen
    }
};