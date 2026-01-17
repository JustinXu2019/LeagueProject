import { HomeImage } from '../components/HomeImage'; 
import { SearchBar } from '../components/SearchBar';
import './Home.css'; 

function Home() {
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

export { Home };   