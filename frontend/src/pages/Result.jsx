import { useState, useEffect } from 'react'
import './Result.css'
import { useParams } from 'react-router-dom'
import { AccountInfo } from '../components/AccountInfo'
import { MatchInfo } from '../components/MatchInfo'

function Result() {

    const { region, username, tagline } = useParams();
    const [userData, setUserData] = useState(null)

    useEffect(() => {

        const fetchData = async () => {
            try {
                const response = await fetch(`http://localhost:8000/api/search/?username=${username}&tagline=${tagline}&region=${region}`);
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                const data = await response.json()
                setUserData(data)
                console.log("Data received from Django:", data);
            } catch (error) {
                console.error("Fetch error:", error);
            }
        };

        fetchData();

    }, [region, username, tagline]);

    if (!userData) return <div>Loading...</div>;

    return (
        <div className="entire-page">
            <div className="account-info">
                <AccountInfo data={userData}/>
            </div>
            <div className="match-info">
                {userData.map((item) =>
                    <MatchInfo key={item.match.match_id} data={item}/>
                )}
            </div>
        </div>
    )
}

export { Result };