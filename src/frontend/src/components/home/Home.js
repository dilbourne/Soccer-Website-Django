import React from 'react'
import Standings from './Standings.js';
import Jumbotron from '../layout/Jumbotron.js';
import Carousel from './Carousel.js';
import NewsItem from '../news/NewsItem.js';

export default function Home(props) {
    return (
        <div>
            <Jumbotron 
            jumbo={{ 
                title: "Welcome to Premier League Addict",
                lead: "Browse league standings, news and experience interactive stats on our favorite players."
            }} />
            {/*<Carousel 
                images={{
                    image1: '/static/resources/news_carousel_test.png/',
                    image2: '/static/resources/polar_carousel.png/',
                    image3: '/static/resources/standings_carousel.png/'
                    }} 
                captions={{
                    cap1: 'Browse the Latest News',
                    cap2: 'Gain Insights from Interactive Plots',
                    cap3: 'Check the League Standings'
                }} />*/}
            <div className="container">
                <div className="row">
                    <div className="col">
                        <ul className="list-unstyled">
                            {props.article ? <NewsItem article = {props.article} toggle = {false} /> : null }
                        </ul>
                    </div>
                </div>
                <div className="row">
                    <div className="col">
                        <Standings standings={props.standings} />
                    </div>
                </div>
            </div>
            
        </div>
    )
}
