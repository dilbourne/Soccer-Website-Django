import React, { Component } from "react";
import ReactDOM from 'react-dom';
import { render } from "react-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Header from './layout/Header';
import News from './news/News';
import axios from 'axios';
import Stats from "./stats/Stats";
import Home from "./home/Home";

class App extends Component {
    state = {
        articles : [],
        standings: [],
    }
    componentDidUpdate(){
        console.log(this.state.standings);
    }
    
    componentDidMount() {
        axios.get("http://localhost:8000/news/api/daily/")
        .then(res => this.setState({
            articles: res.data
        }))

        axios.get("http://localhost:8000/stats/standings/")
        .then(res => this.setState({
            standings: res.data
        },console.log(this.state.standings)))
    }
    render() {
        return (
            <Router>
                <React.Fragment>
                    <Header />
                    {/* Home here */}
                    <Route 
                        path='/' exact
                        render={(props) => <Home {...props} standings = {this.state.standings} />}
                    />
                    <Route 
                        path='/news' exact 
                        render={(props) => <News {...props} articles = {this.state.articles} />}
                     />
                     <Route
                        path='/stats' exact
                        component = {Stats}
                    />
                </React.Fragment>
            </Router>
            
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));