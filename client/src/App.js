import React, { Component } from 'react'
import LoginContainer from './containers/LoginContainer'
import RegisterContainer from './containers/RegisterContainer'
import LoggedNavbar from './components/LoggedNavbar'
import GuestNavbar from './components/GuestNavbar'
import { BrowserRouter as Router, Redirect, Route } from 'react-router-dom'
import PropTypes from 'prop-types'
import Auth from './service/Auth'
import 'react-toastify/dist/ReactToastify.css'

import './App.css'
import PrivateRoute from './components/PrivateRoute'
import DeleteClientContainer from './containers/DeleteClientContainer'
import RegisterActivePrincipleContainer from './containers/RegisterActivePrincipleContainer'

class App extends Component {
  constructor (props) {
    super(props)
    Auth.setApp(this)
    this.state = {
      user: null,
      token: null
    }
  }

  loginOk () {
    this.setState(this.state)
  }

  render () {
    return (
      <React.Fragment>
        <div>
          <Router>
            <div>
              { Auth.isLogged() ? <LoggedNavbar /> : <GuestNavbar/> }

              <Route path="/login"
                render={routeProps => <LoginContainer {...routeProps} onLogin={ () => this.setState(this.state) }/>} />
              <Route path="/logout"
                render={routeProps => <Logout {...routeProps} onLogout={ () => this.setState(this.state) }/>} />
              <Route path="/register" component={RegisterContainer} />
              <PrivateRoute exact path="/delete-client" component={DeleteClientContainer} />
              <PrivateRoute exact path="/register-active-principle" component={RegisterActivePrincipleContainer} />
            </div>
          </Router>
        </div>
      </React.Fragment>
    )
  }
}

const Logout = (props) => {
  Auth.logout()
  props.onLogout() // Hack to refresh NavBar
  return <Redirect to='/' />
}

Logout.propTypes = {
  onLogout: PropTypes.func
}

export default App
