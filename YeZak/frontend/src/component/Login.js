//로그인

import styled from "styled-components";

const Container = styled.div`
  margin-top: 50px;
  padding: 100px;
`;

const Input = styled.input`
  position: relative;
  overflow: hidden;
  width: 800px;
  height: 40px;
  margin: 0 310px 8px;
  padding: 5px 39px 6px 11px;
  border: solid 1px #dadada;
  background: #fff;
  box-sizing: border-box;
`;

const Button = styled.div`
  font-size: 18px;
  font-weight: 700;
  line-height: 49px;
  display: block;
  width: 800px;
  height: 49px;
  margin: 16px 310px 7px;
  cursor: pointer;
  text-align: center;
  color: #fff;
  border: none;
  border-radius: 0;
  background-color: #231A87;
  ${({ disabled }) =>
    disabled &&
    `
    background-color: #efefef;
  `}
`;


export default function Login(){
    return(
    <Container>
      <p style={{
        position :"relative",
        left:"230px",
        top:"50px",
        fontWeight:'bold'
      }}>아이디</p>
      <Input id="id" name="id" placeholder="아이디를 입력해주세요." />
      <p style={{
        position :"relative",
        left:"230px",
        top:"50px",
        fontWeight:'bold'
      }}
      >비밀번호</p>
      <Input
        id="password"
        name="password"
        type="password"
        placeholder="비밀번호를 입력해주세요."
      />
      <Button>로그인</Button>
    </Container>
    );
}