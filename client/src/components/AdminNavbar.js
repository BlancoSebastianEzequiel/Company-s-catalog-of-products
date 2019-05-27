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
        <LinkContainer to="/client-list">
          <NavItem eventKey={3}>Client list</NavItem>
        </LinkContainer>
        <LinkContainer to="/register-active-principle">
          <NavItem eventKey={4}>Register active principle</NavItem>
        </LinkContainer>
        <LinkContainer to="/active-principle-list">
          <NavItem eventKey={4}>Active principle list</NavItem>
        </LinkContainer>
        <LinkContainer to="/register-product">
          <NavItem eventKey={5}>Register product</NavItem>
        </LinkContainer>
        <LinkContainer to="/product-list">
          <NavItem eventKey={6}>Product list</NavItem>
        </LinkContainer>
        <LinkContainer to="/company-data-list">
          <NavItem eventKey={7}>Company data list</NavItem>
        </LinkContainer>
        <LinkContainer to="/logout">
          <NavItem eventKey={8}>Logout</NavItem>
        </LinkContainer>
      </Nav>
    </Navbar>
  )
}

export default AdminNavbar
