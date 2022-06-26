import { useState } from 'react';
import { Registration } from '../../lib/login';
import { useNavigate } from 'react-router-dom'
import swal from 'sweetalert';

const Register = (props) => {
    const [name, setFirstname] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPass] = useState("");

    const history = useNavigate();

    const onSubmitForm = async (event) => {
        event.preventDefault();
    
        try {
            const body = {name, email, password};
            console.log(body)
            const response = await Registration(body);
            console.log(response);
            swal("Registered with success", {
                buttons: [false],
                timer: 2000,
              })
            history('/signin')
        } catch (err) {
            console.log(err);
        }
    }
    
    return (
        <div className='login-box'>
            <h2>Login</h2>
                <form onSubmit={onSubmitForm}>
                <div className='user-box'>
                        <input type="text" value={name} onChange={e=> setFirstname(e.target.value)}/ >
                        <label>Nome</label>
                    </div>
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
    export default Register;