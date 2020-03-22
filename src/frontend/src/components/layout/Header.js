import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import './css/header.css';

class Header extends Component {
    render() {
        return (
            <header>
                <nav className="navbar navbar-expand-md">
                    <a className="navbar-brand" href="#">Premier League Addict</a>
                    <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarsExampleDefault">
                        <ul className="navbar-nav">
                            <li className="nav-item">
                                <Link to='' className="nav-link disabled">Home</Link>
                            </li>
                            <li className="nav-item active">
                                <Link to='/news' className ="nav-link">News</Link>
                                <span className="sr-only">(current)</span>
                            </li>
                            <li className="nav-item">
                                <Link to='/stats' className="nav-link">Stats</Link>
                            </li>
                        </ul>
                    </div>
                </nav>
            </header>
        )
    }
}
export default Header;