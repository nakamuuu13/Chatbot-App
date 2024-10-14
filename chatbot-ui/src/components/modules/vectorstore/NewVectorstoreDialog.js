import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Dialog, DialogTitle, DialogContent, DialogActions, Button, TextField } from '@mui/material';
import { setOpen, setName, setCreate } from '../../../redux/actions/vectorStoreAction';
import { FileUploader } from './FileUploader';
import { POST } from '../../../apis/api';

export const NewVectorstoreDialog = () => {
    const dispatch = useDispatch();
    const { dialogOpen, files, name, create } = useSelector((state) => state.vectorStore);

    // ダイアログを閉じる
    const handleClose = () => {
        dispatch(setOpen(false));
    };

    // 名前の変更
    const handleNameChange = (e) => {
        dispatch(setName(e.target.value));
    };

    // ベクトルストア作成状態
    const handleCreateChange = (state) => {
        dispatch(setCreate(state));
    };

    // ベクトルストアを作成する
    const handleVectorstoreBuild = async () => {
        if (!name) {
            alert('名前を入力してください。');
            return;
        }
    
        if (!files || files.length === 0) {
            alert('ファイルを選択してください。');
            return;
        }

        handleCreateChange(true);

        const formData = new FormData();
        try {
            formData.append('name', name);
            formData.append('description', 'This is a vectorstore');
            for (let i = 0; i < files.length; i++) {
                formData.append('files', files[i]);
            }
            
            const response = await POST('/api/vectorstore/create_vectorstore', formData, {});
            console.log(response);
        } catch (error) {
            console.error('handleVectorstoreBuild error : ', error);
        } finally {
            handleClose();
            handleCreateChange(false);
        }
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
                    
                    {/* nameを入力するテキストフィールド */}
                    <TextField
                        label="Vectorstore Name"
                        value={name}
                        onChange={handleNameChange}
                        fullWidth
                        margin="normal"
                    />

                    {/* FileUploader コンポーネント */}
                    <FileUploader />
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleClose} color="primary">
                        Cancel
                    </Button>  
                    <Button 
                        onClick={handleVectorstoreBuild} 
                        color="primary"
                        disabled={create}
                    >
                        {create ? 'CREATING...' : 'CREATE'}
                    </Button>
                </DialogActions>
            </Dialog>
        </div>
    );
};