import React from 'react'
import { Navbar, Nav, NavItem } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'

const GuestNavbar = function () {
  return (
    <Navbar>
      <Nav>
        <LinkContainer to="/login">
          <NavItem eventKey={2}>Enter</NavItem>
        </LinkContainer>
        <LinkContainer to="/register">
          <NavItem eventKey={2}>Register</NavItem>
        </LinkContainer>
      </Nav>
    </Navbar>
  )
}

export default GuestNavbar
