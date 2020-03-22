import React, { Component } from 'react'
import Plot from 'react-plotly.js';
import axios from 'axios';

export default class ScatterPolar extends Component {
    constructor(props){
        super(props);
        this.state = {
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
                    },
                    showlegend: true,
                    title: "",
                    color: '#27293d',
                    font: {
                        color: '#000000',
                    }
                },
            }
        }
        this.getPolarData = this.getPolarData.bind(this);
    }

    getPolarData = (e) => {
        axios.get(`stats/players/info/${e.target.value}/`)
        .then(res => {
            console.log(res.data.name);
            this.setState({ pInfo: res.data }, () => {console.log(this.state)});
            let layout = {
                polar : {
                    radialaxis: {
                        visible: true,
                        range: [0,1]
                    },
                    showlegend: true,
                    title: this.state.pInfo.name,
                    color: '#27293d',
                    font: {
                        color: '#000000',
                    }
                },
            }
            if (res.status == 200)
            {
                let [role, id] = [res.data.role,res.data.pl_id]
                axios.get(`stats/players/${role}/${id}`)
                .then(resp => {
                    console.log(resp.data);
                    let c = resp.data;
                    let g = resp.data.goals;
                    let data_ = [{
                        type: "scatterpolar",
                        name: "source of goals",
                        r: [c.goals_with_left_foot/g,
                            c.goals_with_right_foot/g,
                            c.headed_goals/g,
                            c.penalties_scored/g,
                            c.freekicks_scored/g],
                        theta: ["Goals with left foot","Goals with right foot","Header Goals","Penalty Goals","Freekick Goals"],
                        fill: "toself"       
                    }];
                    this.setState({ data: data_, layout: layout },()=>{console.log(this.state)});
                    })
            } 
        })
        .catch(error => {
            console.log(error);
        });
    }

    render() {
        return (
            <React.Fragment>
                <Plot 
                    data = {this.state.data}
                    layout = {this.state.layout} 
                />
                <form>
                    <input type="text" onChange={this.getPolarData} placeholder="Type player name" id="input-sp-goals" />
                </form>
            </React.Fragment>
        )
    }
}
