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
        <LinkContainer to="/help-module-list">
          <NavItem eventKey={4}>Help module list</NavItem>
        </LinkContainer>
        <LinkContainer to="/contact-us">
          <NavItem eventKey={5}>Contact us</NavItem>
        </LinkContainer>
        <LinkContainer to="/logout">
          <NavItem eventKey={6}>Logout</NavItem>
        </LinkContainer>
      </Nav>
    </Navbar>
  )
}

export default ClientNavbar
