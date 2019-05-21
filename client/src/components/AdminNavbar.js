import React from 'react'
import { Navbar, Nav, NavItem } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'

const AdminNavbar = function () {
  return (
    <Navbar>
      <Nav>
        <LinkContainer exact to="/">
          <NavItem eventKey={1}>Home</NavItem>
        </LinkContainer>
        <LinkContainer to="/register">
          <NavItem eventKey={2}>Register new client</NavItem>
        </LinkContainer>
        <LinkContainer to="/delete-client">
          <NavItem eventKey={3}>Delete client</NavItem>
        </LinkContainer>
        <LinkContainer to="/register-active-principle">
          <NavItem eventKey={4}>Register active principle</NavItem>
        </LinkContainer>
        <LinkContainer to="/logout">
          <NavItem eventKey={5}>Logout</NavItem>
        </LinkContainer>
      </Nav>
    </Navbar>
  )
}

export default AdminNavbar
