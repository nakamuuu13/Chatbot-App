export const DIALOG_OPEN = 'DIALOG_OPEN';
export const FILES = 'FILES';
export const NAME = 'NAME';
export const CREATE = 'CREATE';

export const setOpen = (dialogOpen) => {
    return {
        type: DIALOG_OPEN,
        payload: dialogOpen
    }
};

export const setFiles = (files) => {
    return {
        type: FILES,
        payload: files
    }
};

export const setName = (name) => {
    return {
        type: NAME,
        payload: name
    }
}

export const setCreate = (create) => {
    return {
        type: CREATE,
        payload: create
    }
}