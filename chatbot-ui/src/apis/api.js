import axios from 'axios';

const API_URL = 'http://localhost:5001';

export const GET = async (endpoint) => {
    try {
        const response = await axios.get(API_URL + endpoint);
        return response.data;
    } catch (error) {
        console.error('GET error : ', error);
        return { message: "エラーが発生しました" };
    }
}

export const POST = async (endpoint, data, { handleResponseMessage, handleResponseMessageStream }) => {
    if (data.stream_response === true) {
        try {
            const response = await axios.post(API_URL + endpoint, data);
            const reader = response.body.getReader();
            const decoder = new TextDecoder('utf-8');
    
            let accumulatedText = '';
            let chunk;
            let firstResponse = false;
    
            while (!(chunk = await reader.read()).done) {
                const text = decoder.decode(chunk.value, { stream: true });
                accumulatedText += text;
                if (!firstResponse) {
                    handleResponseMessage(accumulatedText);
                    firstResponse = true;
                } else {
                    handleResponseMessageStream(accumulatedText);
                }
            }
        } catch (error) {
            console.error("POST error for stream", error);
            handleResponseMessage("エラーが発生しました。");
        };
    } else {
        try {
            const response = await axios.post(API_URL + endpoint, data);
            return response.data;
        } catch (error) {
            console.error('POST error : ', error);
            return { message: "エラーが発生しました" };
        }
    }

};