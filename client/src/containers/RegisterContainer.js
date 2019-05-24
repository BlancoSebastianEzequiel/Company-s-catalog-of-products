import React from 'react'
import { ToastContainer, toast } from 'react-toastify'
import PostingForm from '../components/PostingForm'
import { Redirect } from 'react-router-dom'
import Http from '../service/Http'
import httpStatus from 'http-status-codes'
import Auth from '../service/Auth'
import data from '../data/clientData'

export default class RegisterContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      redirectTo: false,
      errors: {},
      urlToRedirect: '/login',
      fieldsState: data.fieldsState,
      fields: data.fields,
      title: 'Register'
    }
  }

  handleClick (data) {
    if (data.password.localeCompare(data.passConfirmation) !== 0) {
      this.setState({ errors: { 'message': 'passwords do not match' } })
    } else {
      delete data.passConfirmation
      Http.post('/users/', data)
        .then(response => {
          if (response.status === httpStatus.CREATED) {
            if (Auth.isLogged()) {
              this.setState({ urlToRedirect: '/client-list' })
            } else {
              this.setState({ urlToRedirect: '/login' })
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
    const { redirectTo, errors, urlToRedirect, fieldsState, fields, title } = this.state
    if (redirectTo) {
      return <Redirect to={urlToRedirect}/>
    }
    return (
      <div>
        <ToastContainer></ToastContainer>
        <PostingForm
          errors={errors}
          onClick={(data) => this.handleClick(data)}
          fields={fields}
          fieldsState={fieldsState}
          title={title}
        />
      </div>
    )
  }
}
