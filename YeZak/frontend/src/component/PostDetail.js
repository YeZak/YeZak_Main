import { useParams } from "react-router-dom";
import React ,{ useEffect , useState } from "react";
import "./PostDetail.css"
import axios from "axios";

export default PostDetail;


function PostDetail(){
   
    const { item_id } =useParams(); //작품 id

    //var a = parseInt(item_id);
    
    // const item = item.find((item) => {
    //   return item.item_id == item_id;
    // });
    
    const [text, setText] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(null);

    const getItemDetails = async () => {
      setError(null);
      setText(null);
      setLoading(null);
      const response = await axios.get(
          `http://127.0.0.1:8000/post/item/${item_id}`
      );
      if(!response || response.error) {
          setError(response.error);
      } else {
          if(response.data) {

          setText(response.data);

          }

      }
      setLoading(false);

  };

  useEffect(() => {
      getItemDetails();
  }, [item_id]);


    if (loading) return <>loading...</>;
    if (error) return <>occur error</>;
    if (!text) return null;


    console.log(text);

    return(
      <>
          <div id="Bborder" key={text.item_id}>
             <section>
                  <div className="P_img">
                  <img src={`http://localhost:8000${text.item_pic}`} width="555px" height="555px" alt="art" />
                  </div>
                  <span className="sp_">
                      <span className='sp_1'>작품명:{text.item_name}</span>
                      <span className='sp_2'>작가명:{text.seller}</span>
                      <span className='sp_2_5'>사이즈:{text.item_size_height} x {text.item_size_width}</span>
                      <span className='sp_4'>판매중</span>
                      <span className='sp_3'> {text.price}원 </span>
                      <span className="comunity_button">
                          <a href="#"><button type="button" className='buy__now' onClick={"location.href= "}>작가 정보 보기</button></a>
                          <button type="button" className='like_button' onclick="">♡</button>
                      </span>
                  </span>
              </section>
              <br /><br/><br /><br /><br/>
              <section>
                  <div className ="product">
                      <div className="product_name"><p>[작품 상세설명]</p></div>
                      <br /><br/><br /><br /><br/><br /> <br /><br/><br /><br /><br/><br />
                      <div className="product_detail">{text.details}</div>
                      <br /><br/><br /><br /><br/><br />
                      <div className="interior_img">
                      <img src={`http://localhost:8000${text.pic_interior}`} width="555px" height="555px" alt="interior" />
                      </div>
                      <br /><br/><br /><br /><br/><br /><br /><br/><br />
                  </div>
              </section>
         </div>

        
      </>

    );
}