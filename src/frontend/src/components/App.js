import React, { Component } from "react";
import ReactDOM from 'react-dom';
import { render } from "react-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Header from './layout/Header';
import News from './news/News';
import axios from 'axios';
import ScatterPolar from "./stats/ScatterPolar";

class App extends Component {
    state = {
        articles : [],
    }

    componentDidMount() {
        axios.get("http://localhost:8000/news/api/daily/")
        .then(res => this.setState({
            articles: res.data
        }))
    }
    render() {
        return (
            <Router>
                <React.Fragment>
                    <Header />
                    <Route 
                        path='/news' exact 
                        render={(props) => <News {...props} articles = {this.state.articles} />}
                     />
                     <Route
                        path='/stats' exact
                        component = {ScatterPolar}
                    />
                </React.Fragment>
            </Router>
            
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));