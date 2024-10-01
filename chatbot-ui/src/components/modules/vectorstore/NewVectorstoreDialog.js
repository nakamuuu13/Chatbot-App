import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Dialog, DialogTitle, DialogContent, DialogActions, Button } from '@mui/material';
import { setOpen } from '../../../redux/actions/vectorStoreAction';
import { FileUploader } from './FileUploader';

export const NewVectorstoreDialog = () => {
    const dispatch = useDispatch();
    const { dialogOpen } = useSelector((state) => state.dialog);
    const [files, setFiles] = useState([]);

    // ファイル選択時に呼ばれるコールバック
    const handleFilesSelected = (selectedFiles) => {
        setFiles(selectedFiles);
    };

    // ダイアログを閉じる
    const handleClose = () => {
        dispatch(setOpen(false));
    };

    return (
        <div>
            <Dialog 
                open={dialogOpen} 
                onClose={handleClose} 
                maxWidth="sm" 
                fullWidth
            >
                <DialogTitle>New Vectorstore Builder</DialogTitle>
                <DialogContent dividers style={{ maxHeight: '400px', overflowY: 'auto' }}>
                    <p>Build your new vectorstore with the files you select here.</p>
                    <FileUploader onFilesSelected={handleFilesSelected} />
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleClose} color="primary">
                        Cancel
                    </Button>
                    <Button onClick={handleClose} color="primary">
                        Build
                    </Button>
                </DialogActions>
            </Dialog>
        </div>
    );
}