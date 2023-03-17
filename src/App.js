import "./App.css";
import Filters from "./components/Filters.styled";
import Navbar from "./components/Navbar.styled";

function App() {
  return (
    <div className="App">
      <Navbar />
      <div className="products-filters">
        <div className="filters-div">
          <p>Filter Products:</p>
          <Filters />
        </div>
        <div className="products-div">
          <p>Our Products:</p>
          {/* products will be visible here */}
        </div>
      </div>
    </div>
  );
}

export default App;
