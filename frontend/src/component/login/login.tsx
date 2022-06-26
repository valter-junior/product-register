import { useState} from 'react';
import { useNavigate } from 'react-router-dom'
import { Login } from '../../lib/login';
import swal from 'sweetalert';
import "./login.css"

const LoginUser = (props) => {
    const [email, setEmail] = useState("");
    const [password, setPass] = useState("");
    
    const history = useNavigate();
        
    const onSubmitForm = async (event) => {
        event.preventDefault();

        const body = {email, password}
        const response = await Login(body)
    
        if (response === "Email or password invalid") {
            swal("Email or password invalid!")
        } else
        if ('token'in response) {
            swal("success", {
              buttons: [false],
              timer: 2000,
            })
            .then((value) => {
              localStorage.setItem('token', response['token']);
              localStorage.setItem('user', JSON.stringify(response['user']));
              history("/movement")
            })
        }
    }
    
    return (

        <div className='login-box'>
            <h2>Login</h2>
                <form onSubmit={onSubmitForm}>
                    <div className='user-box'>
                        <input type="email" value={email} onChange={e=> setEmail(e.target.value)}/ >
                        <label>Email</label>
                    </div>
                    <div className='user-box'>
                        <input type="password" value={password} onChange={e=> setPass(e.target.value)}/>
                        <label>Password</label>
                    </div>
                    <input type="button" value="submit" onClick={onSubmitForm}/>
                </form>
        </div>

    );
       
}

export default LoginUser;





