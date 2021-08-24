import React, { Component } from 'react'
import PropTypes from 'prop-types';
import News from './News';
import './css/news_item.css';

class NewsItem extends Component {
    constructor(props){
        super(props);
    }
    render() {
        const { title, image, url, pub_date, summary } = this.props.article;
        return (
                <div className="card">
                    <li className={(this.props.toggle) ? "media list-group-item-reverse" : "media list-group-item"}>
                        <a href={url} target="_blank" alt={title}>
                            <img src={image} className="img-fluid mr-3" alt="..." />
                        </a>
                        <div className="media-body align-self-center mr-3">
                            <h5 className="mt-0 mb-1">
                                {title}
                            </h5>
                            {summary}
                            <p className="date">Date Published: {pub_date}</p>
                        </div>
                    </li>
                </div>
        );
        }
}

export default NewsItem;

NewsItem.propTypes = {
    article: PropTypes.object.isRequired,
    toggle: PropTypes.bool.isRequired
}