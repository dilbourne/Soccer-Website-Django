import React from 'react';
import ScatterPolar from './ScatterPolar.js';
import NationalityCount from './NationalityCount.js';
import Jumbotron from '../layout/Jumbotron.js';
import './css/stats.css';

export default function Stats() {
    return (
        <React.Fragment>
            <Jumbotron jumbo={{'title': 'Premier League Stats','lead': 'Try out our interactive plots to gain insights on your favorite players.'}} />
            <div id="sp-plot" className="d-flex flex-row justify-content-center card p-3">
                <ScatterPolar />
            </div>
            <div id="bar-plot" className="d-flex flex-row justify-content-center card p-3">
                <NationalityCount />
            </div>
        </React.Fragment>
        
    )
}
