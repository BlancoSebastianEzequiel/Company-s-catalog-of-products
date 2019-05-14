import React from 'react'
import { ToastContainer, toast } from 'react-toastify'
import RegisterForm from '../components/RegisterForm'
import { Redirect } from 'react-router-dom'
import Http from '../service/Http'
import httpStatus from 'http-status-codes'

export default class RegisterContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      redirectToLogin: false,
      errors: {}
    }
  }

  handleClick (data) {
    if (data.password.localeCompare(data.passConfirmation) !== 0) {
      this.setState({ errors: { passConfirmation: 'passwords do not match' } })
    } else {
      delete data.passConfirmation
      alert("here ")
      Http.post('/users/', data)
        .then(response => {
          if (response.status === httpStatus.CREATED) {
            toast('user successfully created!')
            this.setState({ redirectToLogin: true })
          } else {
            toast('The user could not be created, please verify the data')
            this.setState({ errors: response.content.errors })
          }
        })
        .catch(err => {
          toast('Error creating user: ' + err) // TODO hacer algo
        })
    }
  }

  render () {
    const { redirectToLogin, errors } = this.state
    if (redirectToLogin) {
      return <Redirect to='/login' />
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
