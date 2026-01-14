import { useState } from 'react'
import './App.css'
import catImage from './assets/sadcat_thumbsup.png'

// {
//     "summoner": {
//         "puuid": "4r5ofUPpNviVwru6xaRVhgxS35moBn6QjG3UqfRZRJAgbLRGpqctHdEkzOIb4BZ-6KWxH6f5sAdVGA",
//         "username": "Caseoh",
//         "tagline": "NA1"
//     },
//     "match": {
//         "match_id": "NA1_5462883102",
//         "queue_type": 420
//     },
//     "champion": "Skarner",
//     "kills": 7,
//     "deaths": 2,
//     "assists": 19,
//     "winloss": true
// }

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

  return (
    <form className="search-form">
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

function HomeImage() {
  return (
    <div>
      <img className="home-image" src={catImage} />
    </div>
  );
}

function App() {

  return (

    <div className="app-wrapper">
      <div className="image-wrapper">
        <HomeImage />
      </div>
      <div className="search-container">
        <SearchBar />
      </div>
    </div>

  );
}

export default App
