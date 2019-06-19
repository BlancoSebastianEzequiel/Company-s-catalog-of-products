import React from 'react'
import { ToastContainer, toast } from 'react-toastify'
import PostingForm from '../components/PostingForm'
import { Redirect } from 'react-router-dom'
import Http from '../service/Http'
import httpStatus from 'http-status-codes'
import PropTypes from 'prop-types'

export default class ModifyContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      redirectTo: false,
      errors: {},
      urlToRedirect: this.props.urlToRedirect
    }
  }

  filterEmptyFields (data) {
    let filteredData = {}
    for (let field in data) {
      if (data[field].length === 0) {
        continue
      }
      filteredData[field] = data[field]
    }
    return filteredData
  }

  modifyObject = (data) => {
    data['_id'] = this.props.id
    data = this.filterEmptyFields(data)
    Http.patch(this.props.endpoint, data)
      .then(response => {
        if (response.status === httpStatus.CREATED) {
          this.setState({ redirectTo: true })
          toast(this.props.objectName + ' successfully modified!')
        } else {
          toast(this.props.objectName + ' could not be modified, please verify the data')
          this.setState({ errors: { 'message': response.content.data } })
        }
      })
      .catch(err => {
        toast('Error modifying ' + this.props.objectName + ': ' + err)
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
        <PostingForm
          errors={errors}
          onClick={(data) => this.modifyObject(data)}
          fields={this.props.fields}
          fieldsState={this.props.fieldsState}
          title={this.props.title}
        />
      </div>
    )
  }
}

ModifyContainer.propTypes = {
  fields: PropTypes.array,
  fieldsState: PropTypes.object,
  title: PropTypes.string,
  objectName: PropTypes.string,
  endpoint: PropTypes.string,
  urlToRedirect: PropTypes.string,
  id: PropTypes.string
}
