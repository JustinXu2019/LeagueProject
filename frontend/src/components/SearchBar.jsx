import { useState } from 'react'
import './SearchBar.css'
import { useNavigate } from 'react-router-dom'

function SearchBar() {

  const navigate = useNavigate();
  const [region, setRegion] = useState("NA1");
  const [searchInput, setSearchInput] = useState("");
  const regionNames = {
    NA1: "North America",
    EUW1: "Europe West",
    KR: "Korea"
  };

  const dispRegion = regionNames[region];

  const [isOpen, setIsOpen] = useState(false);

  const toggleDropdown = (e) => {
    e.preventDefault();
    setIsOpen(!isOpen);
  };

  const handleRegionChange = (e, selectedRegion) => {
    e.preventDefault()
    setRegion(selectedRegion)
    setIsOpen(false)
    // console.log(selectedRegion)
  };

  const handleSearchSubmission = async (e, searchInput) => {
    e.preventDefault()
    const [username, tagline] = searchInput.split("#");
    navigate(`/results/${region}/${username}/${tagline}`);
  }

  return (
    <form className="search-form" onSubmit={(e) => handleSearchSubmission(e, searchInput)}>
      <div className="label-group">
        <label>Region</label>
        <div className="dropdown">
          <button 
            type="button" className="dropdown-table" onClick={toggleDropdown}
          >
            {dispRegion}
            <span className={`arrow ${isOpen ? "open" : ""}`}>▼</span>
          </button>
          {isOpen && (
            <div className="dropdown-content">
              <a href="#" onClick={(e) => handleRegionChange(e, "NA1")}>North America</a>
              <a href="#" onClick={(e) => handleRegionChange(e, "EUW1")}>Europe West</a>
              <a href="#" onClick={(e) => handleRegionChange(e, "KR")}>Korea</a>
            </div>)}
          </div>
      </div>

      <div className="label-group">
      <label>Search</label>
      <input 
        className="search-input"
        type="search"
        value={searchInput}
        onChange={(e) => {
          setSearchInput(e.target.value);
          // console.log(e.target.value);
          }
        }
        placeholder="Username + Tagline (e.g., #NA1)"
      />
      </div>
    </form>
  );
}

export { SearchBar }