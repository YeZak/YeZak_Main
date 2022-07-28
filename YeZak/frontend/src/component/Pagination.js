//메인 페이지에서 한 페이지의 게시물이 10개가 넘어가면 다음 페이지로 넘어가게 해줌
import styled from "styled-components";

function Pagination({total , limit , page, setPage }){ //total은 총 게시물 수
    const numPages = Math.ceil(total/limit);

    return(
    <>
      <Nav>
        <Button onClick={() => setPage(page - 1)} disabled={page === 1}>
          &lt;
        </Button>
        {Array(numPages)
          .fill()
          .map((_, i) => (
            <Button
              key={i + 1}
              onClick={() => setPage(i + 1)}
              aria-current={page === i + 1 ? "page" : null}
            >
              {i + 1}
            </Button>
          ))}
        <Button onClick={() => setPage(page + 1)} disabled={page === numPages}>
          &gt;
        </Button>
      </Nav>
    </>
    );
}

const Nav = styled.nav`
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 4px;
  margin: 16px;
`;

const Button = styled.button`
  border: none;
  border-radius: 8px;
  padding: 8px;
  margin: 0;
  background: black;
  color: white;
  font-size: 1rem;




  &:hover {
    background: yellow;
    cursor: pointer;
    transform: translateY(-2px);
  }

  &[disabled] {
    background: grey;
    cursor: revert;
    transform: revert;
  }




  &[aria-current] {
    background: navy;
    font-weight: bold;
    cursor: revert;
    transform: revert;
  }
`;
export default Pagination;