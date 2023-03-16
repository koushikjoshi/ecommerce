import React from "react";
import styled from "styled-components";
import Searchbar from "./Searchbar.styled";
import { AiOutlineShoppingCart } from "react-icons/ai";

const Navbar = () => {
  return (
    <StyledNavbar>
      <div>ReactMart</div>
      <Searchbar />
      <div
        className="cart-div"
        style={{
          display: "flex",
          flexDirection: "row",
          height: "100%",
          alignItems: "center",
        }}
      >
        <AiOutlineShoppingCart />
        <p className="cart-items">(0)</p>
      </div>
    </StyledNavbar>
  );
};

const StyledNavbar = styled.header`
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  width: 100%;
  height: 80px;
  font-family: "Brush Script MT", cursive;
  font-style: normal;
  font-weight: 500;
  font-size: 40px;
  line-height: 22px;
`;

export default Navbar;
