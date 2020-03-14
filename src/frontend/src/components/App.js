import React, { Component } from "react";
import ReactDOM from 'react-dom';
import { render } from "react-dom";
import { BrowserRouter as Router, Route } from "react-router-dom";
import Header from './layout/Header';
import News from './news/News';
import axios from 'axios';

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
            <React.Fragment>
                <Header />
                <News articles={this.state.articles} />
            </React.Fragment>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));