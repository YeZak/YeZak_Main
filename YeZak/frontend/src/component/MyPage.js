import { Link } from "react-router-dom";
import "./MyPage.css";


function MyPage(){
    return(
        
        <div>
          <div className="my-page-my-page">
            <div className="my-page-group">
            <div className="my-page-component1">
              </div>
              <div className="my-page-group2">
                <span className="my-page-text02">Username: user1</span>
                <span className="my-page-text03">Email: user1@email.net</span>
                <span className="my-page-text04">Phone: 010-5432-0987</span>
              </div>
              <button className="my-page-button1">
                <span className="my-page-text05"><a href="/MyArtwork">My Artworks</a></span>
              </button>
              <Link to ="/upload">
              <button className="my-page-button2">
                <span className="my-page-text06">Upload artwork</span>
              </button>
              </Link>
                <img
                  alt="profile"
                  src="img/profile.jpg"
                  class="my-page-svg3" />
              <button className="my-page-button5">
                <span className="my-page-text09">Edit Profile</span>
              </button>
            </div>
          </div>
        </div>
     
    );
}
export default MyPage