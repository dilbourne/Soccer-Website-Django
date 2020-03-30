import React from 'react';

export default function Jumbotron(props) {
    return (
            <div className="jumbotron jumbotron-fluid text-center">
                <div className="container">
                    <h1 className="display-4">{props.jumbo.title}</h1>
                    <hr className="my-4"></hr>
                    <p className="lead">{props.jumbo.lead}</p>
                </div>
            </div>   
    )
}
