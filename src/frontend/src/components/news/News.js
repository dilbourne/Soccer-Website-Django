import React, { Component } from 'react';
import NewsItem from './NewsItem';
import Jumbotron from '../layout/Jumbotron';

class News extends Component {
    constructor(props){
        super(props);
        this.state = {
            toggle : [],
        }
    }

    componentDidMount() {
        const numArticles = this.props.articles.length;
        let temp = [];
        for (var i=0; i < numArticles; i++) {
            (i % 2 == 0) ? temp.push(true) : temp.push(false);
        }
        this.setState({ toggle: temp });
    }

    render() {
        const news_items = this.props.articles.map((article, index)=>(
            <NewsItem key={index} article={article} toggle={(this.state.toggle.length) ? this.state.toggle[index]  : true} />
        ))
        const jumbo = {
            title : 'Premier League News',
            lead : 'Get the latest updates right here every day, on PL Addict.' 
        }
        return(
            <React.Fragment>
                <Jumbotron jumbo={jumbo} />
                <ul className="list-unstyled">
                    {news_items}
                </ul>
            </React.Fragment>
        )
    }
}

export default News;