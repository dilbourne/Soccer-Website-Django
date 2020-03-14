import React, { Component } from 'react';
import NewsItem from './NewsItem';

class News extends Component {
    render() {
        return (
            <ul className="list-unstyled">
                {this.props.articles.map((article)=>(
                    <NewsItem key={article.id} article={article} />
                ))}
            </ul>
        )
    }
}

export default News;