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
import ClientListContainer from './containers/ClientListContainer'
import RegisterActivePrincipleContainer from './containers/RegisterActivePrincipleContainer'
import ActivePrincipleListContainer from './containers/ActivePrincipleListContainer'
import ModifyActivePrincipleContainer from './containers/ModifyActivePrincipleContainer'
import ModifyClientContainer from './containers/ModifyClientContainer'
import PasswordRecoveryContainer from './containers/PasswordRecoveryContainer'
import RegisterProductContainer from './containers/RegisterProductContainer'
import ProductListContainer from './containers/ProductListContainer'
import ModifyProductContainer from './containers/ModifyProductContainer'
import CompanyDataListcontainer from './containers/CompanyDataListContainer'
import ModifyCompanyDataContainer from './containers/ModifyCompanyDataContainer'
import RegisterHelpModuleContainer from './containers/RegisterHelpModuleContainer'
import HelpModuleListContainer from './containers/HelpModuleListContainer'
import ModifyHelpModuleContainer from './containers/ModifyHelpModuleContainer'

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
              <Route path="/password-recovery" component={PasswordRecoveryContainer} />
              <PrivateRoute exact path="/client-list" component={ClientListContainer} />
              <PrivateRoute exact path="/register-active-principle" component={RegisterActivePrincipleContainer} />
              <PrivateRoute exact path="/active-principle-list" component={ActivePrincipleListContainer} />
              <PrivateRoute exact path="/modify-active-principle" component={ModifyActivePrincipleContainer} />
              <PrivateRoute exact path="/modify-client" component={ModifyClientContainer} />
              <PrivateRoute exact path="/register-product" component={RegisterProductContainer} />
              <PrivateRoute exact path="/product-list" component={ProductListContainer} />
              <PrivateRoute exact path="/modify-product" component={ModifyProductContainer} />
              <PrivateRoute exact path="/company-data-list" component={CompanyDataListcontainer} />
              <PrivateRoute exact path="/modify-company-data" component={ModifyCompanyDataContainer} />
              <PrivateRoute exact path="/register-help-module" component={RegisterHelpModuleContainer} />
              <PrivateRoute exact path="/help-module-list" component={HelpModuleListContainer} />
              <PrivateRoute exact path="/modify-help-module" component={ModifyHelpModuleContainer} />
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
