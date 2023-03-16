import React from "react";
import styled from "styled-components";

const Searchbar = () => {
  return (
    <StyledSearch>
      <input type="text" placeholder="Search for products" />
    </StyledSearch>
  );
};

const StyledSearch = styled.div`
  width: 30%;
  input {
    padding-left: 20px;
    width: 100%;
    height: 42px;
    background: #f9f9f9;
    border: 1px solid #d1d1d1;
    border-radius: 12px;
  }
`;

export default Searchbar;
