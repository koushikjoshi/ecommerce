import React, { useState } from "react";
import styled from "styled-components";

const Filters = () => {
  const [rating, setRating] = useState(0);
  const [price, setPrice] = useState(0);

  const handleStarClick = (value) => {
    setRating(value);
  };

  const handlePriceChange = (event) => {
    setPrice(event.target.value);
  };

  return (
    <FilterWrapper>
      <FilterSection>
        <FilterTitle>Price</FilterTitle>
        <PriceWrapper>
          <PriceLabel>0</PriceLabel>
          <FilterInput
            type="range"
            min="0"
            max="1000"
            value={price}
            onChange={handlePriceChange}
          />
          <PriceLabel>1000</PriceLabel>
        </PriceWrapper>
        <SelectedPrice>Selected Price: {price}</SelectedPrice>
      </FilterSection>
      <FilterSection>
        <FilterTitle>Rating</FilterTitle>
        <StarWrapper>
          {[1, 2, 3, 4, 5].map((value) => (
            <Star
              key={value}
              onClick={() => handleStarClick(value)}
              filled={rating >= value}
            >
              ★
            </Star>
          ))}
        </StarWrapper>
      </FilterSection>
    </FilterWrapper>
  );
};

const FilterWrapper = styled.div`
  display: flex;
  flex-direction: column;
  gap: 1rem;
`;

const FilterSection = styled.div`
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
`;

const FilterTitle = styled.h4`
  margin: 0;
  font-weight: 500;
`;

const PriceWrapper = styled.div`
  display: flex;
  justify-content: space-between;
`;

const PriceLabel = styled.span``;

const SelectedPrice = styled.p`
  margin: 0;
  font-size: 0.9rem;
`;

const FilterInput = styled.input`
  width: 100%;
`;

const StarWrapper = styled.div`
  display: flex;
  gap: 0.25rem;
`;

const Star = styled.span`
  cursor: pointer;
  color: ${(props) => (props.filled ? "#FFD700" : "#C0C0C0")};
`;

export default Filters;
