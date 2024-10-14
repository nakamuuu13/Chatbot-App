import { useDispatch } from 'react-redux';
import Button from '@mui/material/Button';

import { setOpen, setFiles, setName } from '../../../redux/actions/vectorStoreAction';

export const NewVectorstore = () => {

    const dispatch = useDispatch();

    const handleNewVectorstore = () => {
        dispatch(setOpen(true));
        dispatch(setFiles([]));
        dispatch(setName(''));
    };

    return (
        <div>
            <Button
                variant="contained"
                sx={{ 
                    backgroundColor: 'grey', 
                    '&:hover': { backgroundColor: 'darkgrey' },
                    textTransform: 'none'
                }}
                onClick={handleNewVectorstore}
            >
                + New Vectorstore
            </Button>
        </div>
    )
};