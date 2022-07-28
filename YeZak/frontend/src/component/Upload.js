import React, { Component } from "react";
import axios from 'axios';
import "./Upload.css";
import { Link } from "react-router-dom";



class Upload extends Component{

   state ={
     item_id:"",
     item_name: "",
     price: "",
     item_size_width: "",
     item_size_height: "",
     details: "",
     date: "",
     item_pic: null
   };
 
  

  handleChange =(e) =>{
    this.setState({
      [e.target.id] :e.target.value
    })
  };

  handleImageChange = (e) =>{
    console.log(e.target.files[0]);
        this.setState({
          item_pic:e.target.files[0]
        }, () => {
    console.log(this.state.item_pic);
    })
      };

  handleSummit =(e) =>{
    e.preventDefault();
    
    console.log(this.state);
    let form_data = new FormData();
    form_data.append("item_pic", this.state.item_pic);
    form_data.append("item_name", this.state.item_name);
    form_data.append('price', this.state.price);
    form_data.append('item_size_height', this.state.item_size_height);
    form_data.append('item_size_width', this.state.item_size_width);
    form_data.append('details', this.state.details);
    let url ='http://127.0.0.1:8000/post/item/';
    axios.post(url,form_data,{
      headers:{
        'content-type':'multipart/form_data'
      }
    })
         .then(res =>{
          console.log(res.data);
          
         })
         .catch(error =>console.log(error))

    };

    handleClick =(e) =>{
      window.location.href="/myartwork"
    };


  render(){
  return(
    <div className="upload-all">
      <form onSubmit={this.handleSummit}>

        <div className="input-box">
        <p>
          <input  className ="inputs" type="text" placeholder='item_name' id='item_name' value={this.state.item_name} onChange={this.handleChange} required/>
        </p>
        <p>
          <input  className ="inputs" type="text" placeholder='price' id='price' value={this.state.price} onChange={this.handleChange} required/>
        </p>
        <p>
          <input  className ="inputs" type="text" placeholder='item_size_height' id='item_size_height' value={this.state.item_size_height} onChange={this.handleChange} required/>
        </p>
        <p>
          <input  className ="inputs" type="text" placeholder='item_size_width' id='item_size_width' value={this.state.item_size_width} onChange={this.handleChange} required/>
        </p>
        <p>
          <input  className ="inputs" type="text" placeholder='details' id='details' value={this.state.details} onChange={this.handleChange} required/>
        </p>
        </div>
        <p>
            <input className="input-img" type="file"
                   id="item_pic" accept="image/png, image/jpeg, image/jpg"  onChange={this.handleImageChange} required />
        </p>
       
         <button className="upload-button" type="submit" value="Upload" onClick={this.handleClick}>Upload</button> 
        
         <Link to="/mypage">
          <button>
            <span className="upload-page-cancel">Cancel</span>
          </button>
        </Link> 
      
      </form>
    </div>
   
  );
  }
  };
export default Upload;