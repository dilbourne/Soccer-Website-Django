import React, { Component } from 'react'
import Plot from 'react-plotly.js';
import axios from 'axios';
import HelpPopover from '../layout/HelpPopover.js';

export default class ScatterPolar extends Component {
    constructor(props){
        super(props);
        this.state = {
            names : [],
            pInfo : {},
            data : [{
                type: "scatterpolar",
                name: "Source of Goals",
                r: [],
                theta: [],
                fill: "toself"       
            }],
            layout : {
                polar : {
                    radialaxis: {
                        visible: true,
                        range: [0,1]
                    }
                },
                showlegend: true,
                title: "Source Of Goals",
                font : {
                    color: 'white',
                },
                paper_bgcolor: 'rgb(1, 86, 107)',
            }
        }
        this.getPolarData = this.getPolarData.bind(this);
    }

    componentDidMount() {
        let full_names = []
        // fill this.state.names with all player names
        axios.get("stats/players/info/")
        .then( response => {
            response.data.map((p) => full_names = [...full_names,p.name]);
            this.setState({ names: full_names });
        })
    }

    getPolarData = (e) => {
        axios.get(`stats/players/info/${e.target.value}/`)
        .then(res => {
            this.setState({ pInfo: res.data });
            var layout = {
                polar : {
                    radialaxis: {
                        visible: true,
                        range: [0,1]
                    }
                },
                showlegend: true,
                title: this.state.pInfo.name + " - Source Of Goals",
                paper_bgcolor: 'rgb(1, 86, 107)',
                font : {
                    color: 'white'
                }
            }
            if (res.status == 200)
            {
                let [role, id] = [res.data.role,res.data.pl_id]
                axios.get(`stats/players/${role}/${id}`)
                .then(resp => {
                    let c = resp.data;
                    let g = resp.data.goals;
                    let data_ = [{
                        type: "scatterpolar",
                        name: res.data.name,
                        r: [c.goals_with_left_foot/g,
                            c.goals_with_right_foot/g,
                            c.headed_goals/g,
                            c.penalties_scored/g,
                            c.freekicks_scored/g],
                        theta: ["Goals with left foot","Goals with right foot","Header Goals","Penalty Goals","Freekick Goals"],
                        fill: "toself",
                        showlegend: true  
                    }];
                    this.setState({ data: data_, layout: layout });
                    })
            } 
        })
        .catch(error => {
            console.log(error);
        });
    }
    handlePopover = (e) => {
        e.preventDefault();
    }
    popBtnStyle = {
        backgroundColor: 'orange',
        color: 'white',
    }

    render() {
        return (
            <div id="scatterpolar-plot">
                <Plot 
                    data = {this.state.data}
                    layout = {this.state.layout} 
                />
                <div id="sp-input" className="d-flex flex-row justify-content-center p-2">
                    <form className="form-inline">
                        <div className="form-group">
                            <label className="control-label" htmlFor="input-sp-goals">Player Name: </label>
                            <input type="text" list="players" autoComplete="on" onChange={this.getPolarData} placeholder="" className="form-control p-2" id="input-sp-goals" />
                            <datalist id="players">
                                {this.state.names.map((name,index)=>(
                                    <option key={index} value={name}>{name}</option>
                                ))}
                            </datalist>
                            <HelpPopover
                                hp={{
                                    'popBtnStyle' : {
                                        'backgroundColor': 'orange',
                                        'color': 'white',         
                                    },
                                    'buttonText': 'Help',
                                    'title': 'Scatterpolar Plot',
                                    'body': 'Type the name of the player here (preferrably forward or midfielder), e.g - Jamie Vardy'
                                }}
                            />
                        </div>
                    </form>
                </div>    
            </div>
        )
    }
}
