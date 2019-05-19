import React from 'react'
import { Route, Redirect } from 'react-router-dom'
import Auth from '../service/Auth'
import PropTypes from 'prop-types'

const PrivateRoute = ({ component: Component, ...rest }) => (
  <Route
    {...rest}
    render={props =>
      Auth.getToken() ? (
        <Component {...rest} {...props} />
      ) : (
        <Redirect
          to={{
            pathname: '/login',
            state: { from: props.location }
          }}
        />
      )
    }
  />
)

PrivateRoute.propTypes = {
  component: PropTypes.element.isRequired,
  location: PropTypes.object
}

export default PrivateRoute
