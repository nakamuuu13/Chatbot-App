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

export const POST = async (endpoint, data) => {
    try {
        const response = await axios.post(API_URL + endpoint, data);
        return response.data;
    } catch (error) {
        console.error('POST error : ', error);
        return { message: "エラーが発生しました" };
    }
};