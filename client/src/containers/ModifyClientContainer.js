import React from 'react'
import { ToastContainer, toast } from 'react-toastify'
import RegisterForm from '../components/RegisterForm'
import { Redirect } from 'react-router-dom'
import Http from '../service/Http'
import httpStatus from 'http-status-codes'
import PropTypes from 'prop-types'

export default class ModifyClientContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      redirectTo: false,
      errors: {},
      urlToRedirect: '/delete-client'
    }
  }

  modifyClient = (data) => {
    const _id = this.props.location.state.id
    data['_id'] = _id
    Http.put('/users/', data)
      .then(response => {
        if (response.status === httpStatus.CREATED) {
          this.setState({ redirectTo: true })
          toast('user successfully updated!')
        } else {
          toast('The user could not be updated, please verify the data')
          this.setState({ errors: { 'message': response.content.data } })
        }
      })
      .catch(err => {
        toast('Error updating active principle: ' + err)
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
          onClick={(data) => this.modifyClient(data)}
        />
      </div>
    )
  }
}

ModifyClientContainer.propTypes = {
  location: PropTypes.object
}
