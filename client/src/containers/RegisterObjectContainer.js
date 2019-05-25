import React from 'react'
import { ToastContainer, toast } from 'react-toastify'
import PostingForm from '../components/PostingForm'
import { Redirect } from 'react-router-dom'
import Http from '../service/Http'
import httpStatus from 'http-status-codes'
import PropTypes from 'prop-types'

export default class RegisterObjectContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      redirectTo: false,
      errors: {},
      urlToRedirect: this.props.urlToRedirect,
      fieldsState: this.props.fieldsState,
      fields: this.props.fields,
      title: this.props.title
    }
  }

  handleClick (data) {
    Http.post(this.props.endpoint, data)
      .then(response => {
        if (response.status === httpStatus.CREATED) {
          this.setState({ redirectTo: true })
          toast('The ' + this.props.objectName + ' successfully created!')
        } else {
          toast('The ' + this.props.objectName + ' could not be created, please verify the data')
          this.setState({ errors: { 'message': response.content.data } })
        }
      })
      .catch(err => {
        toast('Error creating ' + this.props.objectName + ': ' + err) // TODO hacer algo
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
          onClick={(data) => this.handleClick(data)}
          fields={fields}
          fieldsState={fieldsState}
          title={title}
        />
      </div>
    )
  }
}

RegisterObjectContainer.propTypes = {
  fields: PropTypes.array,
  fieldsState: PropTypes.object,
  title: PropTypes.string,
  objectName: PropTypes.string,
  endpoint: PropTypes.string,
  urlToRedirect: PropTypes.string
}
