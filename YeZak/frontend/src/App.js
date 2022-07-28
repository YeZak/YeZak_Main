import 'bootstrap/dist/css/bootstrap.min.css';
import Header from './component/Header.js'
import{BrowserRouter , Route , Routes} from "react-router-dom";
import Login from './component/Login.js';
import Register from './component/Register.js';
import Main from './component/Main.js';
import PostDetail from './component/PostDetail.js';
import React from 'react';
import Footer from './component/Footer.js';
import MyPage from './component/MyPage.js'
import Upload from './component/Upload.js';
import MyArtwork from './component/MyArtwork.js';



function App(){

    return(
      <><BrowserRouter>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path ="/postdetail/:item_id" element ={<PostDetail />} />
          <Route path ="/mypage" element={<MyPage />} />
          <Route path ="/upload" element={<Upload />} />
          <Route path ="/myartwork" element={<MyArtwork />} />
        </Routes>
        <Footer />
      </div>
    </BrowserRouter>
    
    </>
    );
}


export default App