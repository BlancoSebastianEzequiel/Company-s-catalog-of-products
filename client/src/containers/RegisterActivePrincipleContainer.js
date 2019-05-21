import React from 'react'
import { ToastContainer, toast } from 'react-toastify'
import RegisterActivePrincipleForm from '../components/RegisterActivePrincipleForm'
import { Redirect } from 'react-router-dom'
import Http from '../service/Http'
import httpStatus from 'http-status-codes'

export default class RegisterActivePrincipleContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      redirectTo: false,
      errors: {},
      urlToRedirect: '/active-principle-list'
    }
  }

  handleClick (data) {
    Http.post('/active_principle/', data)
      .then(response => {
        if (response.status === httpStatus.CREATED) {
          this.setState({ redirectTo: true })
          toast('active principle successfully created!')
        } else {
          toast('The active principle could not be created, please verify the data')
          this.setState({ errors: { 'message': response.content.data } })
        }
      })
      .catch(err => {
        toast('Error creating active principle: ' + err) // TODO hacer algo
      })
  }

  render () {
    const { redirectTo, errors, urlToRedirect } = this.state
    if (redirectTo) {
      return <Redirect to={urlToRedirect}/>
    }
    return (
      <div>
        <ToastContainer></ToastContainer>
        <RegisterActivePrincipleForm
          errors={errors}
          onClick={(data) => this.handleClick(data)}
        />
      </div>
    )
  }
}
