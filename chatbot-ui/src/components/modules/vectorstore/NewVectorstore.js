import { useSelector, useDispatch } from 'react-redux';
import Button from '@mui/material/Button';

import { setOpen } from '../../../redux/actions/vectorStoreAction';

export const NewVectorstore = () => {

    const dispatch = useDispatch();
    const { dialogOpen } = useSelector((state) => state.dialog);

    const handleNewVectorstore = () => {
        dispatch(setOpen(true));
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