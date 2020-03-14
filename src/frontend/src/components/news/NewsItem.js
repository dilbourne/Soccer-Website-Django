import React, { Component } from 'react'
import PropTypes from 'prop-types';
import News from './News';

class NewsItem extends Component {
    render() {
        const { id, title, image, url, pub_date, summary } = this.props.article;
        return (
            <div className="card">
                <li className="media list-group-item">
                    <a href={url} alt={title}>
                        <img src={image} className="mr-3" alt="..." />
                    </a>
                    <div className="media-body align-self-center mr-3">
                        <h5 className="mt-0 mb-1">
                            {title}
                        </h5>
                        {summary}
                        <p>Date Published: {pub_date}</p>
                    </div>
                </li>
            </div>
        );
    }
}

export default NewsItem;

NewsItem.propTypes = {
    article: PropTypes.object.isRequired,
}