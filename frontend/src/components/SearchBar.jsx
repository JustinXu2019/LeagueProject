import { useState } from 'react'
import './SearchBar.css'

let userData;

function SearchBar() {

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
    const split = searchInput.split("#")
    const username = split[0]
    const tagline = split[1]
    if (!username || !tagline) return;
    try {
        const response = await fetch(`http://localhost:8000/api/search/?username=${username}&tagline=${tagline}&region=${region}`);
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        userData = await response.json()
        console.log("Data received from Django:", data);
    } catch (error) {
        console.error("Fetch error:", error);
    }
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

export { SearchBar, userData }