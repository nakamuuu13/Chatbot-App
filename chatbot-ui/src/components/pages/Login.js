import { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';

import { setLoginState } from '../../redux/actions/loginAction';

import './../../App.css';
import logo from './ai_logo.png';

export const Login = () => {

    const dispatch = useDispatch();
    const loginState = useSelector(state => state.login.loginState);

    const handleLogin = async () => {
        dispatch(setLoginState(true));
    };

    useEffect(() => {
        if (loginState) {
            window.location.href = '/chat';
        }
    }, [loginState]);


    return (
        <div className="Login">
            <header className="Login-header">
                <img src={logo} className="Login-logo" alt="logo" />
                <h1>Chatbot Application</h1>
                <button className="Login-button" onClick={handleLogin}>Login</button>
            </header>
        </div>
    );
}