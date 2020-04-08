import React from 'react';
import './css/footer.css';

export default function Footer() {
    return (
        <footer>
            <div className="container">
                <div className="row footer-top">
                    <div className="col info">
                        <img id="logo-footer" className="img-responsive" src="/static/resources/logo.png" alt="logo" />
                        <p>This website is a personal project of mine inspired by my love for anything football/soccer related and evidently, the Premier League.
                            I am proud to share this website, and I will aim to maintain and add features frequently. It was built
                            using the Django Python Web Framework for the backend and ReactJS for the frontend.
                        </p>
                    </div>
                    <div className="col about-me">
                        <div className="about-me-top">
                            <img id="me" className="img-responsive" src="/static/resources/me.png" alt="creator's photo" />
                            <ul className="me-list"> 
                                <li>Dillon Bourne</li>
                                <li>MSc. Computer Science</li>
                                <li>University of Guelph</li>
                            </ul>
                        </div>
                        <p id="bio">I describe myself as self-motivated, eager & ambitious. At UofG I specialized in Artificial Intelligence, 
                        Machine Learning & Optimization. Although challenging, I succeeded and learnt more than I ever thought I could. I
                        aspire to be a Backend Web-Developer or anything requiring complex logical thinking because that is where I thrive.</p>
                    </div>
                </div>
                <div className="row footer-bottom">
                    <div className="col contact-info">
                        <ul className="social-icons">
                            <li><a target="_blank" href="https://www.linkedin.com/in/dillon-bourne-87185b121/" className="social-icon"> <i className="fa fa-linkedin"></i></a></li>
                            <li><a target="_blank" href="https://github.com/GingerLion?tab=repositories" className="social-icon"> <i className="fa fa-github"></i></a></li>
                            <li><a target="_blank" href="mailto:dbourne246@gmail.com" className="social-icon"> <i className="fa fa-google"></i></a></li>
                            <li>
                                <a target="_blank" href="tel:519-993-6316" className="social-icon"><i className="fa fa-whatsapp"></i></a>
                            </li>
                        </ul>
                        <p>&copy; Premier League Addict. All rights reserved.</p>
                    </div>
                </div>
            </div>
        </footer>
    )
}
