import { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import Button from '@mui/material/Button';

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
                <Button
                    variant="contained"
                    sx={{ 
                        backgroundColor: 'grey', 
                        '&:hover': { backgroundColor: 'darkgrey' },
                        textTransform: 'none'
                    }}
                    onClick={handleLogin}
                >
                    Login
                </Button>
            </header>
        </div>
    );
}