import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Header extends Component {
    render() {
        return (
            <header>
                <nav className="navbar navbar-expand-md navbar-blue bg-blue">
                    <a className="navbar-brand" href="#">Premier League Addict</a>
                    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#varbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle naviagtion">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarsExampleDefault">
                        <ul className="navbar-nav mr-auto">
                            <li className="nav-item">
                                <a className="nav-link disabled">Home</a>
                            </li>
                            <li className="nav-item-active">
                                <a href='/news/' className ="nav-link">News</a>
                                <span className="sr-only">(current)</span>
                            </li>
                            <li className="nav-item">
                                <a href='/stats/' className="nav-link">Stats</a>
                            </li>
                        </ul>
                    </div>
                </nav>
            </header>
        )
    }
}
export default Header;