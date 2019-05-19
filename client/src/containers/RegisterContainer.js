import React from 'react'
import { ToastContainer, toast } from 'react-toastify'
import RegisterForm from '../components/RegisterForm'
import { Redirect } from 'react-router-dom'
import Http from '../service/Http'
import httpStatus from 'http-status-codes'
import Auth from '../service/Auth'

export default class RegisterContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      redirectTo: false,
      errors: {},
      urlToRedirect: '/login'
    }
  }

  handleClick (data) {
    if (data.password.localeCompare(data.passConfirmation) !== 0) {
      this.setState({ errors: { passConfirmation: 'passwords do not match' } })
    } else {
      delete data.passConfirmation
      Http.post('/users/', data)
        .then(response => {
          if (response.status === httpStatus.CREATED) {
            if (Auth.isAdmin()) {
              this.setState({ urlToRedirect: '/delete-client' })
            } else {
              this.setState({ urlToRedirect: '/login' })
              Auth.setTypeOfUser(data.type)
            }
            this.setState({ redirectTo: true })
            toast('user successfully created!')
          } else {
            toast('The user could not be created, please verify the data')
            this.setState({ errors: { 'message': response.content.data } })
          }
        })
        .catch(err => {
          toast('Error creating user: ' + err) // TODO hacer algo
        })
    }
  }

  render () {
    const { redirectTo, errors, urlToRedirect } = this.state
    if (redirectTo) {
      return <Redirect to={urlToRedirect}/>
    }
    return (
      <div>
        <ToastContainer></ToastContainer>
        <RegisterForm
          errors={errors}
          onClick={(data) => this.handleClick(data)}
        />
      </div>
    )
  }
}
