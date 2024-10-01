import React, { useState } from 'react';
import { Button, List, ListItem } from '@mui/material';

export const FileUploader = ({ onFilesSelected }) => {
    const [selectedFiles, setSelectedFiles] = useState([]);

    // 複数のファイルが選択されたときの処理
    const handleFileChange = (e) => {
        const files = Array.from(e.target.files);
        setSelectedFiles(files);
        onFilesSelected(files);  // 親コンポーネントにファイルを渡す
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
            {selectedFiles.length > 0 && (
                <List>
                    {selectedFiles.map((file, index) => (
                        <ListItem key={index}>{file.name}</ListItem>
                    ))}
                </List>
            )}
        </div>
    );
};