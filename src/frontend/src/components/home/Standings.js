import React from 'react'
import './css/standings.css';

export default function Standings(props) {
    return (
        <div>
            <table className="table table-sm table-hover table-bordered table-striped table-light">
                <thead>
                    <tr>
                        <th scope="col"><span className="full ">Position</span><span className="abbr">Pos</span></th>
                        {props.standings[0] && Object.keys(props.standings[0]).map((item,index)=>{
                            switch(item) {
                                case "Position":
                                    return <th scope="col" key={index}><span className="full">{item}</span><span className="abbr">Pos</span></th>;
                                    break;
                                case "Played":
                                    return <th scope="col" key={index}><span className="full">{item}</span><span className="abbr">P</span></th>;
                                break;
                                case "Won":
                                    return <th scope="col" key={index}><span className="full">{item}</span><span className="abbr">W</span></th>;
                                    break;
                                case "Drawn":
                                    return <th scope="col" key={index}><span className="full">{item}</span><span className="abbr">D</span></th>;
                                    break;
                                case "Lost":
                                    return <th scope="col" key={index}><span className="full">{item}</span><span className="abbr">L</span></th>;
                                    break;
                                case "Points":
                                    return <th scope="col" key={index}><span className="full">{item}</span><span className="abbr">Pts</span></th>;
                                break;
                                default:
                                    return <th scope="col" key={index}>{item}</th>;
                            }
                        })}
                    </tr>
                </thead>
                <tbody>
                    {props.standings && props.standings.map((row,index) => {
                        return (
                        <tr>
                            <th className="align-middle text-center" scope="row">{index+1}</th>
                            <td className="align-middle text-center">
                                <span className="badge"><img src={row.Club[2]} alt={row.Club[0] + "badge"} /></span>
                                <span className="full">{row.Club[0]}</span>
                                <span className="abbr">{row.Club[1]}</span>
                            </td>
                            <td className="align-middle text-center">{row.Played}</td>
                            <td className="align-middle text-center">{row.Won}</td>
                            <td className="align-middle text-center">{row.Drawn}</td>
                            <td className="align-middle text-center">{row.Lost}</td>
                            <td className="align-middle text-center">{row.GF}</td>
                            <td className="align-middle text-center">{row.GA}</td>
                            <td className="align-middle text-center">{row.GD}</td>
                            <td className="align-middle text-center">{row.Points}</td>
                        </tr>
                        );
                    })}
                </tbody>
            </table>
        </div>
    )
}
