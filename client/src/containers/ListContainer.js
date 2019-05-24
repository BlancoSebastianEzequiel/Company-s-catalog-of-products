import React from 'react'
import { Redirect } from 'react-router-dom'
import { ToastContainer, toast } from 'react-toastify'
import ListForm from '../components/ListForm'
import Http from '../service/Http'
import httpStatus from 'http-status-codes'
import PropTypes from 'prop-types'

export default class ListContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      errors: {},
      refresh: true,
      objects: [{
        'data': '',
        '_id': ''
      }],
      redirectTo: false,
      urlToRedirect: this.props.urlToRedirect,
      dataToRedirect: {}
    }
  }

  handleChange = (name, value) => {
    this.setState({
      [name]: value
    })
  }

  getObjects = () => {
    if (!this.state.refresh) return
    let objectsVector = []
    Http.get(this.props.query)
      .then(response => {
        if (response.status === httpStatus.OK) {
          const length = response.content.data.length
          for (let i = 0; i < length; i++) {
            const anObject = response.content.data[i]
            objectsVector.push(this.props.writeInfo(anObject))
          }
          this.handleChange('objects', objectsVector)
          this.handleChange('refresh', false)
        } else {
          toast('ERROR: ' + response.content.data)
        }
      })
      .catch(err => {
        toast('ERROR: ' + err)
      })
  }

  modifyObject = (anObject) => {
    this.setState({ redirectTo: true })
    this.setState({ dataToRedirect: anObject })
  }

  deleteObject = (anObject) => {
    Http.delete(this.props.url, anObject._id)
      .then(response => {
        if (response.status === httpStatus.OK) {
          this.setState({ 'refresh': true })
          toast('The deletion succeed')
        } else {
          toast('The deletion did not succeed: ' + response.content.data)
        }
      })
      .catch(err => {
        toast('ERROR: ' + err)
      })
  }

  render () {
    const { errors, objects, redirectTo, urlToRedirect, dataToRedirect } = this.state
    if (redirectTo) {
      return <Redirect to={{
        pathname: urlToRedirect,
        state: { id: dataToRedirect._id }
      }}
      />
    }
    return (
      <div>
        <ToastContainer></ToastContainer>
        <ListForm
          errors={errors}
          ObjectsList={objects}
          getList={() => this.getObjects()}
          deleteObject={(anObject => this.deleteObject(anObject))}
          modifyObject={(anObject) => this.modifyObject(anObject)}
        />
      </div>
    )
  }
}

ListContainer.propTypes = {
  url: PropTypes.string,
  query: PropTypes.string,
  writeInfo: PropTypes.func,
  urlToRedirect: PropTypes.string
}
