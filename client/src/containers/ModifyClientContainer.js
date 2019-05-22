import React from 'react'
import { ToastContainer, toast } from 'react-toastify'
import PostingForm from '../components/PostingForm'
import { Redirect } from 'react-router-dom'
import Http from '../service/Http'
import httpStatus from 'http-status-codes'
import PropTypes from 'prop-types'
import data from '../data/clientData'

export default class ModifyClientContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      redirectTo: false,
      errors: {},
      urlToRedirect: '/delete-client',
      fieldsState: data.fieldsState,
      fields: data.fields,
      title: 'Modify client'
    }
  }

  modifyClient = (data) => {
    const _id = this.props.location.state.id
    data['_id'] = _id
    Http.patch('/users/', data)
      .then(response => {
        if (response.status === httpStatus.CREATED) {
          this.setState({ redirectTo: true })
          toast('user successfully modified!')
        } else {
          toast('The user could not be modified, please verify the data')
          this.setState({ errors: { 'message': response.content.data } })
        }
      })
      .catch(err => {
        toast('Error modifying active principle: ' + err)
      })
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
          onClick={(data) => this.modifyClient(data)}
          fields={fields}
          fieldsState={fieldsState}
          title={title}
        />
      </div>
    )
  }
}

ModifyClientContainer.propTypes = {
  location: PropTypes.object
}
