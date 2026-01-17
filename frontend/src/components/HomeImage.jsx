import catImage from '../assets/sadcat_thumbsup.png'
import './HomeImage.css'

function HomeImage() {
  return (
    <div>
      <img className="home-image" src={catImage} />
    </div>
  );
}

export { HomeImage }