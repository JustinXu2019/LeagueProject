import './MatchInfo.css'

function MatchInfo({ data }) {

    const matchId = data.match.match_id
    const champion = data.champion
    const kills = data.kills
    const deaths = data.deaths
    const assists = data.assists
    const winloss = data.winloss

    return (
        <div className="match-box">
            <div className="champ-name">
                <label>{champion}</label>
            </div>
            <div className="match-stats">
                <label>{kills}/{deaths}/{assists}</label>
            </div>
        </div>
    )
}

export { MatchInfo }