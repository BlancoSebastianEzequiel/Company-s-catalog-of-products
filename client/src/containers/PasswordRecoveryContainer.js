import React from 'react'
import { ToastContainer, toast } from 'react-toastify'
import PostingForm from '../components/PostingForm'
import Http from '../service/Http'
import httpStatus from 'http-status-codes'
import data from '../data/passwordRecoveryData'

export default class PasswordRecoveryContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
    errors: {},
    fieldsState: data.fieldsState,
    fields: data.fields,
    title: 'Password Recovery'
    }
  }

  handleClick (data) {
    Http.get('/password_recovery/' + data.email + '/')
      .then(response => {
        if (response.status === httpStatus.OK) {
          toast(response.content.data)
        } else {
          this.setState({ errors: { 'message': response.content.data } })
        }
      })
      .catch(err => {
        toast('Error: ' + err)
      })
  }

  render () {
    const { errors, fields, fieldsState, title } = this.state
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
