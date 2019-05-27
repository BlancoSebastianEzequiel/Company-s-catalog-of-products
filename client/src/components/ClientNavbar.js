import React from 'react'
import { Navbar, Nav, NavItem } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'

const ClientNavbar = function () {
  return (
    <Navbar>
      <Nav>
        <LinkContainer exact to="/">
          <NavItem eventKey={1}>Home</NavItem>
        </LinkContainer>
        <LinkContainer to="/product-list">
          <NavItem eventKey={2}>Product list</NavItem>
        </LinkContainer>
        <LinkContainer to="/company-data-list">
          <NavItem eventKey={3}>Company data list</NavItem>
        </LinkContainer>
        <LinkContainer to="/logout">
          <NavItem eventKey={4}>Logout</NavItem>
        </LinkContainer>
      </Nav>
    </Navbar>
  )
}

export default ClientNavbar
