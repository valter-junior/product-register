import React from 'react';
import logo from './logo.svg';
import './App.css';
import LoginUser from './component/login/login'
import Home from './component/home/home'
import Register from './component/register/register'
import { BrowserRouter, Route, Routes} from 'react-router-dom';
import { Container } from 'react-bootstrap';
import  Movement from './component/product/movement'

function App() {
  
  return(
    <div>
      <Container>
        <BrowserRouter>
          <Routes>
            <Route path="/signin" element={<LoginUser/>}/>
            <Route path="/" element={<Home/>}/>              
            <Route path="/signup" element={<Register/>} />
            <Route path="/movement" element={<Movement/>} />
          </Routes>
        </BrowserRouter>
      </Container>  
    </div>
  )

}

export default App;
