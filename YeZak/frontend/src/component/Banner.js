//메인페이지 상단에 예작 소개하는 배너
import { Carousel } from "react-bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";


export default function Banner(){
    
    return(
        <Carousel fade>
        <Carousel.Item>
        <Carousel.Caption>
        </Carousel.Caption>

          <img
            style={{ height: "600px" , width: "800px" }}
            className="d-block w-100"
            src="img/gallery-3.jpg"
            alt="First slide"
          />
          <Carousel.Caption>
          <h1 
          style={{
            fontWeight:"bold"
          }}>미대생의 작품을 더 쉽게 만나다.</h1>
        </Carousel.Caption>
        </Carousel.Item>
        <Carousel.Item>
          <img
            style={{ height: "600px" , width: "800px" }}
            className="d-block w-100"
            src="img/gallery-2.jpg"
            alt="Second slide"
          />
          <Carousel.Caption>
          <h1 style={{
            fontWeight:"bold"
          }}
          >Visualize Your Artwork.</h1>
        </Carousel.Caption>
        </Carousel.Item>
      </Carousel>
       
    );
 
}