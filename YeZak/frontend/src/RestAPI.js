import React, { useState } from "react";
import axios from "axios";

function RestAPI() {
  const [text, setText] = useState([]);

  return (
    <>
      <h1>REST API 연습</h1>
      <div className="btn-primary">
        <button
          onClick={() => {
            axios

              .post("http://127.0.0.1:8000/post/upload/", {
                item_name: "작품명",
                price : "가격",
                item_size_width : "가로",
                item_size_height : "세로",
                details: "상세설명",
              })
              .then(function (response) {
                console.log(response);
              })
              .catch(function (error) {
                console.log(error);
              });
          }}
        >
          POST
        </button>
        <button
          onClick={() => {
            axios
              .get("http://127.0.0.1:8000/post/item/")
              .then((response) => {
                setText([...response.data]);
                console.log(response.data);
              })
              .catch(function (error) {
                console.log(error);
              });
          }}
        >
          GET
        </button>
      </div>
      {text.map((e) => (
        <div>
          {" "}
          <div className="list">
            <span>
              {e.item_id}번, <a href={`http://localhost:3000/postdetail/${e.item_id}`}>{e.item_name}</a>, {e.details}, {e.price}
            </span>
            <button
              className="btn-delete"
              onClick={() => {
                axios.delete(`http://127.0.0.1:8000/post/item/${e.item_id}`);
                setText(text.filter((text) => text.item_id !== e.item_id));
              }}
            >
              DELETE
            </button>{" "}
          </div>
        </div>
      ))}
    </>
  );
}

export default RestAPI;