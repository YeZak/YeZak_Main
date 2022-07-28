import { useState , useEffect} from "react";
import Pagination from "./Pagination";
import axios from 'axios';
import styled from "styled-components";
import {Link} from "react-router-dom";
import { Container, Row, Col } from "react-bootstrap";

import "./MainPost.css";


function MainPost(){
    const [posts , setPosts] = useState([]);
    const [limit , setLimit] = useState(9); //한 페이지에 작품 9개만
    const [page , setPage] = useState(1); // 페이지 수
    const offset = (page-1)*limit;//각 페이지의 첫번째로 올 작품 인덱스

    //장고에서 가져올 작품 데이터
    useEffect(()=> {
      const fetchData = async() =>{
        const response = await axios .get(
          "http://127.0.0.1:8000/post/item/"
        );
        setPosts(response.data);
      };
      fetchData();
    },[]);

    return(
        <Container>
        <Row>
        {posts.slice(offset , offset+limit).map(({item_id ,item_pic, item_name , seller ,price, details ,item_size_height ,item_size_width , prediction,tag_list})=>(
          <Col>
          <div className="card-all">
              <div className="card-top"  style={{}}>
                <figure className="card-img-figure" data-category = {prediction}>
                <img src= {`${item_pic}`} className="card-img-top" alt="art" style={{
                  width:"360px",
                  height :"300px"
                }}/>
                </figure>
                <br/>
                <div className="card-bottom">
                <ul className="card-body" style={{ margin: "5px", backgroundColor: "white", height: "330px" }}>
                  <li className="card-title" key={"item_name"} >{item_name}</li><br/>
                  <li className="card-artist" key={"artist"} >작가: {seller}</li><br />
                  <li className="card--item-price" key={"price"} >가격: {price}</li><br />
                  <li className="card-item-size" key={"item_size"} >사이즈 : {item_size_width}*{item_size_height}</li><br />
                  <li className="card--item-tag_list" key={"tag_list"} >{tag_list}</li><br />
                  <Link to ={`/postdetail/${item_id}`} className="card-link" key={"details"}>작품 상세보기 <br/></Link>
                </ul>
                </div>
             </div>
          </div>
            </Col>
          ))}
          </Row>
         <div>
            <Pagination
              total={posts.length}
              limit={limit}
              setLimit={setLimit}
              page={page}
              setPage={setPage}
            />
          </div>
        </Container>
    );
}


export default MainPost;