import React from 'react'

export default function Carousel(props) {
    return (
        <div id="carouselExampleIndicators" className="carousel slide" data-ride="carousel">
            <ol className="carousel-indicators">
                <li data-target="#carouselExampleIndicators" data-slide-to="0" className="active"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
            </ol>
            <div className="carousel-inner">
                <div className="carousel-item active">
                    <img className="d-block w-100" src={props.images.image1} alt="First slide" />
                    <div class="carousel-caption d-none d-md-block">
                        <h5>{props.captions.cap1}</h5>
                        <p>...</p>
                    </div>
                </div>
                <div className="carousel-item">
                    <img className="d-block w-100" src={props.images.image2} alt="Second slide" />
                    <div class="carousel-caption d-none d-md-block">
                    <h5>{props.captions.cap2}</h5>
                        <p>...</p>
                    </div>
                </div>
                <div className="carousel-item">
                    <img className="d-block w-100" src={props.images.image3} alt="Third slide" />
                    <div class="carousel-caption d-none d-md-block">
                        <h5>{props.captions.cap3}</h5>
                        <p>...</p>
                    </div>
                </div>
            </div>
            <a className="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                <span className="carousel-control-prev-icon" aria-hidden="true"></span>
                <span className="sr-only">Previous</span>
            </a>
            <a className="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                <span className="carousel-control-next-icon" aria-hidden="true"></span>
                <span className="sr-only">Next</span>
            </a>
        </div>
    )
}
