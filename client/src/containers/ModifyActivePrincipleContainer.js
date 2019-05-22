import React from 'react'
import { ToastContainer, toast } from 'react-toastify'
import PostingForm from '../components/PostingForm'
import { Redirect } from 'react-router-dom'
import Http from '../service/Http'
import httpStatus from 'http-status-codes'
import PropTypes from 'prop-types'
import data from '../data/activePrincipleData'

export default class ModifyActivePrincipleContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      redirectTo: false,
      errors: {},
      urlToRedirect: '/active-principle-list',
      fieldsState: data.fieldsState,
      fields: data.fields,
      title: 'Update active principle'
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
    const { redirectTo, errors, urlToRedirect, fields, fieldsState, title } = this.state
    if (redirectTo) {
      return <Redirect to={urlToRedirect}/>
    }
    return (
      <div>
        <ToastContainer></ToastContainer>
        <PostingForm
          errors={errors}
          onClick={(data) => this.modifyActivePrinciple(data)}
          fields={fields}
          fieldsState={fieldsState}
          title={title}
        />
      </div>
    )
  }
}

ModifyActivePrincipleContainer.propTypes = {
  location: PropTypes.object
}
