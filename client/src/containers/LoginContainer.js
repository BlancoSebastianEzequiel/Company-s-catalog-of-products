import React from 'react'
import LoginForm from '../components/LoginForm'
import { Redirect } from 'react-router-dom'
import Http from '../service/Http'
import Auth from '../service/Auth'
import PropTypes from 'prop-types'
import httpStatus from 'http-status-codes'

export default class LoginContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      redirectToReferrer: false
    }
  }

  handleClick (data) {
    const { email, password } = data
    Http.post('/session/', { email, password }, () => {})
      .then(response => {
        const data = response.content
        if (response.status === httpStatus.OK && data && data.token) {
          Auth.login(data.token)
          this.setState({ redirectToReferrer: true })
          this.props.onLogin() // Hack to refresh NavBar
        } else {
          alert('invalid user or password')
        }
      })
      .catch(err => {
        alert('Auth Error' + err) // TODO
      })
  }

  render () {
    const { from } = this.props.location.state || { from: { pathname: '/' } }
    const token = Auth.getToken()
    const { redirectToReferrer } = this.state

    if (redirectToReferrer) {
      return <Redirect to={from} />
    }
    if (token) {
      return <Redirect to='/' />
    }
    return (
      <LoginForm onClick={(data) => this.handleClick(data)} />
    )
  }
}

LoginContainer.propTypes = {
  onLogin: PropTypes.func,
  location: PropTypes.shape({ state: PropTypes.object })
}
