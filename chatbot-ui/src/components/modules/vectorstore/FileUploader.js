import { useSelector, useDispatch } from 'react-redux';
import { Button, List, ListItem } from '@mui/material';

import { setFiles } from '../../../redux/actions/vectorStoreAction';

export const FileUploader = () => {
    const dispatch = useDispatch();
    const { files } = useSelector((state) => state.vectorStore);

    // 複数のファイルが選択されたときの処理
    const handleFileChange = (e) => {
        const files = Array.from(e.target.files);
        dispatch(setFiles(files));
    };

    // ファイル選択ダイアログを開くための関数
    const openFileDialog = () => {
        document.getElementById('file-input').click();
    };

    return (
        <div>
            {/* カスタムボタンでファイル選択を誘導 */}
            <input
                type="file"
                id="file-input"
                style={{ display: 'none' }}  // 非表示にする
                multiple
                onChange={handleFileChange}
            />
            <Button variant="contained" onClick={openFileDialog}>
                Select Files
            </Button>

            {/* 選択されたファイルリストを表示 */}
            {files.length > 0 && (
                <List>
                    {files.map((file, index) => (
                        <ListItem key={index}>{file.name}</ListItem>
                    ))}
                </List>
            )}
        </div>
    );
};