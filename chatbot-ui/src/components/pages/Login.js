import { useEffect } from 'react';

import './../../App.css';
import logo from './ai_logo.png';

import { GET } from '../../apis/api';

export const Login = () => {

    let response = {};
    const getHelloWorld = async () => {
        response = await GET('/api/helloworld');
        console.log(response);
    }

    useEffect(() => {
        getHelloWorld();
    }, []);


    return (
        <div className="Login">
            <header className="Login-header">
                <img src={logo} className="Login-logo" alt="logo" />
                <h1>Chatbot Application</h1>
            </header>
        </div>
    );
}