import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import {Link} from  "react-router-dom";


export default function Header(){
    return(
        <Navbar collapseOnSelect expand="lg" bg="bright" variant="dark">
      <Container>
        <Navbar.Brand href="/">
          <img className='logobar' alt='logo' src='img/logo-removebg.png' />
        </Navbar.Brand>
         <Nav>
            <Nav.Link  as ={Link} to ="/" style={{
              color:'black',
              fontWeight:'bold'
            }}>안녕하세요, user1님</Nav.Link>
            <Nav.Link style={{
              color:'black',
              fontWeight:'bold'
            }} href="/mypage">마이페이지</Nav.Link>
          </Nav>
        
      </Container>
    </Navbar>
    );
}