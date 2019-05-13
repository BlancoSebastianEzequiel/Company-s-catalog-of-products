import React from 'react'
import { Route, Redirect } from 'react-router-dom'
import Auth from '../service/Auth'

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

export default PrivateRoute
