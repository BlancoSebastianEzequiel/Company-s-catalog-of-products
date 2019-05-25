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
      errors: {},
      redirectToReferrer: false
    }
  }

  setTypeOfUser (email) {
    return Http.get('/users/?email=' + email)
      .then(response => {
        if (response.status === httpStatus.OK) {
          const user = response.content.data[0]
          Auth.setTypeOfUser(user.type)
        } else {
          this.setState({ errors: { 'message': response.content.data } })
        }
      })
      .catch(err => {
        this.setState({ errors: { 'message': err } })
        alert('Error: ' + err)
      })
  }

  handleClick (data) {
    const { email, password } = data
    Http.post('/session/', { email, password })
      .then(response => {
        const token = response.content.data
        if (response.status === httpStatus.CREATED && token) {
          Auth.login(token)
          this.setTypeOfUser(email)
            .then(() => {
              this.setState({ redirectToReferrer: true })
              this.props.onLogin() // Hack to refresh NavBar
            })
        } else {
          this.setState({ errors: { 'message': response.content.data } })
        }
      })
      .catch(err => {
        alert('Error: ' + err)
      })
  }

  render () {
    const { from } = this.props.location.state || { from: { pathname: '/' } }
    const token = Auth.getToken()
    const { redirectToReferrer, errors } = this.state

    if (redirectToReferrer) {
      return <Redirect to={from} />
    }
    if (token) {
      return <Redirect to='/' />
    }
    return (
      <LoginForm
        errors={errors}
        onClick={(data) => this.handleClick(data)}
      />
    )
  }
}

LoginContainer.propTypes = {
  onLogin: PropTypes.func,
  location: PropTypes.shape({ state: PropTypes.object })
}
