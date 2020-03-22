import React, { Component } from 'react';
import NewsItem from './NewsItem';

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
            <NewsItem key={article.id} article={article} toggle={(this.state.toggle.length) ? this.state.toggle[index]  : true} />
        ))
        return(
            <React.Fragment>
                <div className="jumbotron jumbotron-fluid text-center">
                    <div className="container">
                        <h1 className="display-4">Premier League News</h1>
                        <hr className="my-4"></hr>
                        <p className="lead">Get the latest news updates right here, every single day.</p>
                    </div>
                </div>   
                <ul className="list-unstyled">
                    {news_items}
                </ul>
            </React.Fragment>
        )
    }
}

export default News;