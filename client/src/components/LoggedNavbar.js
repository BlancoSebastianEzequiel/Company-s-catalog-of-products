import React from 'react'
import { Navbar, Nav } from 'react-bootstrap'
import AdminNavbar from './AdminNavbar'
import ClientNavbar from './ClientNavbar'
import Auth from '../service/Auth'

const LoggedNavbar = function () {
  return (
    <Navbar>
      <Nav>
        { Auth.isAdmin() ? <AdminNavbar/> : <ClientNavbar/> }
      </Nav>
    </Navbar>
  )
}

export default LoggedNavbar
