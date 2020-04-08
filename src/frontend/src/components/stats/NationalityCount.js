import React, { Component } from 'react';
import Plot from 'react-plotly.js';
import axios from 'axios';
import HelpPopover from '../layout/HelpPopover.js';

export default class NationalityCount extends Component {
    constructor(props){
        super(props);
        this.state = {
            data : [],
            layout : {
                title: 'Most Popular Premier League Nationalities',
                xaxis: {
                    tickangle: -45
                },
                showlegend: false,
                bargap: 0.05,
                paper_bgcolor: 'rgb(1, 86, 107)',
                font: {
                    color: 'white'
                },
                autosize:true
            }
        }
        this.getNationalityCount = this.getNationalityCount.bind(this);
    }

    getNationalityCount = (e) => {
        var countries = [];
        var count = [];
        axios.get(`stats/nationality_count/${e.target.value}/`)
        .then(res => {
            res.data.map((item)=>{
                countries=[...countries,item.country];
                count=[...count,item.country__count];
            });
            this.setState({ 
                data : [{
                    x: countries,
                    y: count,
                    type: 'bar',
                    name: "Number of Players",
                    marker: {
                        color: 'skyblue',
                    },
                    opacity: 0.75,
                    }]
             });
        })
    }

    render() {
        return (
            <React.Fragment>
                <Plot 
                    data = {this.state.data}
                    layout = {this.state.layout}
                    useResizeHandler
                />
                <div id="nat-input-wrapper" className="p-2">
                    <form className="form-inline">
                        <div className="form-group">
                            <label className="control-label" htmlFor="top_n">Top Nationalities: </label>
                            <div className="col-xs-2">
                                <input type="number" className="form-control" id="nat-input" min="1" onChange={this.getNationalityCount} /> 
                            </div>
                            <HelpPopover
                                hp={{
                                    'popBtnStyle' : {
                                        'backgroundColor': 'orange',
                                        'color': 'white',         
                                    },
                                    'buttonText': 'Help',
                                    'title': 'Nationality Bar Plot',
                                    'body': 'Enter the number to specify how much of the nationality count ranking should be displayed.'
                                }}
                            />
                        </div> 
                    </form>  
                </div>
            </React.Fragment>
        )
    }
}
