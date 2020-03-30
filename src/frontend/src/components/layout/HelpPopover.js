import React from 'react'
import { MDBPopover,  MDBPopoverBody, MDBPopoverHeader, MDBBtn } from 'mdbreact';

export default function HelpPopover(props) {
    return (
        <MDBPopover 
        placement="bottom"
        popover
        clickable
        id="scatter-popper"
        >
        <MDBBtn style={props.hp.popBtnStyle}>{props.hp.buttonText}</MDBBtn>
        <div>
            <MDBPopoverHeader>{props.hp.title}</MDBPopoverHeader>
            <MDBPopoverBody>
                {props.hp.body}
            </MDBPopoverBody>
        </div>
        </MDBPopover>
    )
}
