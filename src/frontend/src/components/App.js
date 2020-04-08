import React, { Component } from "react";
import ReactDOM from 'react-dom';
import { render } from "react-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Header from './layout/Header';
import News from './news/News';
import axios from 'axios';
import Stats from "./stats/Stats";
import Home from "./home/Home";
import Footer from './layout/Footer';
import '../../../dashboard/static/css/main.css';

class App extends Component {
    state = {
        articles : [],
        standings: [],
        isLoading: true,
    }

    componentDidMount() {
        Promise.all(["news/api/daily/","stats/standings/"].map(url=>axios.get(url)))
        .then(responses => this.setState({ articles: responses[0].data, standings: responses[1].data, isLoading: false }))
        //.then(responses => this.setState({articles: responses[0] , standings: responses[1], isLoading: false}))
    }

    render() {
        const len_articles = !this.state.isLoading ? this.state.articles.length : 0;
        const randomIntegerInRange = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;
        const article_idx = !this.state.isLoading ? randomIntegerInRange(0,len_articles) : null;
        return (
            <Router>
                <React.Fragment>
                    <Header />
                    {/* Home here */}
                    <div className="main-content">
                        <Route 
                            path='/' exact
                            render={(props) => <Home {...props} article = { !this.state.isLoading ? this.state.articles[article_idx] : null } standings = {this.state.standings} />}
                        />
                        <Route 
                            path='/news' exact 
                            render={(props) => <News {...props} articles = {!this.state.isLoading ? this.state.articles: null} />}
                        />
                        <Route
                            path='/stats' exact
                            component = {Stats}
                        />
                        </div>
                    <Footer />
                </React.Fragment>
            </Router>
            
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));