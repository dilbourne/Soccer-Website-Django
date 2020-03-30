import React from 'react'
import Standings from './Standings.js';
import Jumbotron from '../layout/Jumbotron.js';

export default function Home(props) {
    return (
        <div>
            <Jumbotron 
            jumbo={{ 
                title: "Welcome to Premier League Addict!",
                lead: "Browse league standings, news and experience interactive stats on our favorite players."
            }} />
            <Standings standings={props.standings} />
        </div>
    )
}
