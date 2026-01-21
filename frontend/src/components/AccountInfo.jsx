import './AccountInfo.css'

function AccountInfo({ data }) {
    // console.log(data[0].summoner.username)

    const AccountName = data[0].summoner.username
    const AccountTag = data[0].summoner.tagline

    return (
        <label className="username-label">{AccountName}#{AccountTag}</label>
    );
}

export { AccountInfo }