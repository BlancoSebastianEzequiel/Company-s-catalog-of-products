import React from 'react'
import { ToastContainer, toast } from 'react-toastify'
import RegisterForm from '../components/RegisterForm'
import { Redirect } from 'react-router-dom'
import Http from '../service/Http'
import httpStatus from 'http-status-codes'

export default class ModifyActivePrincipleContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      redirectTo: false,
      errors: {},
      urlToRedirect: '/active-principle-list'
    }
  }

  modifyActivePrinciple = (data) => {
    const _id = this.props.location.state.id
    data['_id'] = _id
    Http.put('/active-principle/', data)
      .then(response => {
        if (response.status === httpStatus.CREATED) {
          this.setState({ redirectTo: true })
          toast('active principle successfully updated!')
        } else {
          toast('The active principle could not be updated, please verify the data')
          this.setState({ errors: { 'message': response.content.data } })
        }
      })
      .catch(err => {
        toast('Error creating active principle: ' + err)
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
        <RegisterForm
          errors={errors}
          onClick={(data) => this.modifyActivePrinciple(data)}
        />
      </div>
    )
  }
}
